# Generated by Django 4.2.13 on 2024-07-03 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, choices=[('USA', 'Estados Unidos'), ('BRA', 'Brasil'), ('FRA', 'França'), ('COL', 'Colombia')], max_length=20, null=True)),
            ],
        ),
    ]
