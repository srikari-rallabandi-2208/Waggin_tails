# Generated by Django 3.2.8 on 2021-10-23 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_first_name', models.CharField(max_length=200, null=True)),
                ('v_last_name', models.CharField(max_length=200, null=True)),
                ('v_gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=20, null=True)),
                ('v_age', models.IntegerField(max_length=3, null=True)),
                ('v_phone', models.CharField(max_length=200, null=True)),
                ('v_email', models.CharField(max_length=200, null=True)),
                ('v_aadhaar', models.IntegerField(max_length=12, null=True)),
                ('v_address', models.CharField(max_length=500, null=True)),
                ('v_city', models.CharField(max_length=100, null=True)),
                ('v_state', models.CharField(choices=[('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhattisgarh', 'Chhattisgarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadweep', 'Lakshadweep'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Orissa', 'Orissa'), ('Pondicherry', 'Pondicherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Tripura', 'Tripura'), ('Uttaranchal', 'Uttaranchal'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal')], max_length=100, null=True)),
                ('v_postal_code', models.IntegerField(max_length=6, null=True)),
                ('v_day_pref', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=10, null=True)),
                ('v_time_pref', models.CharField(choices=[('4a.m. - 5a.m.', '4a.m. - 5a.m.'), ('5a.m. - 6a.m.', '5a.m. - 6a.m.'), ('6a.m. - 7a.m.', '6a.m. - 7a.m.'), ('7p.m. - 8p.m.', '7p.m. - 8p.m.'), ('8p.m. - 9p.m.', '8p.m. - 9p.m.'), ('9p.m. - 10p.m.', '9p.m. - 10p.m.')], max_length=20, null=True)),
                ('v_profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('v_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_first_name', models.CharField(max_length=200, null=True)),
                ('o_last_name', models.CharField(max_length=200, null=True)),
                ('o_phone', models.IntegerField(max_length=10, null=True)),
                ('o_email', models.CharField(max_length=200, null=True)),
                ('o_address', models.CharField(max_length=500, null=True)),
                ('o_city', models.CharField(max_length=100, null=True)),
                ('o_state', models.CharField(max_length=100, null=True)),
                ('o_postal_code', models.IntegerField(max_length=6, null=True)),
                ('o_about_me', models.CharField(max_length=1000, null=True)),
                ('o_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog_name', models.CharField(max_length=100, null=True)),
                ('dog_breed', models.CharField(max_length=100, null=True)),
                ('dog_age', models.IntegerField(blank=True, null=True)),
                ('dog_gender', models.CharField(max_length=100, null=True)),
                ('dog_city', models.CharField(max_length=100)),
                ('dog_state', models.CharField(max_length=100)),
                ('dog_pfp', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
