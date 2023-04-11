import json  
from api.models import Company, Vacancy
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def list_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [ i.to_json() for i in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        print(data.get('name', ''))
        company = Company.objects.create(
            name = data.get('name', ''),
            description = data.get('description',''),
            city = data.get('city',''),
            address = data.get('address','')
            )
        return JsonResponse(company.to_json())


@csrf_exempt
def company_by_id(request, company_id):

    try:
        company = Company.objects.get(id = company_id)
        company_json = company.to_json()
    except:
        return JsonResponse({'error': "Don't find id" })


    if request.method =='GET':
        return JsonResponse(company_json)
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        print(data)

        name = data.get('name', '')
        description = data.get('description','')
        city = data.get('city','')
        address = data.get('address','')

        company.name = name
        company.description = description
        company.city = city
        company.address = address
        company.save()

        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'delete': True})
        


def vacancy_by_company(request, company_id):
    vacansies = Vacancy.objects.filter(company_id = company_id)
    vacansies_json = [ i.to_json() for i in vacansies]
    return JsonResponse(vacansies_json, safe=False)


def list_vacancies(request):
    vacansies = Vacancy.objects.all()
    vacansies_json = [ i.to_json() for i in vacansies]
    return JsonResponse(vacansies_json, safe=False)


def vacancy_by_id(request, vacancy_id):
    vacancies = Vacancy.objects.filter(id = vacancy_id)
    vacancies_json = [ i.to_json() for i in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def top_ten_vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary')
    top_ten = vacancies[:10]
    vacancies_json = [ i.to_json() for i in top_ten]
    return JsonResponse(vacancies_json, safe=False)

