from django.shortcuts import render
from rest_framework.views import APIView
from .models import Question, Answer
from .serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class QuestionList(APIView):
    def get(self, request):
        qusetions = Question.objects.all()
        print(qusetions)
        serializer = QuestionSerializer(qusetions, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
