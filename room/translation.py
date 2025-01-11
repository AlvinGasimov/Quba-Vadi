from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(RoomCategory)
class RoomCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )
    
    
@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('category', 'name', 'description', 'bed_position',)
    
    
@register(RoomSupply)
class RoomSupplyTranslationOptions(TranslationOptions):
    fields = ('name',)
    
    
@register(RoomFeature)
class RoomFeatureTranslationOptions(TranslationOptions):
    fields = ('name',)
