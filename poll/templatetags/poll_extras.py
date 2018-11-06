from django import template
from poll.models import Question

register = template.Library()

def upper(value):
    """Converts a string into all uppercase"""
    return value.upper()

register.filter('upper' , upper)


@register.simple_tag
def recent_polls(n=5, **kwargs):
    """Return recent n polls"""
    name = kwargs.get("name", "Arguments is not passed")
    print(name)
    questions = Question.objects.all().order_by("-created_at")
    return questions[0:n]

#23