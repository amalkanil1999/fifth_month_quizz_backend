from django.contrib import admin


from django.contrib import admin
from quizz.models import Question, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

admin.site.register(Category,CategoryAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "question","category"]

admin.site.register(Question,QuestionAdmin)
