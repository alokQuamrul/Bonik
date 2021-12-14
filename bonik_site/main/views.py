from django.shortcuts import render
from .models import Brand, Category, Product, ProductAttribute

# homepage

def home(request):
    tabCap = {'title':'Home:Bonik'}
    return render(request,'index.html',context=tabCap)

#category
def category_list(request):
    tabCap ={'title':'Categories'}
    data = Category.objects.all().order_by('-id')
    return render(request,'category-list.html',{'data':data})


# brand
def brand_list(request):
    tabCap = {'title':'Brands'}
    data = Brand.objects.all().order_by('-id')
    return render(request,'brand-list.html',{'data':data})

#products
def product_list(request):
    tabCap = {'title':'Products'}
    data = Product.objects.all().order_by('-id')
    cats = Product.objects.distinct().values('category__title','category__id')
    brands = Product.objects.distinct().values('brand__title','brand__id')
    # colors = ProductAttribute.objects.distinct().values('color__title','color__id','color__code')
    sizes = ProductAttribute.objects.distinct().values('size__title','size__id')

    return render(request,'product-list.html',
    {
        'data':data,
        'cats':cats,
        'brands':brands,
        # 'colors':colors,
        'sizes':sizes,


    }
    )
#product list according to the category

def category_product_list(request,cat_id):
    category = Category.objects.get(id=cat_id)
    data = Product.objects.filter(category=category).order_by('-id')
    return render(request, 'category-product-list.html',{'data':data})


#product Details

def product_detail(request,slug,id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html',{'data':product})

