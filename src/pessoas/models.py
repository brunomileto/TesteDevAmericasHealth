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
    cpf = models.CharField(max_length=120, blank=False, null=True, unique=True, default=None)
    data_nascimento = models.DateField(blank=False, null=True, default=None)
    cidade = models.CharField(max_length=30, blank=True)
    estado = models.CharField(max_length=2, blank=True, )


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Pessoa.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

