from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) # CharField is a field type
    pub_date = models.DateTimeField(default=timezone.now) # 'date published' is a human-readable name for the field

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # ForeignKey is a relationship
    choice_text = models.CharField(max_length=200) 
    votes = models.IntegerField(default=0) # IntegerField is a field type
    
    def __str__(self) -> str:
        return f"Question #{self.pk}" + self.choice_text

