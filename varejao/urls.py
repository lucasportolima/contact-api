from rest_framework.routers import SimpleRouter

from .views import VarejaoContactViewSet

app_name = 'varejao'

router = SimpleRouter()
router.register('varejao', VarejaoContactViewSet, 'varejao_contact')
