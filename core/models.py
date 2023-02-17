from django.db import models

class Discos(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True,null=True)
    imagen = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    precio = models.DecimalField(max_digits=5,decimal_places=2)
    autor = models.CharField(max_length=100)

    class Meta:
        db_table="Discos"
        verbose_name="Discos"
        verbose_name_plural="Discos"

    def __str__(self):
        return self.titulo


