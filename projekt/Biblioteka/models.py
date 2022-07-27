from django.db      import models
from django.conf    import settings

# Create your models here.

class Book(models.Model):
    
    Cover = (
        ('Twarda', 'Twarda'),
        ('Miękka', 'Miękka'),
    )
    title = models.CharField(
        'Tytuł',
        max_length=200,
    )
    author = models.CharField(
        'Autor',
        max_length=200,
    )
    cover = models.CharField(
        'Okładka',
        max_length=30,
        choices=Cover,
        default='Miękka',
    )
    publisher = models.CharField(
        'Wydawnictwo',
        max_length=200,
    )
    premiere_date = models.DateField(
        'Data premiery',
    )
    pub_date = models.DateField(
        'Data publikacji',
        default=None,
    )
    number_of_pages = models.IntegerField(
        'Liczba stron',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
    photo = models.FileField(
        'Zdjęcie',
        upload_to='images',
        blank=True,
    )
    deleted = models.BooleanField(
        'Usunąć? ',
        default=False,
    )

    def __str__(self):
        return self.title

