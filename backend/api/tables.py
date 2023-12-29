import django_tables2 as tables
from .models import *


class CommunityWorkerTable(tables.Table):
    class Meta:
        model = CommunityWorker
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", "nombre", "appelido", "visit_id")


class RowTable(tables.Table):
    name = tables.Column()
    value = tables.Column()

    class Meta:
        template = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-striped table-responsive"}
