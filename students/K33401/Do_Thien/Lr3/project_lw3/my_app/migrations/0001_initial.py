# Generated by Django 3.2.9 on 2021-12-03 01:00

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Middle name')),
                ('date_of_birth', models.DateField(verbose_name='Birthday')),
                ('address', models.CharField(default='VP 5/7', max_length=50, verbose_name='Address')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('phone', models.CharField(default='897777777', max_length=20, verbose_name='Phone number')),
                ('passport', models.CharField(default='C5555555', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Middle name')),
                ('date_of_birth', models.DateField(null=True, verbose_name='Birthday')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='Phone number')),
                ('address', models.CharField(max_length=50, null=True, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('e', 'empty'), ('f', 'full')], max_length=1, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=1, verbose_name='Type')),
                ('price', models.IntegerField(verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('floor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.floor')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='100', max_length=10, verbose_name='Room number')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone number')),
                ('floor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.floor')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.status')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.type')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('check_in', models.DateField(verbose_name='Check in')),
                ('check_out', models.DateField(verbose_name='Check out')),
                ('adults', models.SmallIntegerField()),
                ('children', models.SmallIntegerField(blank=True, null=True)),
                ('amount', models.IntegerField()),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.guest')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.room')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('tel', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone number')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
