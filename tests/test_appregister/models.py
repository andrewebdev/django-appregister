from django.db import models
from appregister.base import Registry, AutoRegistry


class Question(models.Model):
    pass


class BooleanQuestion(Question):
    pass


class MultipleChoiceQuestion(Question):
    pass


# Setting up the registry.


class QuestionRegistry(Registry):

    base = Question
    discovermodule = 'questions'

registry = QuestionRegistry()
registry.register(BooleanQuestion)
registry.register(MultipleChoiceQuestion)


class AutoQuestion(object):
    pass


class AutoQuestionRegistry(AutoRegistry):

    base = 'test_appregister.models.AutoQuestion'
    discovermodule = 'autoquestions'

auto_registry = AutoQuestionRegistry()


class AutoQuestion(AutoQuestion, auto_registry.Mixin):
    pass
