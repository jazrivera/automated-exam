from django.contrib import admin
from .models import ExamDetail
from .models import ExamQuestion
from .models import ExamAnswer


admin.site.register(ExamDetail)
admin.site.register(ExamQuestion)
admin.site.register(ExamAnswer)
