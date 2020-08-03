from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class DashboardConfig(AppConfig):
    name = 'dashboard'


class SuitConfig(DjangoSuitConfig):
    # layout = 'horizontal'
    layout = 'vertical'
