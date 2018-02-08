import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					 'tango_with_django_project.settings')

import django 
django.setup()
from rango.models import Category, page

def populate():
	python_pages = [
		{"title": "Offical Python Tutorial",
		"url" : "http://docs.python.org/2/tutorial"},
		{"title": "How to Think like a Computer Scientist",
		"url": "http://www.greenteapress.com/thinkpython/"},
		{"title":"Learn Python in 10 Minutes",
		"url":"http://www.korokithakis.net/tutorials/python"}]

	django_pages = [
		{"title": "Offical Django Tutorial",
		"url":"http://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
		{"title":"Django Rocks",
		"url":"http://www.djangorocks.com/"},
		{"title":"How to Tango with Django",
		"url":"http://www.tangowithdjango.com/"}]

	other_pages = [
		{"title":"Bottle",
		"url":"http://bottlepy.org/docs/dev/"},
		{"title":"Flask",
		"url":"http://flask.pocoo.org"}]

	cats = {"python": {"Pages": python_pages, "views": 128, "likes": 64},
		"Django":{"Pages": django_pages, "views": 64, "likes": 32 },
		"other Frameworks": {"Pages":other_pages, "views": 42, "likes": 16} }


	for cat, cat_data in cats.items():
		c = add_cat(cat, cat_data["views"], cat_data["likes"])
		for p in cat_data["Pages"]:

			add_page(c, p["title"], p["url"],)

	for c in Category.objects.all():
		for p in page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c),str (p)))


def add_page(cat,title,url,views=0):
	p = page.objects.get_or_create(category = cat,title = title)[0]
	p.url = url
	p.views = views
	p.save()
	return p

def add_cat(name,views = 0,like = 0):
	c = Category.objects.get_or_create(name = name)[0]
	c.views = views
	c.like = like
	c.save()
	return c

if __name__ == '__main__':
	print("starting Rango Population script.......")
	populate()





	