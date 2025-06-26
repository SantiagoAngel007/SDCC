from django.db import models

#se crean claase que hacen referencia las tablas de la base de datos para poder hacer la lista de desplegables
class Maquina(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False  # Muy importante: Django no crea ni borra esta tabla
        db_table = 'nombre_real_en_postgresql'  # El nombre exacto de la tabla en la BD

    def __str__(self):
        return f"{self.id} - {self.nombre}"  # Esto se ve en el <select>, lo que se va a mostrar en la lista desplegables es [id - nombre maquina]
    
class Encargado(models.Model):
    
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    class Meta:
        managed = False  
        db_table = 'nombre_real_en_postgresql'  
    
    def __str__(self):
        return f"{self.id} - {self.nombre}"
    
class Emisor(models.Model):
    
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    class Meta:
        managed = False  
        db_table = 'nombre_real_en_postgresql'  
    
    def __str__(self):
        return f"{self.id} - {self.nombre}"
    
class Evaluador(models.Model):
    
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    class Meta:
        managed = False  
        db_table = 'nombre_real_en_postgresql'  
    
    def __str__(self):
        return f"{self.id} - {self.nombre}"
    
#creamos la clase actividades
class Actividades(models.Model):
    
    #colocamos sus atributos
    id = models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=200, blank=False,null=False)
    descripcion=models.TextField(blank=False,null=False)
    tipo = models.CharField(max_length=200, blank=False,null=False)
    fecha_inicio = models.DateField() 
    fecha_final = models.DateField() 
    
    maquina_id = models.IntegerField()
    encargado_id = models.IntegerField()
    evaluador_id = models.IntegerField()
    emisor_id = models.IntegerField()
    
    periodo = models.BooleanField('perido',default=False)
    repeticiones = models.BooleanField('repeticiones',default=False)
    
    estado = models.CharField(max_length=200, blank=False,null=False) 
    
    duracion = models.IntegerField()
    
    porcentaje = models.IntegerField()
    
    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['titulo']
        
    #esta funcion permite identificar cada objeto instanciado por su nombre     
    def __str__(self):
        return str(self.titulo) if self.titulo else "Sin nombre"
    
    
