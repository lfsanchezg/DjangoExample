from django.db import models


# TODO crear formulario público para crear mascotas
# TODO asignar URL de objeto para que al crearlo nos vayamos allá mismo
# TODO definir relación varios a uno de dueño a mascota
class Mascota(models.Model):
    class Meta:
        verbose_name = 'Mascota'
    name = models.CharField('Nombre', max_length=10)
    date_of_birth = models.DateField('Fecha de nacimiento')
    def __str__(self):
        return "Mascota de nombre: " + self.name

    def __unicode__(self):
        return self.name


class Duegno(models.Model):
    class Meta:
        verbose_name = u'Dueño'
    name = models.CharField('Dueño', max_length=40)

