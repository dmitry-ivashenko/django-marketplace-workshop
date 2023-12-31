from django.shortcuts import render, get_object_or_404

from item.models import Item, Category


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(pk=item.pk)

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
    })
