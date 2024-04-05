from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    nombre_usuario = models.CharField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=100)
    perfil = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    cantidad_mascotas = models.IntegerField(default=0)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Mascotas(models.Model):

    id_mascota = models.AutoField(primary_key=True)   
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    tipo = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    descripcion_fisica = models.TextField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion_personalidad = models.TextField()
    foto = models.ImageField(upload_to='mascotas', null=True, blank=True, multiple=True)
    alimento = models.CharField(max_length=100)

@receiver(post_save, sender=Mascotas)
def actualizar_cantidad_mascotas(sender, instance, created, **kwargs):
    if created:
        usuario = instance.usuario
        usuario.cantidad_mascotas += 1
        usuario.save()


class Agenda(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    duracion = models.IntegerField()
    horas_reservadas = models.IntegerField(default=0)  

    def __str__(self):
        return f"{self.tipo} - {self.fecha} - {self.hora}"
    
class Veterinarias(models.Model):
    id_veterinaria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Especialidades(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre_especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_especialidad

class Vacunas(models.Model):
    id_vacuna = models.AutoField(primary_key=True)
    nombre_vacuna = models.CharField(max_length=100)
    via_aplicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_vacuna

class Staff(models.Model):
    id_staff = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    disponibilidad = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

    
 