# Generated by Django 3.2.6 on 2022-04-04 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestion", "0012_alter_glossary_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="inforesource",
            options={"ordering": ("name",)},
        ),
        migrations.RenameField(
            model_name="inforesource",
            old_name="resource",
            new_name="description",
        ),
        migrations.AddField(
            model_name="inforesource",
            name="name",
            field=models.CharField(
                default=" ",
                help_text="Nombre para este recurso de información.",
                max_length=100,
            ),
            preserve_default=False,
        ),
    ]
