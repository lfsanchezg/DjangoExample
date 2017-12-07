from django.db import models
from django.urls import reverse_lazy
from django.core.validators import validate_email
from .validators import validate_chilean_cellphone


class Duegno(models.Model):
    class Meta:
        verbose_name = u'Dueño'
    first_name = models.CharField('Nombre', max_length=40)
    last_name = models.CharField('Apellido', max_length=40)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True, validators=[validate_email])
    phone = models.CharField(null=True, blank=True, max_length=12, validators=[validate_chilean_cellphone])

    def __str__(self):
        return self.first_name + " " + self.last_name

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse_lazy('duegno_detail', kwargs={'duegno_id': self.id})

class Mascota(models.Model):

    class Meta:
        verbose_name = 'Mascota'

    name = models.CharField('Nombre', max_length=10)
    date_of_birth = models.DateField('Fecha de nacimiento')
    duegno = models.ForeignKey(Duegno, on_delete=models.CASCADE, null=True) # https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.ForeignKey.on_delete
    created_by = models.CharField('Creador', max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('detail_pet', kwargs={'pk': self.id})

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name




