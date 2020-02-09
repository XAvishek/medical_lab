from django.db.models import Q
from django.shortcuts import render
from medical_lab.models import Doctor, Patient, TestCategory

# Create your views here.

def is_valid_queryparam(param):
    return param != '' and param is not None

def bootstrapfilterview(request):
    qs = Patient.objects.all()
    test_categories = TestCategory.objects.all() 
    name_contains_query = request.GET.get('name_contains')
    id_exact_query = request.GET.get('id_exact')
    patient_or_doctor_query = request.GET.get('patient_or_doctor')
    patient_address = request.GET.get('patient_address')
    min_age = request.GET.get('min_age')
    max_age = request.GET.get('max_age')
    min_date = request.GET.get('min_date')
    max_date = request.GET.get('max_date')
    test_category = request.GET.get('test_category')
    tested = request.GET.get('tested')
    not_tested = request.GET.get('not_tested')

    if is_valid_queryparam(name_contains_query):
        qs = qs.filter(name__icontains=name_contains_query)

    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)
    
    elif is_valid_queryparam(patient_or_doctor_query):
        qs = qs.filter(Q(name__icontains=patient_or_doctor_query)|
                        Q(doctor__name__icontains=patient_or_doctor_query)
                        ).distinct() 
    
    if is_valid_queryparam(patient_address):
        qs = qs.filter(address__icontains = patient_address)

    if is_valid_queryparam(min_age):
        qs = qs.filter(age__gte = min_age)

    if is_valid_queryparam(max_age):
        qs = qs.filter(age__lt=max_age)
    
    if is_valid_queryparam(min_date):
        qs = qs.filter(collected_date__gte=min_date)

    if is_valid_queryparam(max_date):
        qs = qs.filter(collected_date__lt=max_date)

    if is_valid_queryparam(test_category) and test_category != 'Choose...':
        qs = qs.filter(test_category__name=test_category)

    if tested == 'on':
        qs = qs.filter(tested=True)

    elif tested == 'on':
        qs = qs.filter(tested=False)

    context = {
        'queryset': qs,
        'test_categories': test_categories
    }
    return render(request, 'bootstrap_form.html', context)