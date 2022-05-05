# Generated by Django 3.2.6 on 2022-04-29 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestion", "0013_auto_20220404_0417"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="glossary",
            name="parent",
        ),
        migrations.RemoveField(
            model_name="inforesource",
            name="parent",
        ),
        migrations.AddField(
            model_name="unit",
            name="assessment_html",
            field=models.TextField(
                blank=True,
                help_text="HTML para la sección de evaluación.",
                max_length=1000,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="unit",
            name="assessment_resource",
            field=models.TextField(
                blank=True,
                help_text="HTML para la sección de evaluación (recurso).",
                max_length=1000,
                null=True,
            ),
        ),
    ]
