# Generated by Django 3.0.5 on 2020-09-28 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('grade', models.CharField(choices=[('primary', 'Primary'), ('juniors', 'Junior Secondary'), ('seniors', 'Senior Secondary')], default='juniors', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('age', models.CharField(default=20, max_length=2)),
                ('dob', models.DateField()),
                ('disabilities', models.CharField(default='None', max_length=150)),
                ('nce', models.CharField(blank=True, default='None', max_length=100, verbose_name='College of Education')),
                ('bachelors', models.CharField(blank=True, default='None', max_length=200, verbose_name='Bachelors')),
                ('post_grad', models.CharField(blank=True, default='None', max_length=100, verbose_name='Post Graduate Studies')),
                ('masters', models.CharField(blank=True, default='None', max_length=200, verbose_name='Masters')),
                ('phd', models.CharField(blank=True, default='None', max_length=100, verbose_name='Doctor of Philosophy(PhD)')),
                ('government_id_type', models.CharField(choices=[('NIN', 'NIN'), ('PVC', 'Permanent Voters Card'), ('INTL', 'International Passport'), ('DRIV', "Drivers' License")], max_length=4)),
                ('government_id_number', models.PositiveIntegerField()),
                ('yrs_of_experience', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=500)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_account_number', models.PositiveIntegerField()),
                ('social_media_verification', models.BooleanField(default=False)),
                ('government_id_verification', models.BooleanField(default=False)),
                ('bank_verification', models.BooleanField(default=False)),
                ('slug', models.SlugField()),
                ('became_tutor_at', models.DateTimeField(auto_now_add=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='parents.ParentProfile')),
            ],
        ),
        migrations.CreateModel(
            name='TutoringPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medium', models.CharField(choices=[('online', 'Online Tutoring'), ('physical', 'Physical Tutoring'), ('both', 'Online and Physical Tutoring')], default='online', max_length=10)),
                ('locations', models.CharField(default='Any Location...', max_length=200)),
                ('rate_per_hour', models.PositiveIntegerField()),
                ('major', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='major', to='tutors.Expertise')),
                ('minor1', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='minor1', to='tutors.Expertise')),
                ('minor2', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='minor2', to='tutors.Expertise')),
                ('tutor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tutors.Tutor')),
            ],
        ),
    ]