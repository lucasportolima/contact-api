from django.db import models


class MacapaContact(models.Model):
    nome = models.CharField(max_length=200, null=False)
    celular = models.CharField(max_length=20, null=False)

    class Meta:
        managed = True
        db_table = 'contacts'
        verbose_name = 'Contato Macapa'
        verbose_name_plural = 'Contatos Macapa'
        unique_together = ['nome', 'celular']
        ordering = ['nome']
        get_latest_by = ['pk']

    def __str__(self) -> str:
        return self.nome

    def save(self, *args, **kwargs):
        """Processing data before saving the contact"""

        self.nome = self.nome.upper()
        if len(self.celular) == 13:
            self.celular = f"+{self.celular[0:2]} " \
                           f"({self.celular[2:4]}) " \
                           f"{self.celular[4:9]}-" \
                           f"{self.celular[9:13]}"
        super().save(*args, **kwargs)
