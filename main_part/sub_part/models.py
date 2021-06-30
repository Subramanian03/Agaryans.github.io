from django.db import models

# Create your models here.
class reg(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    psw=models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class contacts(models.Model):
    full_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    email_id=models.CharField(max_length=100)
    message=models.CharField(max_length=300)

    def __str__(self):
        return self.full_name

class adminreg(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    psw=models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class equipment(models.Model):
    name=models.CharField(max_length=100)
    equipment=models.CharField(max_length=1000)
    description=models.CharField(max_length=1000)
    category=models.CharField(max_length=100)
    count=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class package(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    count=models.CharField(max_length=100)
    product=models.CharField(max_length=100)
    items=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class category(models.Model):
    name=models.CharField(max_length=1000)
    categories=models.CharField(max_length=100)
    count=models.CharField(max_length=1000)

    def __str__(self):
        return self.categories

class users(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    activation=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class reservation(models.Model):
    name=models.CharField(max_length=100)
    payment=models.CharField(max_length=100)
    price=models.CharField(max_length=1000)
    security=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    count=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class invoice(models.Model):
    name=models.CharField(max_length=100)
    product=models.CharField(max_length=1000)
    payment=models.CharField(max_length=1000)
    count=models.CharField(max_length=1000)
    status=models.CharField(max_length=1000)
    category=models.CharField(max_length=1000)
    price=models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    