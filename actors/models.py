from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRA', 'Brasil'),
    ('FRA', 'França'),
    ('COL', 'Colombia'),


)
class Actor(models.Model):
    name = models.CharField(max_length=30)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=20,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name