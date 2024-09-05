from django.contrib import admin
from .models import Flower, FlowerCategory
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('flower_name', 'price', 'stock')
    search_fields = ('flower_name',)
    list_filter = ('category',)
    filter_horizontal = ('category',)
    
admin.site.register(Flower,FlowerAdmin)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    
admin.site.register(FlowerCategory,CategoryAdmin)




# Lilies
# Sunflowers
# Tulips
# Orchids
# Daisies
# Hydrangeas
# Mixed Flowers