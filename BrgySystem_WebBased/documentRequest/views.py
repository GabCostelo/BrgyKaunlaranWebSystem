from django.shortcuts import render,get_object_or_404
from documentRequest.forms import brgyIndigencyForm,brgyClearanceForm,brgyResidencyForm
from documentRequest.models import BrgyIndigency,BrgyClearance,BrgyResidency
from django.views.generic import DetailView
from accounts.models import Constituent

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

#User View
def updateReq(request,pk):
    context = {}
    obj = get_object_or_404(BrgyIndigency, pk=pk)
    doneform = brgyIndigencyForm(data=request.POST or None,instance=obj)
    if doneform.is_valid():
        doneform.save(commit=False)
        obj.is_Pending = False
        obj.is_Done = True
        doneform.save()
        context["dataset"]=BrgyIndigency.objects.filter(is_Pending=True)
        return render(request,'staffview_Indigency.html',context)
    else:
        print(doneform.errors)
    return render(request,'update_view.html',{'doneform':doneform})

#BrgyIndigency
def brgyIndigencyView(request):
        if request.method == 'POST':
            docReq_form = brgyIndigencyForm(request.POST, request.FILES)
            if docReq_form.is_valid():
                docReq_form.save(commit=False)
                BrgyIndigency.is_Pending=True
                docReq_form.save()
                return render(request,'index.html')
            else:
                print(docReq_form.errors)
        else:
            docReq_form = brgyIndigencyForm

        return render(request,'brgyIndigency_docRequest.html',{'docReq_form':docReq_form})

#BrgyClearance
def brgyClearanceView(request):
        if request.method == 'POST':
            docReq_form = brgyClearanceForm(request.POST, request.FILES)
            if docReq_form.is_valid():
                docReq_form.save(commit=False)
                BrgyClearance.is_Pending=True
                docReq_form.save()
                return render(request,'index.html')
            else:
                print(docReq_form.errors)
        else:
            docReq_form = brgyClearanceForm

        return render(request,'brgyClearance_docRequest.html',{'docReq_form':docReq_form})

def updateReqClearance(request,pk):
    context = {}
    obj = get_object_or_404(BrgyClearance, pk=pk)
    doneform = brgyClearanceForm(data=request.POST or None,instance=obj)
    if doneform.is_valid():
        doneform.save(commit=False)
        obj.is_Pending = False
        obj.is_Done = True
        doneform.save()
        context["dataset"]=BrgyClearance.objects.filter(is_Pending=True)
        return render(request,'staffview_Clearance.html',context)
    else:
        print(doneform.errors)
    return render(request,'update_view.html',{'doneform':doneform})


#BrgyResidency
def brgyResidencyView(request):
        if request.method == 'POST':
            docReq_form = brgyResidencyForm(request.POST, request.FILES)
            if docReq_form.is_valid():
                docReq_form.save(commit=False)
                BrgyResidency.is_Pending=True
                docReq_form.save()
                return render(request,'index.html')
            else:
                print(docReq_form.errors)
        else:
            docReq_form = brgyResidencyForm

        return render(request,'brgyResidency_docRequest.html',{'docReq_form':docReq_form})

def updateReqResidency(request,pk):
    context = {}
    obj = get_object_or_404(BrgyResidency, pk=pk)
    doneform = brgyResidencyForm(data=request.POST or None,instance=obj)
    if doneform.is_valid():
        doneform.save(commit=False)
        obj.is_Pending = False
        obj.is_Done = True
        doneform.save()
        context["dataset"]=BrgyResidency.objects.filter(is_Pending=True)
        return render(request,'staffView_Residency.html',context)
    else:
        print(doneform.errors)
    return render(request,'update_view.html',{'doneform':doneform})

#history
def history(request):
    context = {}
    context["dataset"] = BrgyIndigency.objects.all
    return render(request,'history.html',context)
#Staff View
#IndigencyViews
def indigencyListView(request):
    context = {}
    context["dataset"] = BrgyIndigency.objects.filter(is_Pending=True)
    return render(request,'staffview_Indigency.html',context)

class indigencyDetail(DetailView):
    model = BrgyIndigency
    template_name = 'indigencyDetail.html'
#ClearanceViews
def clearanceListView(request):
    context = {}
    context["dataset"] = BrgyClearance.objects.filter(is_Pending=True)
    return render(request,'staffView_Clearance.html',context)

class clearanceDetail(DetailView):
    model = BrgyClearance
    template_name = 'clearanceDetail.html'

#ResidencyViews
def residencyListView(request):
    context = {}
    context["dataset"] = BrgyResidency.objects.filter(is_Pending=True)
    return render(request,'staffView_Residency.html',context)

class residencyDetail(DetailView):
    model = BrgyResidency
    template_name = 'residencyDetail.html'

#certificate
class generatePdf(DetailView):
    model = BrgyIndigency
    template_name = 'certificate.html'

class generatePdfClearance(DetailView):
    model = BrgyClearance
    template_name = 'clearance.html'

class generatePdfResidency(DetailView):
    model = BrgyResidency
    template_name = 'residency.html'

def sendUpdateIndigency(request,pk):
    context={}
    context["data"] = BrgyIndigency.objects.get(pk=pk)
    if request.method == 'POST':
        bodySubject = request.POST.get('StatusBody')
        em = request.POST.get('emailParam')
        subject = 'Document Request Update'
        message = bodySubject
        email_from = settings.EMAIL_HOST_USER
        recipient_list =[em,]
        send_mail( subject, message, email_from, recipient_list , fail_silently = False)
        return render(request,'indigencyDetail.html',context)

    return render(request,'sendStatus.html',context)

def sendUpdateClearance(request,pk):
    context={}
    context["data"] = BrgyClearance.objects.get(pk=pk)
    if request.method == 'POST':
        bodySubject = request.POST.get('StatusBody')
        em = request.POST.get('emailParam')
        subject = 'Document Request Update'
        message = bodySubject
        email_from = settings.EMAIL_HOST_USER
        recipient_list =[em,]
        send_mail( subject, message, email_from, recipient_list , fail_silently = False)
        return render(request,'clearanceDetail.html',context)

    return render(request,'sendStatus.html',context)

def sendUpdateResidency(request,pk):
    context={}
    context["data"] = BrgyResidency.objects.get(pk=pk)
    if request.method == 'POST':
        bodySubject = request.POST.get('StatusBody')
        em = request.POST.get('emailParam')
        subject = 'Document Request Update'
        message = bodySubject
        email_from = settings.EMAIL_HOST_USER
        recipient_list =[em,]
        send_mail( subject, message, email_from, recipient_list , fail_silently = False)
        return render(request,'residencyDetail.html',context)

    return render(request,'sendStatus.html',context)
