from django.contrib import admin
from . models import mymodel
# Register your models here.

class testModelAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','salary')
    


admin.site.register(mymodel,testModelAdmin)