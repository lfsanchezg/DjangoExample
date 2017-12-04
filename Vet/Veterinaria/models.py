from django.db import models
from django.urls import reverse_lazy

class Duegno(models.Model):
    class Meta:
        verbose_name = u'Dueño'
    first_name = models.CharField('Nombre', max_length=40)
    last_name = models.CharField('Apellido', max_length=40)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True, max_length=10)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def __unicode__(self):
        return self.first_name + " " + self.last_name

# TODO crear formulario público para crear mascotas
# TODO asignar URL de objeto para que al crearlo nos vayamos allá mismo
# TODO definir relación varios a uno de dueño a mascota
class Mascota(models.Model):

    class Meta:
        verbose_name = 'Mascota'

    name = models.CharField('Nombre', max_length=10)
    date_of_birth = models.DateField('Fecha de nacimiento')
    duegno = models.ForeignKey(Duegno, on_delete=models.CASCADE, null=True) # https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.ForeignKey.on_delete

    def get_absolute_url(self):
        return reverse_lazy('detail_pet', kwargs={'pk': self.id})

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name




