from django.contrib import admin
from .models import Divisions, Districts, Chondokotha, Category


class DivisionModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", "details"]

    class Meta:
        Model = Divisions


admin.site.register(Divisions, DivisionModel)


class DistrictModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", "details"]

    class Meta:
        Model = Districts


admin.site.register(Districts, DistrictModel)


class ChondokothaAdmin(admin.ModelAdmin):
    list_display = ['title', 'districts', 'category', 'category_name', 'disticts_name', 'division_name']
    search_fields = ["__str__", "details"]

    class Meta:
        Model = Chondokotha


admin.site.register(Chondokotha, ChondokothaAdmin)


class CategoryModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", "details"]

    class Meta:
        Model = Category


admin.site.register(Category, CategoryModel)
# Register your models here.
