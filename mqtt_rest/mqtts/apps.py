from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MqttsConfig(AppConfig):
    name = "mqtt_rest.mqtts"
    verbose_name = _("MQTTs")
