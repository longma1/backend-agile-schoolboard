import uuid

from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from core.models import StudentProfile
from core.models.board import Board
from core.serializer.board_serializer import BoardSerializer


# noinspection PyMethodMayBeStatic

class BoardController(APIView):
    def get(self, request):
        student_profile = StudentProfile.objects.filter(user=request.user).first()
        boards = Board.objects.filter(owner=student_profile)
        serializer = BoardSerializer(boards, many=True)

        return JsonResponse({'result': serializer.data})

    def post(self, request):
        student_profile = StudentProfile.objects.filter(user=request.user).first()
        if student_profile:
            serializer = BoardSerializer(data=request.data, context={'student_profile': student_profile})
            if serializer.is_valid():
                board = serializer.create(serializer.validated_data)

                serializer = BoardSerializer(board, many=False)
                return JsonResponse({'result': serializer.data})

        return HttpResponse(status=400)
