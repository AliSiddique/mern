from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from .models import Listing, ListingViews, ListingTour, ListingMail
from .serializers import ListingSerializer, ListingMailSerializer, ListingTourSerializer
from rest_framework.response import Response
from .filters import ListingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
# Create your views here.
class ListingList(ListAPIView):
    serializer_class = ListingSerializer
    def get_queryset(self):
        qs = Listing.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            qs = qs.filter(title__icontains=title)
            print(qs)
        return qs   


@api_view(['GET'])
def get_listings(request):
    filterset = ListingFilter(request.GET,queryset=Listing.objects.all().order_by('-created_at'))
    count = filterset.qs.count()
    resPerPage = 10
    paginator = PageNumberPagination()
    paginator.page_size = resPerPage
    queryset = paginator.paginate_queryset(filterset.qs,request)
    serializer = ListingSerializer(queryset,many=True)

    return Response({'listing':serializer.data,'resPerPage':resPerPage,'count':count})



@api_view(['POST'])
def create_listing(request):
    user = request.user
    title = request.data['title']
    description = request.data['description']
    price = request.data['price']
    bedrooms = request.data['bedrooms']
    location = request.data['location']
    bathrooms = request.data['bathrooms']
    is_published = request.data['is_published']
    photo_main = request.FILES['photo_main']
    photo_1 = request.FILES['photo_1']
    photo_2 = request.FILES['photo_2']
    photo_3 = request.FILES['photo_3']
    photo_4 = request.FILES['photo_4']
    photo_5 = request.FILES['photo_5']
    photo_6 = request.FILES['photo_6']
    listing = Listing.objects.create(
        user=user,
        title=title,
        description=description,
        price=price,
        bedrooms=bedrooms,
        bathrooms=bathrooms,
        location=location,
        is_published=is_published,
        photo_main=photo_main,
        photo_1=photo_1,
        photo_2=photo_2,
        photo_3=photo_3,
        photo_4=photo_4,
        photo_5=photo_5,
        photo_6=photo_6
    )
    serializer = ListingSerializer(listing,many=False)
    return Response(serializer.data)





@api_view(['PUT'])
def update_listing(request,pk):
    listing = get_object_or_404(Listing,id=pk)
    if listing.user != request.user:
        return Response({'message':'You can not update this job'},status=HTTP_403_FORBIDDEN)
    listing.title = request.data['title']   
    listing.description = request.data['description']
    listing.price = request.data['price']
    listing.bedrooms  = request.data['bedrooms']
    listing.bathrooms = request.data['bathrooms']
    listing.user = request.user
    listing.save()
    serializer = ListingSerializer(listing,many=False)
    return Response(serializer.data)    




@api_view(['DELETE'])
def delete_listing(request,pk):
    listing = Listing.objects.get(id=pk)
    if listing.user != request.user:
        return Response({'message':'You can not delete this listing'},status=HTTP_403_FORBIDDEN)
    listing.delete()
    return Response({"Message":'Listing deleted'},status=HTTP_200_OK)    

@api_view(['GET'])
def get_listing(request,pk):
    listing = Listing.objects.get(id=pk)
    serializer = ListingSerializer(listing,many=False)
    return Response(serializer.data)    













@api_view(['POST'])
def create_mail(request):
    data = request.data
    listing = ListingMail.objects.create(**data)
    serializer = ListingMailSerializer(listing,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_mails(request):
    listing = ListingMail.objects.filter(to_user=request.user)
    serializer = ListingMail(listing,many=True)
    return Response(serializer.data)    


@api_view(['GET'])
def get_mail(request,pk):
    listing = ListingMail.objects.get(id=pk)
    serializer = ListingMailSerializer(listing,many=False)
    return Response(serializer.data)    



@api_view(['POST'])
def create_tour(request):
    data = request.data
    listing = ListingTour.objects.create(**data)
    serializer = ListingTourSerializer(listing,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_tours(request,pk):
    listing = ListingTour.objects.filter(to_user=request.user)
    serializer = ListingTourSerializer(listing,many=True)
    return Response(serializer.data)    



@api_view(['GET'])
def get_tour(request,pk):
    listing = ListingTour.objects.get(id=pk)
    serializer = ListingTourSerializer(listing,many=False)
    return Response(serializer.data)    