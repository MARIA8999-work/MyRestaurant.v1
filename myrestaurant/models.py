from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#usuarios
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    contrasena = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=20, default='cliente')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nombre


# platillos
class Platillo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=50)
    es_vegano = models.BooleanField(default=False)
    contiene_alergenos = models.BooleanField(default=False)
    imagen_url = models.TextField(blank=True, null=True)

    def _str_(self):
        return f"{self.nombre} - ${self.precio}"


#eservaciones
class Reservacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    num_personas = models.IntegerField()
    estado = models.CharField(max_length=20, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)


#pedidos
class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo_entrega = models.CharField(max_length=20, choices=[('delivery', 'Delivery'), ('pickup', 'Pick-up')])
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estado = models.CharField(max_length=20, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)


#reseñas
class Resena(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)


#blog
class Blog(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    autor = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen_url = models.TextField(blank=True, null=True)


#fidelidad
class Fidelidad(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)
    fecha_actualizacion = models.DateTimeField(auto_now=True)


#eventos
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    imagen_url = models.TextField(blank=True, null=True)


#redes 
class RedSocial(models.Model):
    plataforma = models.CharField(max_length=50)
    url = models.TextField()


#contacto
class Contacto(models.Model):
    telefono = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.TextField()
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    mapa_url = models.TextField(blank=True, null=True)
    