from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

# Create your views here.
def index(request):

    return redirect('/shows')


def new_show(request):

    return render(request, 'new_shows.html')


def create_show(request):

    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/shows/new')
    
    else:
        new_show = Show.objects.create(
            title = request.POST['show_title'],
            network = request.POST['show_network'],
            release_date = request.POST['show_release_date'],
            description = request.POST['show_description']
        )

    return redirect(f'/shows/{new_show.id}')


def all_shows(request):

    context = {
        "all_shows": Show.objects.all()
    }

    return render(request, 'all_shows.html', context)


def show_detail(request, show_id):

    context = {
        'show': Show.objects.get(id = show_id)
    }

    return render(request, 'show_detail.html', context)


def show_edit(request, show_id):

    context = {
        'show': Show.objects.get(id = show_id)
    }

    return render(request, 'show_edit.html', context)


def show_update(request, show_id):

    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect(f'/shows/{show_id}/edit')
    
    else:
        show = Show.objects.get(id = show_id)
        show.title = request.POST['show_title']
        show.network = request.POST['show_network']
        show.release_date = request.POST['show_release_date']
        show.description = request.POST['show_description']
        show.save()

    return redirect(f'/shows/{show_id}')


def show_delete(request, show_id):

    show = Show.objects.get(id = show_id)
    show.delete()

    return redirect(f'/shows')