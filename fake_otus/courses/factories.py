import factory
from factory import fuzzy

from courses.models import Course

TECHNOLOGIES = ('React', 'Vue', 'Django', 'HTML', 'Python', 'Flask', 'Tornado', 'Bottle', 'Zend', 'Symfony')
NAME_CHOICES = [f'{tech} для тупых' for tech in TECHNOLOGIES]


class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course
    title = fuzzy.FuzzyChoice(NAME_CHOICES)
    description = fuzzy.FuzzyText(length=256)

