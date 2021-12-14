from django.contrib import admin
from .models import Banner,Category,Brand,Color, ProductAttribute,Size,Organization,Product

admin.site.register(Banner)
# admin.site.register(Category)
admin.site.register(Brand)
# admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Organization)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Category,CategoryAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('title','color_bg')
admin.site.register(Color,ColorAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','brand','organization','color','size','status','is_featured')
    list_edtable = ('status','is_featured')
admin.site.register(Product)


#product attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','product','price','color','size')
admin.site.register(ProductAttribute,ProductAttributeAdmin)


