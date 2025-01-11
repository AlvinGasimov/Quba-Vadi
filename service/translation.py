from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', )
    