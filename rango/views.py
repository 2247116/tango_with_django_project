from django.shortcuts import render

from django.http import HttpResponse

from rango.models import Category

from rango.models import page

from rango.forms import CategoryForm

from rango.forms import PageForm


def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}
    # Render the response and send it back!
	return render(request, 'rango/index.html', context_dict)

def add_category(request):
	form = CategoryForm()

	if request.method =='POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit = True)

			return index(request)
		else:
			print(form.errors)
	return render(request, 'rango/add_category.html', {'form':form})

def add_page(request, category_name_slug):
	try:
		category = Category.objects.get(slug = category_name_slug)
	except Category.DoesNotExist:
		category = None

	form = PageForm()
	if requested.method =='POST':
		form = PageForm(request.POST)
		if form.is_valid:
			if category:
				page = form.save(commit = False)
				page.category = category 
				page.views = 0
				page.save()
				return show_category(request, category_name_slug)
		else:
			print(form.errors)
	context_dict = {'form':form, 'category': category}
	return render(request, 'rango/add_page.html', context_dict)


def show_category(request, category_name_slug):
	context_dict = {}
	print(request.method)
	print(request.user)

	try:

		category = Category.objects.get(slug  = category_name_slug)
		pages = page.objects.filter(category = category)

# Can we find a category name slug with the given name?
# If we can't, the .get() method raises a DoesNotExist exception.
# So the .get() method returns one model instance or raises an exception. category = Category.objects.get(slug=category_name_slug)
# Retrieve all of the associated pages.
# Note that filter() will return a list of page objects or an empty list pages = Page.objects.filter(category=category)
        # Adds our results list to the template context under name pages.
		context_dict['pages'] = pages
# We also add the category object from
# the database to the context dictionary.
# We'll use this in the template to verify that the category exists. context_dict['category'] = category
	except Category.DoesNotExist:
		cotext_dict['category'] = None
		context_dict['pages'] = None
# We get here if we didn't find the specified category. # Don't do anything -
	return render(request, 'rango/category.html', context_dict)

def about(request):

	print(request.method )
	print(request.user)
	return render(request, 'rango/about.html', {}) 

def rangImage(request):
	print(request.method)
	print(request.user)
	return render(request, 'rango/about.html',{})
	  

# Create your views here.
