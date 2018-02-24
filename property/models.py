from django.db import models

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Model(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return '{} ({})'.format(self.name, self.type)


class PropertyAddress(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200, default='Беларусь')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return ", ".join([self.address, self.city, self.country])


class Entity(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Юридическое лицо'
        verbose_name_plural = 'Юридические лица'

    def __str__(self):
        return self.name


class Department(models.Model):
    address = models.ForeignKey(PropertyAddress, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.address, self.entity)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.full_name, self.department)

    @property
    def full_name(self):
        return ' '.join([self.first_name, self.last_name])


class Equipment(models.Model):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    STATUSES = (
        (ACTIVE, 'Рабочее'),
        (INACTIVE, 'Нерабочее')
    )
    status = models.CharField(
        max_length=10,
        choices=STATUSES,
        default=ACTIVE,
    )
    name = models.CharField(max_length=200, verbose_name='Название')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, verbose_name='Модель')
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пользователь')
    serial_number = models.CharField(max_length=200, verbose_name='Серийный номер')
    receipt_date = models.DateField(verbose_name='Дата поступления')

    def __str__(self):
        return '{} ({})'.format(self.name, self.employee.full_name)


class Service(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200, default='Минск')
    country = models.CharField(max_length=200, default='Беларусь')
    phone = models.CharField(max_length=200)


class Repair(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date_of_transfer = models.DateField(verbose_name='Дата перемещения')
