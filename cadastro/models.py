from django.db import models
	
class Inscricao(models.Model):
        razao = models.CharField(max_length=100, verbose_name='Razao Social')
        fantasia = models.CharField(max_length=100, verbose_name='Nome Fantasia')
        endereco = models.CharField(max_length=100, verbose_name='Endereco')
        objetivo = models.CharField(max_length=100, verbose_name='Objetivo do Contrato')
        alvara = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Data do Alvara')

        class Meta:
                ordering = ['alvara']
                verbose_name = (u'razao')
                verbose_name_plural = (u'razoes')

        def __unicode__(self):
                return self.razao

