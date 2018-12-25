from django.shortcuts import render, get_object_or_404

from .models import Mineral


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def mineral_details(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    fields = [field.name for field in Mineral._meta.get_fields()]
    fields = [entry for entry in fields if entry not in ('id', 'name', 'image_filename', 'image_caption')]
    return render(request, 'minerals/mineral_details.html', {'mineral': mineral, 'fields': fields,})


def mineral_by_letter(request, letter):
    minerals = Mineral.objects.filter(name__istartswith=letter)
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals, 'letter': letter})


def search_term(request):
    term = request.GET.get('q')
    minerals = Mineral.objects.filter(name__icontains=term)
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def group_search(request, group):
    minerals = Mineral.objects.filter(group__icontains=group)
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals, 'selected_group': group})
