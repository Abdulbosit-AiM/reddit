# Generated by Django 3.2 on 2022-02-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogcomment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='content',
            field=models.TextField(),
        ),
    ]
