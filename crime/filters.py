import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class LogFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_posted", lookup_expr='gte')
    # end_date = DateFilter(field_name="date_posted", lookup_expr='lte')
    case = CharFilter(field_name='case', lookup_expr='icontains')
    class Meta:
        model = Log
        fields = ['case', 'location', 'date_posted', 'status', 'type']
        # exclude = ['date_posted']
