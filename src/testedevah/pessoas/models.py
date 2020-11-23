from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Pessoa(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=120, blank=False, null=True, default=None)
    data_nascimento = models.DateField(blank=False, null=True, default=None)
    cidade = models.CharField(max_length=30, blank=False, null=True, default=None)
    estado = models.CharField(max_length=2, blank=False, null=True, default=None)
    email = models.CharField(max_length=30, blank=False, null=True, default=None)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Pessoa.objects.create(user=instance)
    instance.pessoa.save()


