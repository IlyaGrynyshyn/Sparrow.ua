# Generated by Django 4.0.4 on 2022-05-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_first_name_alter_user_last_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Користувачі', 'verbose_name_plural': 'Користувачі'},
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=38096065555, max_length=20, verbose_name='Phone number'),
            preserve_default=False,
        ),
    ]