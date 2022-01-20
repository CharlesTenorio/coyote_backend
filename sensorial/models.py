from django.db import models
from django.utils.translation import gettext_lazy as _


class Sensor(models.Model):
    identification = models.CharField(_("Identificação"), max_length=500)
    date = models.DateTimeField(_("Data"), auto_now=False, auto_now_add=False) # created_at ?
    shed = models.ForeignKey("app.Shed", verbose_name=_("Galpão"), on_delete=models.CASCADE)
    accommodation = models.ForeignKey("app.Accommodation", verbose_name=_("Alojamento"), on_delete=models.CASCADE)
    sector = models.ForeignKey("app.Sector", verbose_name=_("Setor"), on_delete=models.CASCADE)
    data = models.JSONField(_("Valor"))

    class Meta:
        verbose_name = _("Sensor")
        verbose_name_plural = _("Sensors")

    def __str__(self):
        return self.identification


class Temperature(models.Model):
    identification = models.CharField(_("Identificação"), max_length=500)
    date = models.DateTimeField(_("Data"), auto_now=False, auto_now_add=False) # created_at ?
    shed = models.ForeignKey("app.Shed", verbose_name=_("Galpão"), on_delete=models.CASCADE)
    accommodation = models.ForeignKey("app.Accommodation", verbose_name=_("Alojamento"), on_delete=models.CASCADE)
    sector = models.ForeignKey("app.Sector", verbose_name=_("Setor"), on_delete=models.CASCADE)
    value = models.DecimalField(_("Valor"), max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = _("Temperatura")
        verbose_name_plural = _("Temperaturas")

    def __str__(self):
        return self.identification

class Moisture(models.Model):
    identification = models.CharField(_("Identificação"), max_length=500)
    date = models.DateTimeField(_("Data"), auto_now=False, auto_now_add=False) # created_at ?
    shed = models.ForeignKey("app.Shed", verbose_name=_("Galpão"), on_delete=models.CASCADE)
    accommodation = models.ForeignKey("app.Accommodation", verbose_name=_("Alojamento"), on_delete=models.CASCADE)
    sector = models.ForeignKey("app.Sector", verbose_name=_("Setor"), on_delete=models.CASCADE)
    value = models.DecimalField(_("Valor"), max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = _("Umidade")
        verbose_name_plural = _("Umidades")

    def __str__(self):
        return self.identification