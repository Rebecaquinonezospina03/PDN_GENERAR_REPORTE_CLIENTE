from django.db import models
from django.db.models import BooleanField, CharField

class Producto(models.Model):
    TIPO_PRODUCTO_CHOICES = [
        ('Elije', 'Elije'),
        ('camisa', 'Camisa'),
        ('pantalon', 'Pantalón'),
        ('vestido', 'Vestido')
    ]

    id = models.AutoField(primary_key=True)
    tipo_producto = models.CharField(max_length=20, choices=TIPO_PRODUCTO_CHOICES, default='Elije')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    existencias = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo_producto} - {self.descripcion}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_pedido = models.DateField(blank=True, null=True)
    tipo_producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, related_name='clientes')
    numero_de_pedido = models.ForeignKey('Pedido', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='pedidos')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} - {self.apellido} {self.nombre}'

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'),
                                                      ('completado', 'Completado')], default='pendiente')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)
    numero = models.PositiveIntegerField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.numero:
            ultimo_numero_pedido = Pedido.objects.filter(cliente=self.cliente).order_by('-numero').first()
            if ultimo_numero_pedido:
                self.numero = ultimo_numero_pedido.numero + 1
            else:
                self.numero = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.numero}'
