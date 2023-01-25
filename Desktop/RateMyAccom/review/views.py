from multiprocessing import context
from django.shortcuts import render
from django.core import serializers
from review.forms import PostSearchForm
from .models import Accomodation, Post, University
from django.http import JsonResponse
from django.db.models import Q
from django.db.models import Avg

def home(request):
    universities = University.objects.all()[:9]
    form = PostSearchForm()
    q = ''
    results = []
    result = []

    query = Q()

    if request.POST.get('action') == 'post':
        search_string = str(request.POST.get('ss'))

        if search_string is not None:
            search_string = University.objects.filter(
                name__icontains=search_string)[:5]  or Accomodation.objects.filter(name__icontains=search_string)[:5]   


            data = serializers.serialize('json', list(
                search_string), fields=('id', 'name', 'slug'))

            return JsonResponse({'search_string': data})

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
       
            if q is not None:
                query &= Q(name__contains=q)
                results = University.objects.filter(query) 

    context = {
        "universities":universities,
        'form': form,
        'q': q,
        'results': results,'result':result
    }
    return render(request,"content/home.html",context)


def post_search(request):
    form = PostSearchForm()
    q = ''
    c = ''
    results = []
    result = []

    query = Q()

    if request.POST.get('action') == 'post':
        search_string = str(request.POST.get('ss'))

        if search_string is not None:
            search_string = University.objects.filter(
                name__icontains=search_string)[:5]  or Accomodation.objects.filter(name__icontains=search_string)[:5]   


            data = serializers.serialize('json', list(
                search_string), fields=('id', 'name', 'slug'))

            return JsonResponse({'search_string': data})

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
       
            if q is not None:
                query &= Q(name__contains=q)
                results = University.objects.filter(query) 


    return render(request, 'reviews/search.html',
                  {'form': form,
                   'q': q,
                   'results': results,'result':result})





# accomodation page
def accom(request,slug):
    accomodations = Accomodation.objects.filter(uni__name=slug)
    reviews = Post.objects.filter(accom__name=slug).count()

    context = {
        "accomodations":accomodations,
        "reviews":reviews
    }
    return render(request,"content/Accomodations.html",context)        
# posts page
def post(request,slug):
    posts = Post.objects.filter(accom__name=slug)
    rating_room = float(round(posts.aggregate(Avg('rating_room')).get('rating_room__avg')))
    rating_house = posts.aggregate(Avg('rating_house')).get('rating_house__avg')
    rating_bath = posts.aggregate(Avg('rating_bath')).get('rating_bath__avg')
    rating_location = posts.aggregate(Avg('rating_location')).get('rating_location__avg')
    posts_count = posts.count()
    rating_total = float((rating_room + rating_house + rating_bath + rating_location/ posts_count) / 5)

    accomodation = Accomodation.objects.get(name=slug)
    url  = slug
    context = {
        "posts":posts,
        "url":url,
        "accomodation":accomodation,
        "rating":rating_room,
        "review_amount":posts_count
        
    }
    return render(request,"content/Reviews.html",context)     



def createPost(request,slug):
    slug = slug
    context ={
        "url":slug
    }
    return render(request,"content/Create.html",context)



