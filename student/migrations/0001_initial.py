# Generated by Django 3.1.7 on 2021-07-21 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(max_length=15, unique=True)),
                ('dob', models.DateField()),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrator.department')),
            ],
        ),
        migrations.CreateModel(
            name='CourseRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(null=True)),
                ('first_test', models.FloatField(default=0)),
                ('second_test', models.FloatField(default=0)),
                ('exam', models.FloatField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.course')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
