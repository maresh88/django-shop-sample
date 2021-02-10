from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    LABEL_CHOICES = (
        ('N', 'new'),
        ('B', 'bestseller'),
        ('NON', 'not applicable')
    )

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    is_available = models.BooleanField(default=True)
    is_on_stock = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='created_products', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=5, default='N')

    class Meta:
        ordering = ('-created_at',)
        index_together = ('id', 'slug')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'pk': self.pk, 'slug': self.slug})


