from django.shortcuts import render,redirect,HttpResponse
from .models import SearchModel
from django.db.models import Q
from django.contrib import messages




# Create your views here.
def registerdetails(request):
    return render(request,'register.html')


def savedeatils(request):
    companyname = request.POST.get('t1')
    ceo = request.POST.get('t2')
    headquter = request.POST.get('t3')
    founder = request.POST.get('t4')
    SearchModel(company_name=companyname,ceo=ceo,headquater=headquter,founder=founder).save()
    return render(request,'register.html',{'message':'data is inserted'})

def showdetails(request):
    if request.method == 'POST':
        search1 = request.POST['srh']
        search = search1.swapcase()
        print(search)
        if search:
            match = SearchModel.objects.filter(Q(company_name__icontains=search))

            if match:
                return render(request,'search.html',{'sr':match})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponse(search)
    return render(request,'search.html')



