# Generated by Django 3.2.7 on 2021-09-05 19:39

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('current_position', models.CharField(max_length=200, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('descriptions', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер телефона')),
                ('phone_type', models.CharField(choices=[('Рабочий', 'Рабочий'), ('Личный', 'Личный'), ('Факс', 'Факс')], max_length=50, verbose_name='Тип телефона')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone_numbers', to='phonebook.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Номер телефона',
                'verbose_name_plural': 'Телефоные номера',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='phonebook.organization', verbose_name='Организация'),
        ),
        migrations.AddConstraint(
            model_name='phonenumber',
            constraint=models.UniqueConstraint(condition=models.Q(('phone_type', 'Личный')), fields=('phone_number', 'employee'), name='unique employee'),
        ),
        migrations.AddConstraint(
            model_name='employee',
            constraint=models.UniqueConstraint(fields=('full_name', 'organization'), name='unique follow'),
        ),
    ]