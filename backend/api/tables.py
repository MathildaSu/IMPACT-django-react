import django_tables2 as tables
from .models import *
from django_tables2.utils import A  # alias for Accessor
from django.urls import reverse
from django.utils.html import format_html


class CommunityWorkerTable(tables.Table):
    # id = tables.LinkColumn("get_chw_by_id", args=[A("pk")])
    id = tables.Column(linkify=("viewCHW", (tables.A("id"),)))

    class Meta:
        model = CommunityWorker
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", "nombre", "appelido", "visit_id")

    # def render_id(self, record):
    #     return format_html(
    #         '<a href="person/{}">{}</a>',
    #         reverse("viewCHW", kwargs={"pk": str(record.id)}),
    #         record.id,
    #     )


class RowTable(tables.Table):
    name = tables.Column()
    value = tables.Column()

    class Meta:
        template = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-striped table-responsive"}
