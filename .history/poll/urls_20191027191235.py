from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ChoiceViewSet,QuestionViewSet


router=SimpleRouter()

router.register('question', QuestionViewSet)
router.register('choice', ChoiceViewSet)
router.register('vote', ChoiceViewSet)

urlpatterns = router.urls