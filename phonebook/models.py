from django.db import models
from django.db.models import Q
from phonenumber_field.modelfields import PhoneNumberField


class PhoneNumber(models.Model):
    phone_number = PhoneNumberField(null=False, blank=False, verbose_name='Номер телефона')
    PhoneTypes = (
        ('Рабочий', 'Рабочий'),
        ('Личный', 'Личный'),
        ('Факс', 'Факс'))
    phone_type = models.CharField(max_length=50, choices=PhoneTypes,
                                  verbose_name='Тип телефона')

    employee = models.ForeignKey('Employee', related_name='phone_numbers',
                                 on_delete=models.CASCADE, verbose_name='Сотрудник', blank=True, null=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['phone_number', 'employee'],
                                               condition=Q(phone_type='Личный'),
                                               name='unique employee')]
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Телефоные номера'

    def __str__(self):
        return f'{self.phone_type}: {self.phone_number}'


class Employee(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ФИО', blank=False, null=False)
    current_position = models.CharField(max_length=200, verbose_name='Должность', blank=False, null=False)
    organization = models.ForeignKey('Organization', related_name='employees',
                                     on_delete=models.SET_NULL, verbose_name='Организация', blank=True, null=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['full_name', 'organization'],
                                               name='unique follow')]
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __repr__(self):
        return f'{self.full_name} ({self.current_position})'

    def __str__(self):
        return f'{self.full_name} ({self.current_position})'


class Organization(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название', unique=True)
    address = models.CharField(max_length=200, verbose_name='Адрес')
    descriptions = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name
