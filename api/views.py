from .serializers import ExamSerializer
from .serializers import ExamAnswerSerializer
from .serializers import RegisterSerializer
from .serializers import UserSerializer
from django.shortcuts import render
from exam.models import ExamAnswer
from exam.models import ExamDetail
from exam.models import ExamQuestion
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
from users.models import User
from users.models import User


class UserListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegisterView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(
            data=request.data,
        )

        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            user = User.objects.create(
                email=data.get('email'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                is_prof=data.get('is_prof'),
                avatar=data.get('avatar'),
            )
            user.set_password(data.get('password'))
            user.is_active = False
            user.save()
            print('qweqweqweqwe')
            # user_method = UserMethods.objects.get(
            #     username=user.username
            # )

            # site = get_current_site(request).domain
            # user_method.send_activation_email(user.email, site)
            return Response(UserSerializer(data).data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ExamApiView(generics.ListAPIView):
    queryset = ExamDetail.objects.all()
    serializer_class = ExamSerializer


class ExamAnswerApiView(generics.ListAPIView):
    queryset = ExamAnswer.objects.all()
    serializer_class = ExamAnswerSerializer
