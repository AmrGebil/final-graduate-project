from django.shortcuts import render
from .models import first_aid,disease_knowledge
# Create your views here.
def first_aidView(request):
    name1 = request.GET.get('name1')
    fristAid=first_aid.objects.filter(name=name1)

    return render(request,'helpingPatients/firstaid.html',{'fristAids':fristAid})

def disease_knowledgeView(request):
    name1 = request.GET.get('name1')
    diseaseKnowledge = disease_knowledge.objects.filter(name=name1)

    return render(request, 'helpingPatients/diseaseknowledge.html', {'diseaseKnowledges': diseaseKnowledge})