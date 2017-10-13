from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True,unique=True)
	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('shop:product_list_by_category', args=[self.slug])
	
class SubCategory(models.Model):
	category = models.ForeignKey(Category,related_name='category')
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True,unique=True)
	class Meta:
		ordering = ('name',)
		verbose_name = 'subcategory'
		verbose_name_plural = 'subcategories'
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('shop:product_list_by_category' ,args=[self.category.slug, self.slug])
	
class SubSubCategory(models.Model):
	subcategory = models.ForeignKey(SubCategory,related_name='subcategory')
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True,unique=True)
	class Meta:
		ordering = ('name',)
		verbose_name = 'subsubcategory'
		verbose_name_plural = 'subsubcategories'
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('shop:product_list_by_category', args=[self.subcategory.category.slug, self.subcategory.slug ,self.slug])
	#w adminie kategoria jest opcjonalna
	
class Product(models.Model):
	category = models.ForeignKey(Category,related_name='products')
	subcategory = models.ForeignKey(SubCategory,related_name='products',blank=True,null=True)
	subsubcategory = models.ForeignKey(SubSubCategory,related_name='products',blank=True,null=True)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	def get_absolute_url(self):
		return reverse('shop:product_detail', args=[self.id, self.slug])
	
	class Meta:
		ordering = ('name',)
		index_together = (('id','slug'),)
	
	def __str__(self):
		return self.name
	
class Computer(Product):
	ram = models.DecimalField(
        ("Screen size"),
        max_digits=4,
        decimal_places=2,
    )

	
# Create your models here.
