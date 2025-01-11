from django.contrib import admin
from .models import RoomCategory, Room, RoomImage, RoomSupply, RoomFeature
from modeltranslation.admin import TranslationAdmin

@admin.register(RoomCategory)
class RoomCategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug',)
    
    group_fieldsets = True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    
    
class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1
    
    
class RoomSupplyInline(admin.TabularInline):
    model = RoomSupply
    extra = 1
    
class RoomFeatureInline(admin.TabularInline):
    model = RoomFeature
    extra = 1

@admin.register(Room)
class RoomAdmin(TranslationAdmin):
    list_display = ('name', 'number', 'category', 'price', 'is_active',)
    list_filter = ('category', 'is_active',)
    inlines = [RoomImageInline, RoomSupplyInline, RoomFeatureInline]
    
    group_fieldsets = True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }