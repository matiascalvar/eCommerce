# Generated by Django 3.2.4 on 2021-07-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20210704_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='categorias',
            new_name='categoria',
        ),
    ]
