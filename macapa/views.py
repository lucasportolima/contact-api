from rest_framework import viewsets, filters
from django.conf import settings

from core.permissions import HasPermission
from core.views import AuthModelMixedIn

from .serializers import MacapaContactSerializer
from .models import MacapaContact


class MacapaContactViewSet(viewsets.ModelViewSet, AuthModelMixedIn):
    """ API to return Macapa classes """

    queryset = MacapaContact.objects.all()
    serializer_class = MacapaContactSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'celular']

    def get_permissions(self):
        """
            Override of the get_permissions method,
            custom permissions
        """

        # Default for 'destroy'
        permission_classes = [
            settings.USER_GROUPS['ADMINISTRATOR'],
        ]

        if self.action != 'destroy':
            permission_classes.append(settings.USER_GROUPS['OPERATOR'])

        return [HasPermission(permission_classes)]
