from django_filters import rest_framework as django_filters
from core.models import Program


class ProgramFilter(django_filters.FilterSet):
    age = django_filters.NumberFilter(method='filter_by_age')
    country = django_filters.CharFilter(lookup_expr='icontains')
    format = django_filters.ChoiceFilter(choices=Program.FORMAT_CHOICES)
    gender = django_filters.ChoiceFilter(choices=Program.GENDER_CHOICES)
    major = django_filters.NumberFilter(field_name='major__id')

    def filter_by_age(self, queryset, name, value):
        return queryset.filter(start_age__lt=value, end_age__gte=value)

    class Meta:
        model = Program
        fields = ['age', 'country', 'format', 'gender', 'major']
