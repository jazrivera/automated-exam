from users.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ExamDetail(models.Model):
    exam_name = models.CharField(max_length=100)
    exam_subject = models.CharField(max_length=100)
    uploader = models.ForeignKey(
        User,
        verbose_name=('Uploader'),
        on_delete=models.CASCADE
    )
    date_uploaded = models.DateTimeField(
        _('Date Uploaded'),
        auto_now_add=True
    )
    exam_date = models.DateTimeField(
        _('Examination Date'),
        blank=True
    )
    exam_span = models.IntegerField(
        _(u"Examination Span Time"),
        default=15
    )

    def __str__(self):
        return "%s (%s)" % (
            self.exam_name,
            self.exam_subject
        )


class ExamQuestion(models.Model):
    ABC = 'abc'
    TRUE_FALSE = 'true_false'
    SHORT = 'short'
    ESSAY = 'essay'
    SOLUTION = 'solution'
    ANSWER_FORMAT_CHOICES = [
        (ABC, 'ABC'),
        (TRUE_FALSE, 'True or False'),
        (SHORT, 'Short Sentence'),
        (ESSAY, 'Essay/ Sentence'),
        (SOLUTION, 'Mathematical Solution')
    ]
    question = models.TextField()
    question_image = models.ImageField(
        upload_to='exams/',
        null=True,
        blank=True
    )
    answer_format = models.CharField(
        max_length=20,
        choices=ANSWER_FORMAT_CHOICES,
        default=ABC,
    )
    answer_choices = models.TextField(blank=True)
    answer = models.CharField(max_length=299)
    exam_detail = models.ForeignKey(
        ExamDetail,
        verbose_name=('Exam detail'),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.question


class ExamAnswer(models.Model):
    student = models.ForeignKey(
        User,
        verbose_name=('Student'),
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        ExamQuestion,
        verbose_name=('Exam detail'),
        on_delete=models.CASCADE
    )
    answer_image = models.ImageField(
        upload_to='answers/',
        null=True,
        blank=True
    )
    answer = models.CharField(max_length=299)

    def __str__(self):
        return "%s - %s" % (
            self.student,
            self.answer
        )