from django.urls import path

from .apiviews import IdeaViewSet, CreateVote, UserCreate, LoginView

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("idea", IdeaViewSet, base_name="idea")


urlpatterns = [
    path("login/", LoginView.as_view(), name="user_login"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path(
        "idea/<int:pk>/vote/",
        CreateVote.as_view(),
        name="vote_create",
    ),
]


urlpatterns += router.urls