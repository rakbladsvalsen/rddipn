from colorfield.fields import ColorField
from django.db import models
from tinymce.models import HTMLField


class BaseUnit(models.Model):
    """
    Base class with common attributes.
    """

    class Meta:
        abstract = True

    name = models.CharField(
        max_length=100,
        help_text="Nombre de la unidad.",
        verbose_name="Nombre de la unidad",
    )
    order = models.PositiveIntegerField(
        unique=True,
        help_text="Índice de la unidad (usado para ordenar cada unidad).",
        verbose_name="Índice",
    )


class Unit(BaseUnit):
    class Meta:
        ordering = ("order",)

    goal = models.CharField(
        max_length=200,
        default="Ejemplo",
        help_text="Objetivo de la materia.",
        verbose_name="Objetivo",
    )

    header_color = ColorField(
        default="#000000", help_text="Color de la barra principal."
    )

    assessment_html = models.TextField(
        help_text="HTML para la sección de evaluación.",
        max_length=1000,
        null=True,
        blank=True,
    )

    assessment_resource = models.TextField(
        help_text="HTML para la sección de evaluación (recurso).",
        max_length=1000,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class SubUnit(BaseUnit):
    class Meta:
        ordering = ("order",)

    parent = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name="SubUnit",
        help_text="Sección padre de esta subunidad.",
        verbose_name="Sección padre",
    )
    contents = HTMLField(help_text="Contenidos de esta subunidad.")

    keywords = models.TextField(
        max_length=1000, help_text="Palabras clave (opcionales).", blank=True, null=True
    )

    order_as_str = models.CharField(
        max_length=10,
        unique=True,
        help_text="Índice a mostrar en el sitio (Ej: 1.2.3).",
        verbose_name="Índice (temario)",
    )

    def __str__(self):
        return f"{self.order_as_str}: {self.name}"


class UnitResource(BaseUnit):
    class Meta:
        ordering = ("order",)

    parent = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name="ResourceUnit",
        help_text="Sección padre de este recurso.",
        verbose_name="Sección padre",
    )

    contents = models.TextField(
        help_text="Contenidos (HTML) para este recurso.", max_length=1000
    )

    subtitle = models.TextField(
        max_length=1000, help_text="Subtítulo, opcional.", blank=True, null=True
    )

    order_as_str = models.CharField(
        max_length=10,
        unique=True,
        help_text="Índice a mostrar en el sitio (Ej: 1.2.3).",
        verbose_name="Índice (temario)",
    )

    def __str__(self):
        return f"{self.order_as_str}: {self.name}"


class Glossary(models.Model):
    class Meta:
        ordering = ("term",)
        verbose_name_plural = "Glossary terms"

    # parent = models.ForeignKey(
    #     Unit,
    #     on_delete=models.CASCADE,
    #     help_text="Sección padre de este término.",
    #     verbose_name="Sección padre",
    # )

    term = models.CharField(help_text="Término.", max_length=100)

    description = HTMLField(
        help_text="Descripción de este término.",
    )


class InfoResource(models.Model):
    # This kind of 'resource' is different from the other one - UnitResource.
    # This model will contain mostly links, APA or IEEE references, not videos,
    # or embeddable content.
    class Meta:
        ordering = ("name",)

    # parent = models.ForeignKey(
    #     Unit,
    #     on_delete=models.CASCADE,
    #     help_text="Sección padre de este recurso de información.",
    #     verbose_name="Sección padre",
    # )

    name = models.CharField(
        help_text="Nombre para este recurso de información.", max_length=100
    )

    description = models.TextField(
        help_text="Referencia a este recurso de información.", max_length=300
    )
