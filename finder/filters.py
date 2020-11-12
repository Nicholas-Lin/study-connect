import django_filters

from groups.models import Group
from users.models import Profile

class ProfileFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = ''

