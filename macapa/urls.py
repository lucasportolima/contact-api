from rest_framework.routers import SimpleRouter

from .views import MacapaContactViewSet

app_name = 'macapa'

router = SimpleRouter()
router.register('macapa', MacapaContactViewSet, 'macapa_contact')
