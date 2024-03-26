from django.db import models
from slugify import slugify
from hotel_user.models import User


HOTEL_STATUS = (
    ('Draft', 'Draft'),
    ('Disabled', 'Diasabled'),
    ('Rejected', 'Rejected'),
    ('In Revieew', 'Draft'),
    ("Live", "Live")

)


class Hotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='hotel_galley')
    address = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    status = models.CharField(max_length=20, choices=HOTEL_STATUS, default='Live')

    tags = models.CharField(max_length=40, help_texts="Seperate tags with comma")
    views = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(autho_now_add=True)
    price = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if self.slug == '' or self.slug == None:
            self.slug = slugify
        super().save()
