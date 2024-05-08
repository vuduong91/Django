
from django.db import models

# Create your models here.
class Category(models.Model):
    nameCate = models.CharField(max_length=255)
    def __str__(self):
        return self.nameCate
class Product(models.Model):
    nameProduct = models.CharField(max_length=255)
    nameCate=models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.nameProduct

class ProductDetail(models.Model):
    nameProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    decripsion = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    cost = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product/')
    maxspeed = models.CharField(max_length=255)
    maxtouque = models.CharField(max_length=255)
    def __str__(self):
        return str(self.nameProduct) if self.nameProduct else''

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Shipping(models.Model):
    namePTT= models.CharField(max_length=255)

class Order(models.Model):
    sum = models.CharField(max_length=255)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    dateorder = models.DateTimeField(auto_now_add=True)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE)

class OrderDetail(models.Model):
    cost = models.IntegerField(default=11)
    quanity = models.IntegerField(default=11)
    product = models.ForeignKey(ProductDetail,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.product.id)











