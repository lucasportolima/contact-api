from django.db import models


class VarejaoContact(models.Model):
    nome = models.CharField(max_length=100, null=False)
    celular = models.CharField(max_length=13, null=False)

    class Meta:
        managed = True
        db_table = 'contacts'
        verbose_name = 'Contato Varejão'
        verbose_name_plural = 'Contatos Varejão'
        unique_together = ['nome', 'celular']
        ordering = ['nome']
        get_latest_by = ['pk']

    def __str__(self) -> str:
        return self.nome
