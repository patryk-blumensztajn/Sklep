from django.shortcuts import render, get_object_or_404
from .models import Category, Product, SubCategory, SubSubCategory, Computer
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None, subcategory_slug=None, subsubcategory_slug=None):
	category = None
	subcategory = None
	categories = Category.objects.all()
	subcategories = SubCategory.objects.all()
	subsubcategories = SubSubCategory.objects.all()
	products = Product.objects.filter(available=True)
	products_by_price_asc = products.filter(subsubcategory=subsubcategory).order_by('price')
	products_by_price_desc = products.filter(subsubcategory=subsubcategory).order_by('-price')
	if category_slug:
		category = get_object_or_404(Category,slug=category_slug)
		products = products.filter(category=category)
		products_by_price_asc = products.filter(subsubcategory=subsubcategory).order_by('price')
		products_by_price_desc = products.filter(subsubcategory=subsubcategory).order_by('-price')
	return render(request,'shop/product/list.html',{'subcategory':subcategory,'subsubcategory':subsubcategory,'category':category,
													'categories':categories, 'subcategories':subcategories,
													'products':products,
													'products_by_price_asc':products_by_price_asc,'products_by_price_asc':products_by_price_desc,})
# Create your views here.

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	if (get_object_or_404(Product, id=id, slug=slug, available=True).category.name == "Komputery"):
		product = get_object_or_404(Computer, id=id, slug=slug, available=True)
	cart_product_form = CartAddProductForm()
	return render (request,'shop/product/detail.html',{'product':product, 'cart_product_form': cart_product_form})

# Alternatywa
# for n in Computer: czy ten for wogole potrzeby?
# 	if (get_object_or_404(Computer, id=id, slug=slug, available=True)):
# 		product = get_object_or_404(Computer, id=id, slug=slug, available=True)
# for m in Tea:
# 	...
	
	
	
	
	
	


