from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def shopurl(self):
        return reverse('prod_cat', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    img = models.ImageField(upload_to='product')
    desc = models.TextField()
    spec = models.TextField()
    stock = models.IntegerField()
    available = models.BooleanField()
    price = models.IntegerField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def shopurl(self):
        return reverse('prodetails', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)
    
    
# class products_extra(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_it_good=models.TextField()
    
# def _str_(self):
#     return self.user
    
