from django.contrib import admin

from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Attribute)
class AttributeAdmin(admin.ModelAdmin):
    pass



@admin.register(models.AttributeKey)
class AttributeKeyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass



