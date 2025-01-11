from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(BlogCategory)
class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )
    
    
@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'category',)
    