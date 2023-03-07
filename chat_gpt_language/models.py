from django.db import models
from django.contrib.auth.models import User


#Django model utils TimeStampedModel
class TimestampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class QuestionModel(TimestampedModel):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        help_text="User owning this question",
        null=True
    )    
    question = models.TextField()

    def __str__(self):
        return 'Question: %s.\n Created: %s' % (
            self.question, self.created
        )    

class AnswerModel(TimestampedModel):
    question_fk = models.OneToOneField(QuestionModel, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return 'Answer: %s.\n Created: %s.\n Question: %s' % (
            self.answer, self.created, self.question_fk.question
        )    
