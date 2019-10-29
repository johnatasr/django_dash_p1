from django.db import models

# Create your models here.

class Chips(models.Model):
    CATEGORIA_OPE = (
        ('Oi', 'OI'),
        ('Tim', 'Tim'),
        ('Claro', 'Claro'),
        ('Vivo', 'Vivo'),

    )
    CATEGORIA_PLANO = (
        ('Plano A', 'Plano A'),
        ('Plano B', 'Plano B'),
        ('Plano C', 'Plano C'),
        ('Plano D', 'Plano D'),
    )

    operadora = models.CharField('Operadora', max_length=20, blank=False, null=False, choices=CATEGORIA_OPE)
    plano = models.CharField('Plano', max_length=20, blank=False, null=False, choices=CATEGORIA_PLANO)

    def __str__(self):
        return self.operadora
