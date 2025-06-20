# Software Requirements Specification: Maintenance Task Management System

## 1. Introduction
Responsive web application for maintenance task management accessible on desktop and mobile devices. Supports three user roles with specific functionalities for creating, executing, and validating maintenance actions.

## 2. User Roles
- **Issuer (Emisor)**: Creates action templates and initiates maintenance tasks
- **Recorder (Registrador)**: Performs follow-ups and records task progress
- **Evaluator (Evaluador)**: Validates completed tasks and approves closures

## 3. Functional Requirements

### 3.1 Action Template (Created by Issuer)
- **Activity ID**: Unique identifier for maintenance activity
- **Source ID**: Identifier for machinery/component requiring maintenance
- **Title**: Name of the maintenance activity
- **Description**: Detailed task instructions
- **Status Field**:
    - Implemented (in progress)
    - Closed (completed)
    - Expired (overdue)
- **Start Date**: Planned commencement date/time
- **End Date**: Planned completion date/time
- **Repetitions**: Boolean indicating recurring tasks
- **Multiple Days**: Boolean indicating multi-day tasks
- **Issuer ID**: Identifier of task creator
- **Evaluator ID**: Identifier of validation authority
- **Recorder ID**: Identifier of task executor
- **Completion Percentage**: Current progress (0-100%)

### 3.2 Action Creation
- Saving completed template creates persistent Action record in database
- Initial status set to "Implemented"
- All template fields preserved in Action record

### 3.3 Follow-up Management (Recorder)
- **Type**: Follow-up category (e.g., inspection, repair)
- **Start Time**: Actual commencement timestamp
- **Duration**: Time spent (minutes)
- **End Time**: Completion timestamp
- **Percentage Completed**: Progress achieved in this follow-up
- **Description**: Work performed details
- **Before Photo**: Image evidence prior to work
- **After Photo**: Image evidence after work

### 3.4 Validation Workflow (Evaluator)
- Triggered when follow-up reaches 100% completion
- Evaluator options:
    - **Approve**: Mark action as "Closed"
    - **Reject**:
        - Adjust actual completion percentage
        - Revert status to "Implemented" or "Expired" (if past end date)
- Automatic status update to "Expired" when end date passes

## 4. System Features

### 4.1 Action Lifecycle Management
- Template-to-Action conversion workflow
- Status transition control (Implemented → Closed/Expired)
- Deadline monitoring with automatic expiration

### 4.2 Follow-up System
- Progress tracking with photo documentation
- Percentage-based completion reporting
- Time tracking with duration calculation

### 4.3 Validation System
- Approval/Rejection workflow for 100% completions
- Percentage adjustment mechanism
- Status override capability for evaluators

### 4.4 Responsive Interface
- Mobile-optimized form inputs
- Adaptive data grids for action listing
- Cross-device photo upload capability

## 5. Data Model Requirements
- **Actions Table**:
    - ID (PK), Activity ID, Source ID, Title, Description, Status
    - StartDate, EndDate, HasRepetitions, MultipleDays
    - IssuerID, EvaluatorID, RecorderID, CompletionPercentage

- **Follow-ups Table**:
    - ID (PK), ActionID (FK), Type, StartTime, Duration
    - EndTime, PercentageCompleted, Description
    - BeforePhotoPath, AfterPhotoPath

## 6. Business Rules
1. Only Issuers can create new action templates
2. Recorders can only modify follow-ups for assigned actions
3. 100% completion requires Evaluator validation
4. Actions automatically expire when end date passes
5. Percentage adjustments after rejection must be <100%

## 7. Non-Functional Requirements
- **Responsiveness**: Mobile-first design supporting all screen sizes
- **Performance**: Action loading <3s on 3G connections
- **Security**: Role-based access control with data isolation
- **Storage**: Image compression (max 2MB per photo)
- **Reliability**: Automatic daily database backups