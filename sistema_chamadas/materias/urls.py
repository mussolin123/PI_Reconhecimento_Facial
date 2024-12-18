from rest_framework.routers import DefaultRouter
from .views import MateriaViewSet

router = DefaultRouter()
router.register('', MateriaViewSet)

urlpatterns = router.urls
