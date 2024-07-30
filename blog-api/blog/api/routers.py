from rest_framework.routers import DefaultRouter

from .views import PostViewSet, NoteViewSet

router = DefaultRouter()

router.register(r'post', PostViewSet,basename='post')
router.register(r'note', NoteViewSet,basename='note')

urlpatterns = router.urls