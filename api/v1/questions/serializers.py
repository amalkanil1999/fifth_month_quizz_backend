from rest_framework.serializers import ModelSerializer
from quizz.models import Question


class QuestionSerializer(ModelSerializer):
    class Meta:
        model=Question
        fields=("question","choice_1","choice_2","choice_3","choice_4","hint","id")
