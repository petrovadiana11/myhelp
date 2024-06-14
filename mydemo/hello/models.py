import uuid

from django.db import models

# Create your models here.
class Employee(models.Model):
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    fio = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.CharField(max_length=255, verbose_name="Должность")
    birthday = models.DateField(verbose_name="Дата рождения")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    address = models.CharField(max_length=255, verbose_name="Адрес")

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name_plural = "Сотрудники"

class Master(models.Model):
    guid = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    cost_per_hour = models.CharField(max_length=50, verbose_name="Стоимость часа работы")
    def __str__(self):
        return self.guid

    class Meta:
        verbose_name_plural = "Стоимость часа работы"

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=255, verbose_name="ФИО")
    birthday = models.DateField(verbose_name="Дата рождения")
    passport = models.CharField(max_length=50, verbose_name="Паспортные данные полностью")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Почта эл")

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name_plural = "Клиент"

class Car(models.Model):
    registration_number = models.CharField(max_length=50, primary_key=True)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    year_of_manufacture = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return self.model

    class Meta:
        verbose_name_plural = "Машины"

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    hours = models.CharField(max_length=20)
    order_date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Заказы"

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Услуги"

class OrderService(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return self.order

    class Meta:
        verbose_name_plural = "Услуги заказы"

class HistoryCost(models.Model):
    id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    old_cost = models.CharField(max_length=50)
    new_cost = models.CharField(max_length=50)
    change_date = models.DateField()

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Цены услуг"