from django.urls import path
from api import views

urlpatterns = [
    path('companies/', views.list_companies),
    path('companies/<int:company_id>/', views.company_by_id),
    path('companies/<int:company_id>/vacancies/', views.vacancy_by_company),

    path('vacancies/', views.list_vacancies),
    path('vacancies/<int:vacancy_id>/', views.vacancy_by_id),
    path('vacancies/top_ten/', views.top_ten_vacancies)
]