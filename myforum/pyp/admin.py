from django.contrib import admin

# Register your models here.
from .models import Faculty,Module,ModuleYear,Answer,AnswerFile
admin.site.register(Faculty)
admin.site.register(Module)
admin.site.register(ModuleYear)
admin.site.register(AnswerFile)
admin.site.register(Answer)
