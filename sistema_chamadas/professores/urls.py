from rest_framework.routers import DefaultRouter
from .views import ProfessorViewSet

router = DefaultRouter()
router.register('', ProfessorViewSet)

urlpatterns = router.urls
