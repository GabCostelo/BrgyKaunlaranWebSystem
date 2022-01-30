from django.shortcuts import render,get_object_or_404
from accounts.models import User
from documentRequest.models import BrgyIndigency,BrgyClearance,BrgyResidency
from django.views.generic import DetailView
# Create your views here.


def recordIndex(request):
    return render(request,'base_records.html')

def recordUser(request):
    return render(request,'userRecord.html')

def recordDoc(request):
    return render(request,'documentRecords.html')

def Userlist(request):
    context = {}
    context["dataset"] = User.objects.all
    return render(request,'userRecordList.html',context)

def StaffList(request):
    context = {}
    context["dataset"] = User.objects.filter(is_BrgyStaff=True)
    return render(request,'userRecordList.html',context)

def ConsList(request):
    context = {}
    context["dataset"] = User.objects.filter(is_Constituent=True)
    return render(request,'userRecordList.html',context)

def IndigencyList(request):
    context = {}
    context["dataset"] = BrgyIndigency.objects.filter(is_Done=True)
    return render(request,'docRecordList.html',context)

def ClearanceList(request):
    context = {}
    context["dataset"] = BrgyClearance.objects.filter(is_Done=True)
    return render(request,'docRecordList.html',context)

def ResidencyList(request):
    context = {}
    context["dataset"] = BrgyResidency.objects.filter(is_Done=True)
    return render(request,'docRecordList.html',context)
