from django.shortcuts import render
from .models import Doctor

# Create your views here.
# def doctorList(request):
#     city = request.GET.get('city')
#     specialty = request.GET.get('specialty')
#     if len(city)>0 and len(specialty)>0:
#         doctors = Doctor.objects.filter(his_city=city, his_specialty=specialty)
#     elif len(specialty)>0:
#         doctors = Doctor.objects.filter( his_specialty=specialty)
#     else:
#        doctors = Doctor.objects.filter(his_city=city)
#
#     return render(request,'doctor/doctorsList.html',{'doctors':doctors})


def doctorList(request):
    city = request.GET.get('city')
    specialty = request.GET.get('specialty')
    doctors = None

    if city and specialty:
        doctors = Doctor.objects.filter(his_city=city, his_specialty=specialty)
    elif specialty:
        doctors = Doctor.objects.filter(his_specialty=specialty)
    elif city:
        doctors = Doctor.objects.filter(his_city=city)

    return render(request, 'doctor/doctorsList.html', {'doctors': doctors})

def doctor_details(request, id):
    doctor_detailes = Doctor.objects.get(id=id)
    context = {'doctor': doctor_detailes }

    return render(request, 'doctor/doctordetails.html', context)


