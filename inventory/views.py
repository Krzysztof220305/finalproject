from django.shortcuts import render, redirect, get_object_or_404
from .models import Item

def item_list(request):
    """READ: Display all items."""
    items = Item.objects.all().order_by('-created_at')
    return render(request, 'inventory/item_list.html', {'items': items})

def item_create(request):
    """CREATE: Add a new item."""
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        Item.objects.create(name=name, description=description, image=image)
        return redirect('item_list')
    return render(request, 'inventory/item_form.html')

def item_update(request, id):
    """UPDATE: Edit an item."""
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        item.name = request.POST.get('name')
        item.description = request.POST.get('description')
        if request.FILES.get('image'):
            item.image = request.FILES.get('image')
        item.save()
        return redirect('item_list')
    return render(request, 'inventory/item_form.html', {'item': item})

def item_delete(request, id):
    """DELETE: Remove an item."""
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'inventory/item_confirm_delete.html', {'item': item})

# Create your views here.
