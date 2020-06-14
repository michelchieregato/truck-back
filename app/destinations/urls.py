from rest_framework import routers
from destinations.views import DestinationViewSet

app_name = 'destinations'

router = routers.SimpleRouter()
router.register(r'', DestinationViewSet)

urlpatterns = router.urls