from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_notsubcategory = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Blogs(models.Model):
    name = models.CharField(max_length=500, null=True)
    images = models.CharField(max_length=255, null=True, blank=True)
    linkvideo = models.CharField(max_length=255, null=True, blank=True)
    linkredirect = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    subcategory = models.ForeignKey(
        'SubCategory', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
