from django.urls import path

from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import CommunityWorkerListView

urlpatterns = [
    path("", views.home, name="home"),
    path("token/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", views.RegisterView.as_view(), name="auth_register"),
    path("test/", views.testEndPoint, name="test"),
    path("screenings/", views.getScreening),
    path("screening/create/", views.createScreening),
    path("screening/<str:pk>/update/", views.updateScreening),
    path("screening/<str:pk>/delete/", views.deleteScreening),
    path("screening/<str:pk>/", views.getScreening),
    path("visits/", views.getVisit),
    path("visit/create/", views.createVisit),
    path("visit/<str:pk>/update/", views.updateVisit),
    path("visit/<str:pk>/delete/", views.deleteVisit),
    path("visit/<str:pk>/", views.getVisit),
    path("studypartners/", views.getStudyPartner),
    path("studypartner/create/", views.createStudyPartner),
    path("studypartner/<str:pk>/update/", views.updateStudyPartner),
    path("studypartner/<str:pk>/delete/", views.deleteStudyPartner),
    path("studypartner/<str:pk>/", views.getStudyPartner),
    path("olderadults/", views.getOlderAdult),
    path("olderadult/create/", views.createOlderAdult),
    path("olderadult/<str:pk>/update/", views.updateOlderAdult),
    path("olderadult/<str:pk>/delete/", views.deleteOlderAdult),
    path("olderadult/<str:pk>/", views.getOlderAdult),
    path("communityworkers/", views.getCommunityWorker),
    path("communityworker/create/", views.createCommunityWorker),
    path("communityworker/<str:pk>/update/", views.updateCommunityWorker),
    path("communityworker/<str:pk>/delete/", views.deleteCommunityWorker),
    path("communityworker/<str:pk>/", views.getCommunityWorker),
    path("people/", CommunityWorkerListView.as_view(), name="viewCHWs"),
    path("person/<str:pk>/", views.get_chw_by_id, name="viewCHW"),
    path("create_chw/", views.create_chw, name="create_chw"),
    path("profile/<int:pk>/", views.profile, name="profile"),
]
