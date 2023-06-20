from django.shortcuts import render, get_object_or_404
from .models import Category, Cloth


def cloth_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    cloths = Cloth.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        cloths = cloths.filter(category=category)
    return render(request,
                  'shop/cloth/cloth_list.html',
                  {'category': category,
                   'categories': categories,
                   'cloths': cloths})


def cloth_detail(request, id, cloth_slug):
    cloth = get_object_or_404(Cloth,
                              id=id,
                              slug=cloth_slug,
                              available=True)
    return render(request,
                  'shop/cloth/cloth_detail.html',
                  {'cloth': cloth})
