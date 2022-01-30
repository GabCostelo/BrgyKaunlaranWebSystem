from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'documentRequest'

urlpatterns = [
    path('pdf/<int:pk>',views.generatePdf.as_view(),name='generatePdf'),
    path('pdfclearance/<int:pk>',views.generatePdfClearance.as_view(),name='generatePdfClearance'),
    path('pdfresidency/<int:pk>',views.generatePdfResidency.as_view(),name='generatePdfResidency'),
    path('update_Indigency/<int:pk>',views.updateReq,name='updateReq'),
    path('update_Clearance/<int:pk>',views.updateReqClearance,name='updateReqClearance'),
    path('sentUpdate_Residency/<int:pk>',views.updateReqResidency,name='updateReqResidency'),
    path('sentUpdate_Indigency/<int:pk>',views.sendUpdateIndigency,name='sendUpdateInd'),
    path('sentUpdate_Clearance/<int:pk>',views.sendUpdateClearance,name='sendUpdateClear'),
    path('sentUpdate_Residency/<int:pk>',views.sendUpdateResidency,name='sendUpdateResident'),
    path('indigency_Request/',views.brgyIndigencyView,name='indgencyView'),
    path('clearance_Request/',views.brgyClearanceView,name='clearanceView'),
    path('residency_Request/',views.brgyResidencyView,name='residencyView'),
    path('staffView_Indigency/',views.indigencyListView,name='indigencyStaff'),
    path('staffView_DetailIndigency/<int:pk>',views.indigencyDetail.as_view(),name='indigencyDetail'),
    path('staffView_Clearance/',views.clearanceListView,name='clearanceStaff'),
    path('staffView_DetailClearance/<int:pk>',views.clearanceDetail.as_view(),name='clearanceDetail'),
    path('staffView_Residency/',views.residencyListView,name='residencyStaff'),
    path('staffView_DetailResidency/<int:pk>',views.residencyDetail.as_view(),name='residencyDetail'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
