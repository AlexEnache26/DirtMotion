from django.db import models
from django.db.models import CharField, Model, DO_NOTHING, DateField, DateTimeField, ForeignKey, IntegerField, TextField

class Item(Model):
    Name = CharField(max_length=30)
    Description = TextField()
    Price = IntegerField()
    Brand = ForeignKey('Brand', on_delete=DO_NOTHING)
    Type = ForeignKey('Type', on_delete=DO_NOTHING)
    Image = models.ImageField(upload_to='items/')
    Reviews = ForeignKey('Review', on_delete=DO_NOTHING)
    def __str__(self):
        return self.Name

class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.item.Name}"

class User(Model):
    FullName = CharField(max_length=50)
    Email = CharField(max_length=50)
    Phone = CharField(max_length=15)
    UserName = CharField(max_length=20)
    Password = CharField(max_length=20)
    ProfilePicture = CharField(max_length=200)

class Order(Model):
    User = ForeignKey('User', on_delete=DO_NOTHING)
    CreatedAt = DateTimeField()
    Status = ForeignKey('Status', on_delete = DO_NOTHING) #open, reject, in progress, completed
    IBAN = CharField(max_length=34)
    PaymentDate = DateField()
    Method = CharField(max_length=20)
    Quantity = IntegerField()
    Shipment = ForeignKey('Shipment', on_delete=DO_NOTHING)
    Item = ForeignKey('Item', on_delete=DO_NOTHING)

class Status(Model):
    Name = CharField(max_length=50)
    Type = CharField(max_length=50)

class Shipment(Model):
    TrackNumber = CharField(max_length=50)
    Product = CharField(max_length=100)
    Status = CharField(max_length=50) #open, in delivery, delivered, refused

class Review(models.Model):
    User = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)  # folosește Userul Django
    CreatedAt = models.DateTimeField(auto_now_add=True)
    Rating = models.IntegerField()
    Comment = models.TextField()
    def __str__(self):
        return f"{self.User} - {self.Rating}⭐"

class Brand(Model):
    Name = CharField(max_length=50)
    def __str__(self):
        return self.Name

class Type(Model):
    Name = CharField(max_length=50)
    def __str__(self):
        return self.Name