from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.html import mark_safe 

#Banner
class Banner(models.Model):
    img = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural='1. Banners'


#categories
class Category(models.Model):
    title = models.CharField(max_length=100)
    image= models.ImageField(upload_to='cat_imgs/')

    class Meta:
        verbose_name_plural='2. Categories'

    def image_tag(self):
        return mark_safe('<img src="%s" height="50" width="50" />' % (self.image.url))

    def __str__(self):
        return self.title


#brands
class Brand(models.Model):
    title = models.CharField(max_length=100)
    image= models.ImageField(upload_to='brand_imgs/')

    class Meta:
        verbose_name_plural='3. Brands'

    def __str__(self):
        return self.title

#organizations
class Organization(models.Model):
    title = models.CharField(max_length=100)
    image= models.ImageField(upload_to='org_imgs/')

    class Meta:
        verbose_name_plural='4. Organizations'

    def __str__(self):
        return self.title


# color
class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='5. Colors'

    def color_bg(self):
        return mark_safe('<div style="width:50px; height:50px; background-color:%s" ></div>' % (self.color_code))

    def __str__(self):
        return self.title

#size
class Size(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='6. Sizes'

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "product_imgs/")
    slug = models.CharField(max_length=400)
    detail = models.TextField()
    specs = models.TextField()
    # price = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    orgs = models.ForeignKey(Organization, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='7. Products'

    def __str__(self):
        return self.title


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product,on_delete=CASCADE)
    color = models.ForeignKey(Color,on_delete=CASCADE)
    size = models.ForeignKey(Size,on_delete=CASCADE)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural='8. ProductAttributes'

    def __str__(self):
        return self.product.title
