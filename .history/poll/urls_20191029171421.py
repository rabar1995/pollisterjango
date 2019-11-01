from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import ChoiceViewSet,QuestionViewSet,VoteViewSet


router=SimpleRouter()

router.register('question', QuestionViewSet)
router.register('choice', ChoiceViewSet)
router.register('vote', VoteViewSet)

urlpaterns = [
     path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt'))
]

urlpatterns += router.urls