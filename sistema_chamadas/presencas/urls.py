from rest_framework.routers import DefaultRouter
from .views import PresencaViewSet

router = DefaultRouter()
router.register('', PresencaViewSet)

urlpatterns = router.urls
