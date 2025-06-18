Este archivo documenta cómo el equipo debe escribir los mensajes de commit utilizando el estándar de **Conventional Commits**:

---

# Conventional Commits

Este documento define cómo estructurar los mensajes de commit en el proyecto, utilizando las convenciones del estándar **Conventional Commits**. El objetivo es mantener un historial de cambios claro y coherente, facilitar la generación de changelogs y el versionado semántico.

## Estructura de un Commit

Un mensaje de commit sigue esta estructura básica:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Ejemplo

```
feat(auth): add JWT authentication for user login

- Implemented JWT-based authentication for user login and session management.
- Updated user model to support token generation and validation.
- Added tests for the new authentication flow.

BREAKING CHANGE: The login API now requires a JWT token.
```

## Tipos de Commits

Los siguientes son los tipos de commit permitidos:

### `feat`
Usado cuando se añade una nueva funcionalidad al proyecto.

Ejemplo:
```
feat(payment): add support for multiple payment methods
```

### `fix`
Usado para corregir errores en el código.

Ejemplo:
```
fix(cart): resolve issue with incorrect total calculation
```

### `docs`
Usado para cambios en la documentación solamente.

Ejemplo:
```
docs: update README with installation instructions
```

### `style`
Usado para cambios que no afectan la lógica del código, solo el estilo (espacios, comas, etc.).

Ejemplo:
```
style: format code using Black
```

### `refactor`
Usado para cambios en el código que no corrigen errores ni añaden nuevas funcionalidades, pero mejoran la estructura o legibilidad.

Ejemplo:
```
refactor(api): simplify user data fetching logic
```

### `test`
Usado para agregar o modificar pruebas unitarias.

Ejemplo:
```
test(order): add unit tests for order processing module
```

### `chore`
Usado para cambios en las herramientas de construcción, configuración o mantenimiento del proyecto. No afecta el código fuente o las pruebas.

Ejemplo:
```
chore(ci): update GitHub Actions configuration
```

## Alcances (Scopes)

El **scope** (opcional) se usa para especificar la parte del proyecto que se ve afectada. Se debe escribir entre paréntesis justo después del tipo de commit. Algunos ejemplos de scopes pueden ser:

- `auth`
- `api`
- `login`
- `project-creation`

Ejemplo:
```
feat(auth): add social login support
```

## Descripción

La descripción debe ser clara y concisa, con la primera letra en minúscula y sin punto final.

Ejemplo:
```
fix(create-role): correct total
```

## Cuerpo del Commit (opcional)

El cuerpo del commit proporciona detalles adicionales sobre el cambio. Se recomienda usar oraciones completas y describir **qué** se ha hecho y **por qué**.

Ejemplo:
```
fix(cart): correct total price calculation error

The previous implementation was not considering the discount properly, which resulted in incorrect totals for customers with applied discounts.
```

## Pies (Footers) (opcional)

Se utilizan para proporcionar información adicional como **breaking changes** o referencias a issues. Las **breaking changes** deben ir siempre en el footer, precedidas por el texto `BREAKING CHANGE:`.

Ejemplo:
```
BREAKING CHANGE: The login API now requires a JWT token for authentication.
```

También se pueden usar para cerrar issues automáticamente:
```
Closes #123
```

## Ejemplos de Mensajes de Commit

### Nuevo Feature
```
feat(cart): add discount functionality

- Implemented discount application to the cart.
- Updated cart model and API to support discounts.
- Added unit tests for discount calculation.
```

### Corrección de Error
```
fix(api): resolve user authentication issue

Fixed a bug where the authentication token was not being validated correctly.
```

### Documentación
```
docs: update API documentation with new endpoints

Added documentation for the new payment and order tracking endpoints.
```

### Cambio Importante
```
refactor(payment): simplify payment validation logic

BREAKING CHANGE: Removed support for outdated payment method APIs.
```

---

Este archivo proporciona una guía clara sobre cómo realizar commits siguiendo las convenciones de **Conventional Commits**, lo cual ayudará a mantener un historial de commits ordenado y fácil de interpretar para todos los miembros del equipo.