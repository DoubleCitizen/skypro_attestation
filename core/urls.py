from django.urls import path

from . import views

urlpatterns = [
    path('factory/create', views.FactoryCreateView.as_view(), name='create_factory'),
    path('factory/list', views.FactoryListView.as_view(), name='list_factory'),
    path('factory/<pk>', views.FactoryView.as_view(), name='retrieve_factory'),
    path('factory/<pk>/update', views.FactoryUpdateView.as_view(), name='update_factory'),
    path('factory/<pk>/delete', views.FactoryDeleteView.as_view(), name='delete_factory'),
    path('retail/create', views.RetailChainCreateView.as_view(), name='create_retail'),
    path('retail/list', views.RetailChainListView.as_view(), name='list_retail'),
    path('retail/<pk>', views.RetailChainView.as_view(), name='retrieve_retail'),
    path('retail/<pk>/update', views.RetailUpdateView.as_view(), name='update_retail'),
    path('retail/<pk>/delete', views.RetailDeleteView.as_view(), name='delete_retail'),
    path('ie/create', views.IndividualEntrepreneurCreateView.as_view(), name='create_ie'),
    path('ie/list', views.IndividualEntrepreneurListView.as_view(), name='list_ie'),
    path('ie/<pk>', views.IndividualEntrepreneurView.as_view(), name='retrieve_ie'),
    path('ie/<pk>/update', views.IndividualEntrepreneurUpdateView.as_view(), name='update_ie'),
    path('ie/<pk>/delete', views.IndividualEntrepreneurDeleteView.as_view(), name='delete_ie'),
    path('contact/create', views.ContactCreateView.as_view(), name='create_contact'),
    path('contact/list', views.ContactListView.as_view(), name='list_contact'),
    path('contact/<pk>', views.ContactView.as_view(), name='retrieve_contact'),
    path('contact/<pk>/update', views.ContactUpdateView.as_view(), name='update_contact'),
    path('contact/<pk>/delete', views.ContactDeleteView.as_view(), name='delete_contact'),
]
