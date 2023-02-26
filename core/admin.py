from django.contrib import admin

from core.models import Application, Colleges
admin.site.index_template = "pages/index.html"
class CollegeView(admin.ModelAdmin):
    list_display=['college_id','name','location']
    # list_filter=['location']
    list_per_page=10
    search_fields=['college_id','name','location']


class ApplicationView(admin.ModelAdmin):
    list_display=['name','email','whatsapp_number','college','linkedin','github','question','meal_type','tshirt_size','status']
    save_as = True
    save_on_top = True
# Register your models here.
admin.site.register(Colleges,CollegeView)
admin.site.register(Application,ApplicationView)