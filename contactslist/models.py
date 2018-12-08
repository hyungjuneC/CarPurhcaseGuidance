from django.db import models

class User(models.Model):
    u_id = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    e_mail = models.EmailField(max_length=20)
    phone_number = models.CharField(max_length=20)

    def publish(self):
        self.save()

    def __str__(self):
        return self.u_id
class Category(models.Model):
    Category_Name= models.CharField(max_length=10)
class Company(models.Model):
    Company = models.CharField(max_length=20)
    Country = models.CharField(max_length=20)
class Carinfo(models.Model):
    car_name = models.CharField(max_length=20)
    car_fuel = models.CharField(max_length=20)
    car_Auto = models.CharField(max_length=20)
    car_Cate =models.ForeignKey(Category, on_delete=models.CASCADE)
    car_Image = models.CharField(max_length=255)
    car_Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    car_Country = models.CharField(max_length=20)





class UsersPick(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    c_id = models.ForeignKey(Carinfo, on_delete=models.CASCADE)
