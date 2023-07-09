from django.shortcuts import render
from .models import Nurse
# Create your views here.
def nurses(request):
    city = request.GET.get('city')
    specialty = request.GET.get('specialty')
    nurses = None

    if city and specialty:
        nurses = Nurse.objects.filter(his_city=city, his_specialty=specialty)
    elif specialty:
        nurses = Nurse.objects.filter(his_specialty=specialty)
    elif city:
        nurses = Nurse.objects.filter(his_city=city)

    return render(request,'nurse/nursesList.html',{'nurses':nurses})

def nurse_detailes(request, id):
    nurse_detailes = Nurse.objects.get(id=id)
    context = {'nurse': nurse_detailes }
    return render(request, 'nurse/nursedetailes.html', context)
