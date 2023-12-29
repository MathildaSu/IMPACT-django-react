from django.shortcuts import render, redirect
from rest_framework import status, generics
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.views.generic import ListView
from django_tables2 import SingleTableView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings


from .serializers import *
from .models import *
from .tables import *

import json


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            "Endpoint": "/notes/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of notes",
        },
        {
            "Endpoint": "/notes/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single note object",
        },
        {
            "Endpoint": "/notes/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "Creates new note with data sent in put request",
        },
        {
            "Endpoint": "/notes/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "Updates an existing note with data sent in post request",
        },
        {
            "Endpoint": "/notes/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "Deletes an existing note",
        },
        "/api/token/",
        "/api/register/",
        "/api/token/refresh/",
        "/api/test/",
    ]
    return Response(routes)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == "GET":
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({"response": data}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        try:
            body = request.body.decode("utf-8")
            data = json.loads(body)
            if "text" not in data:
                return Response("Invalid JSON data", status.HTTP_400_BAD_REQUEST)
            text = data.get("text")
            data = f"Congratulation your API just responded to POST request with text: {text}"
            return Response({"response": data}, status=status.HTTP_200_OK)
        except json.JSONDecodeError:
            return Response("Invalid JSON data", status.HTTP_400_BAD_REQUEST)
    return Response("Invalid JSON data", status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getOlderAdult(request):
    oa = OlderAdult.objects.all()
    serializer = OlderAdultSerializer(oa, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getOlderAdult(request, pk):
    oa = OlderAdult.objects.get(id=pk)
    serializer = OlderAdultSerializer(oa)
    return Response(serializer.data)


@api_view(["POST"])
def createOlderAdult(request):
    data = request.data
    oa = OlderAdult.objects.create(**data)
    serializer = OlderAdultSerializer(oa)
    return Response(serializer.data)


@api_view(["PUT"])
def updateOlderAdult(request, pk):
    oa = OlderAdult.objects.get(id=pk)
    serializer = OlderAdultSerializer(oa, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def deleteOlderAdult(request, pk):
    oa = OlderAdult.objects.get(id=pk)
    oa.delete()
    return Response(f"Note with id={pk} is deleted.")


@api_view(["GET"])
def getStudyPartner(request):
    sp = StudyPartner.objects.all()
    serializer = StudyPartnerSerializer(sp, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getStudyPartner(request, pk):
    sp = StudyPartner.objects.get(id=pk)
    serializer = StudyPartnerSerializer(sp)
    return Response(serializer.data)


@api_view(["POST"])
def createStudyPartner(request):
    data = request.data
    sp = StudyPartner.objects.create(**data)
    serializer = StudyPartnerSerializer(sp)
    return Response(serializer.data)


@api_view(["PUT"])
def updateStudyPartner(request, pk):
    sp = StudyPartner.objects.get(id=pk)
    serializer = StudyPartnerSerializer(sp, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def deleteStudyPartner(request, pk):
    sp = StudyPartner.objects.get(id=pk)
    sp.delete()
    return Response(f"Note with id={pk} is deleted.")


@api_view(["GET"])
def getCommunityWorker(request):
    cw = CommunityWorker.objects.all()
    serializer = CommunityWorkerSerializer(cw, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getCommunityWorker(request, pk):
    cw = CommunityWorker.objects.get(id=pk)
    serializer = CommunityWorkerSerializer(cw)
    return Response(serializer.data)


@api_view(["POST"])
def createCommunityWorker(request):
    data = request.data
    cw = CommunityWorker.objects.create(**data)
    serializer = CommunityWorkerSerializer(cw)
    return Response(serializer.data)


@api_view(["PUT"])
def updateCommunityWorker(request, pk):
    cw = CommunityWorker.objects.get(id=pk)
    serializer = CommunityWorkerSerializer(cw, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def deleteCommunityWorker(request, pk):
    cw = CommunityWorker.objects.get(id=pk)
    cw.delete()
    return Response(f"Note with id={pk} is deleted.")


@api_view(["GET"])
def getVisit(request):
    visit = Visit.objects.all()
    serializer = VisitSerializer(visit, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getVisit(request, pk):
    visit = Visit.objects.get(id=pk)
    serializer = VisitSerializer(visit)
    return Response(serializer.data)


@api_view(["POST"])
def createVisit(request):
    data = request.data
    visit = Visit.objects.create(**data)
    serializer = VisitSerializer(visit)
    return Response(serializer.data)


@api_view(["PUT"])
def updateVisit(request, pk):
    visit = Visit.objects.get(id=pk)
    serializer = VisitSerializer(visit, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def deleteVisit(request, pk):
    visit = Visit.objects.get(id=pk)
    visit.delete()
    return Response(f"Note with id={pk} is deleted.")


@api_view(["GET"])
def getScreening(request):
    screening = Screening.objects.all()
    serializer = ScreeningSerializer(screening, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getScreening(request, pk):
    screening = Screening.objects.get(id=pk)
    serializer = ScreeningSerializer(screening)
    return Response(serializer.data)


@api_view(["POST"])
def createScreening(request):
    data = request.data
    screening = Screening.objects.create(**data)
    serializer = ScreeningSerializer(screening)
    return Response(serializer.data)


@api_view(["PUT"])
def updateScreening(request, pk):
    screening = Screening.objects.get(id=pk)
    serializer = ScreeningSerializer(screening, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def deleteScreening(request, pk):
    screening = Screening.objects.get(id=pk)
    screening.delete()
    return Response(f"Note with id={pk} is deleted.")


class CommunityWorkerListView(SingleTableView):
    model = CommunityWorker
    table_class = CommunityWorkerTable
    template_name = "viewCHWs.html"


def home(request):
    # Get the current user object
    user = request.user
    if not user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    # show home
    return render(request, "home.html", {"user": user})


def create_chw(request):
    # Get the current user object
    # user = request.user
    # if not user.is_authenticated:
    #     return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    # # do form
    # if request.method == "POST":
    #     form = NotaForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("notas_list")
    # else:
    #     form = NotaForm()
    return render(request, "create_chw.html")


# Define a view that requires the user to be logged in
# @login_required
def profile(request, pk):
    # Get the current user object
    user = request.user
    if not user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    # Render a template with the user's information
    return render(request, "profile.html", {"user": user})


def get_chw_by_id(request, pk):
    cw = CommunityWorker.objects.get(id=pk)

    row_data = []
    serializer = CommunityWorkerSerializer(cw)
    for key in serializer.data.keys():
        row_data.append({"name": key, "value": serializer.data[key]})

    table = RowTable(row_data)
    return render(request, "viewCHW.html", {"table": table})
