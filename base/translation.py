from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(NavigationItem)
class NavigationItemTranslationOptions(TranslationOptions):
    fields = ('title', 'address',)
    
    
@register(HomeHotel)
class HomeHotelTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Mission)
class MissionTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')

