from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet

router = DefaultRouter()
router.register('', AlunoViewSet)

urlpatterns = router.urls
