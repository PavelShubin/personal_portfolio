# Generated by Django 4.1.3 on 2022-11-23 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0002_rename_title_project_titleman"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="titleman",
            new_name="title",
        ),
    ]
