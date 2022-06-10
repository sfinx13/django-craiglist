from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from authentification.models import User

TEST_IMAGE = """
iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX
///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASU
VORK5CYII=
""".strip()

class Category(models.Model):
    title = models.fields.CharField(max_length=255)
    slug = models.fields.SlugField()
    created_at = models.fields.DateTimeField(auto_now_add=True)
    updated_at = models.fields.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Advert(models.Model):
    title = models.fields.CharField(max_length=255)
    description = models.fields.TextField()
    slug = models.fields.SlugField(editable=False)
    price = models.fields.FloatField()
    zipcode = models.fields.IntegerField()
    picture = models.ImageField(null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    published_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ended_at = models.fields.DateTimeField(null=True)
    created_at = models.fields.DateTimeField(auto_now_add=True)
    updated_at = models.fields.DateTimeField(auto_now=True)

    def publish(self):
        self.created_at = timezone.now()
        self.slug = slugify(self.title, allow_unicode=True)
        self.save()
