# Generated by Django 3.2.7 on 2021-09-18 17:59

from django.conf import settings
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
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('dob', models.DateField(blank=True, null=True)),
                ('timezone', models.CharField(blank=True, max_length=255, null=True)),
                ('country_code', models.CharField(blank=True, max_length=10, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('terms_and_condition', models.BooleanField(default=False)),
                ('certify', models.BooleanField(default=False)),
                ('credits', models.PositiveIntegerField(default=0)),
                ('amount', models.FloatField(default=0.0)),
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
        migrations.CreateModel(
            name='CreditsSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('credits', models.PositiveIntegerField(verbose_name='Credits per dollar')),
            ],
            options={
                'verbose_name_plural': '3- Credits Per Dollar',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('error', models.TextField()),
            ],
            options={
                'verbose_name_plural': '4- Error while buying credits',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='PaymentInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=150)),
                ('bank_address', models.CharField(max_length=150)),
                ('account_number_or_iban', models.CharField(max_length=150)),
                ('beneficiary_name', models.CharField(max_length=150)),
                ('beneficiary_country', models.CharField(max_length=150)),
                ('beneficiary_address', models.CharField(max_length=500)),
                ('swift', models.CharField(max_length=150)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_payment_information', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '1- Bank Details',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='AmountPaid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('failed', 'Failed')], default='pending', max_length=20)),
                ('amount', models.FloatField(default=0.0, help_text='Payment in USD.')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='complete_payments', to='payment.paymentinformation')),
            ],
            options={
                'verbose_name_plural': '2- Requested/Paid Amounts',
                'ordering': ('-created',),
            },
        ),
    ]