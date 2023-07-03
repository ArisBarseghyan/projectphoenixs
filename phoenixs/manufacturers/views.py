from django.shortcuts import render, get_object_or_404
from cars.models import Company

def company_view(request):
    company = Company.objects.all()
    return render(request, 'company/company.html', {'company': company})

def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'company/detail.html', {'com': company})