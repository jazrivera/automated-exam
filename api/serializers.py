from exam.models import ExamAnswer
from exam.models import ExamDetail
from exam.models import ExamQuestion
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        allow_blank=False,
        allow_null=False,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_prof',
            'avatar',
        ]


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        allow_blank=False,
        allow_null=False,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    password = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
    )

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'first_name',
            'last_name',
            'is_prof',
            'avatar',
        ]


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'first_name',
            'last_name',
        ]


class ExamAnswerSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=False)
    class Meta:
        model = ExamAnswer
        fields = [
            'student',
            'question',
            'answer_image',
            'answer',
        ]


class ExamQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamQuestion
        fields = [
            'question',
            'question_image',
            'answer_format',
            'answer_choices',
            # 'answer', this will show the correct answer
            'exam_detail',
        ]


class ExamSerializer(serializers.ModelSerializer):
    examquestion_set = ExamQuestionSerializer(many=True)
    class Meta:
        model = ExamDetail
        fields = [
            'exam_name',
            'exam_subject',
            'exam_date',
            'exam_span',
            'examquestion_set'
        ]


