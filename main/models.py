from django.db import models

class Services(models.Model):
    caption = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    icon = models.ImageField()
    picture = models.ImageField()
    title = models.CharField(max_length=255)
    body = models.TextField()

    class Meta():
        verbose_name_plural = "Xizmatlar"
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=13)
    message = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta():
        verbose_name_plural = "Murojaatlar"
    
    def __str__(self):
        return self.name

class Technicians(models.Model):
    picture = models.ImageField()
    name = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name_plural = "Texnik xodimlar"

class Comments(models.Model):
    picture = models.ImageField()
    name = models.CharField(max_length=255)
    body = models.TextField()
    profession = models.CharField(max_length=255)

    def __str__(self):
        return f"Murojaat {self.name} dan"
    
    class Meta():
        verbose_name_plural = "Fikrlar"
        ordering = ("-id",)

class Booking(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    date = models.DateField(auto_now_add=True)
    message = models.TextField()
    select = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
