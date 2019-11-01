from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ChoiceViewSet,QuestionViewSet,VoteViewSet


router=SimpleRouter()

router.register('question', QuestionViewSet)
router.register('choice', ChoiceViewSet)
router.register('vote', VoteViewSet)

urlpatterns = router.urls