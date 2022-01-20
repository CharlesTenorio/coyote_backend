from django.db import models
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(_("Nome"), max_length=500)
    brand = models.ImageField(_("Logo"), upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")

    def __str__(self):
        return self.name


class Shed(models.Model):
    company = models.ForeignKey("app.Company", verbose_name=_("Empresa"), on_delete=models.CASCADE)
    identification = models.CharField(_("Identificação"), max_length=500)
    
    class Meta:
        verbose_name = _("Galpão")
        verbose_name_plural = _("Galpões")

    def __str__(self):
        return self.identification


class Accommodation(models.Model):
    shed = models.ForeignKey("app.Shed", verbose_name=_("Galpão"), on_delete=models.CASCADE)
    identification = models.CharField(_("Identificação"), max_length=500)

    class Meta:
        verbose_name = _("Alojamento")
        verbose_name_plural = _("Alojamentos")

    def __str__(self):
        return self.identification


class Sector(models.Model):
    accommodation = models.ForeignKey("app.Accommodation", verbose_name=_("Alojamento"), on_delete=models.CASCADE)
    identification = models.CharField(_("Identificação"), max_length=500)
    
    class Meta:
        verbose_name = _("Setor")
        verbose_name_plural = _("Setores")

    def __str__(self):
        return self.identification
