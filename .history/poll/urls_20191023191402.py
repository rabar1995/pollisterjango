from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router=SimpleRouter()

router.register('question', QuestionViewSet)
router.register('choice', ChoiceViewSet)

urlpatterns = router.urls