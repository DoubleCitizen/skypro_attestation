from rest_framework import generics, filters

from core.models import Factory, RetailChain, IndividualEntrepreneur, Contact
from rest_framework import permissions

from core.serializers import FactorySerializer, RetailChainSerializer, IndividualEntrepreneurSerializer, \
    ContactSerializer


class ContactCreateView(generics.CreateAPIView):
    model = Contact
    permissions = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer


class ContactUpdateView(generics.UpdateAPIView):
    model = Contact
    permissions = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer


class ContactDeleteView(generics.DestroyAPIView):
    model = Contact
    permissions = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer


class ContactView(generics.RetrieveAPIView):
    model = Contact
    permissions = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactListView(generics.ListAPIView):
    model = Contact
    permissions = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['city']
    ordering = ['city']
    search_fields = ['city']


class FactoryCreateView(generics.CreateAPIView):
    model = Factory
    permissions = [permissions.IsAuthenticated]
    serializer_class = FactorySerializer


class FactoryView(generics.RetrieveAPIView):
    model = Factory
    permissions = [permissions.IsAuthenticated]
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()


class FactoryUpdateView(generics.UpdateAPIView):
    model = Factory
    permissions = [permissions.IsAuthenticated]
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()


class FactoryDeleteView(generics.DestroyAPIView):
    model = Factory
    permissions = [permissions.IsAuthenticated]
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()


class FactoryListView(generics.ListAPIView):
    model = Factory
    permissions = [permissions.IsAuthenticated]
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['city']
    ordering = ['city']
    search_fields = ['city']


class RetailChainCreateView(generics.CreateAPIView):
    model = RetailChain
    permissions = [permissions.IsAuthenticated]
    serializer_class = RetailChainSerializer


class RetailChainView(generics.RetrieveAPIView):
    model = RetailChain
    permissions = [permissions.IsAuthenticated]
    serializer_class = RetailChainSerializer
    queryset = RetailChain.objects.all()


class RetailUpdateView(generics.UpdateAPIView):
    model = RetailChain
    permissions = [permissions.IsAuthenticated]
    serializer_class = RetailChainSerializer
    queryset = RetailChain.objects.all()


class RetailDeleteView(generics.DestroyAPIView):
    model = RetailChain
    permissions = [permissions.IsAuthenticated]
    serializer_class = RetailChainSerializer
    queryset = RetailChain.objects.all()


class RetailChainListView(generics.ListAPIView):
    model = RetailChain
    permissions = [permissions.IsAuthenticated]
    serializer_class = RetailChainSerializer
    queryset = RetailChain.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['city']
    ordering = ['city']
    search_fields = ['city']


class IndividualEntrepreneurCreateView(generics.CreateAPIView):
    model = IndividualEntrepreneur
    permissions = [permissions.IsAuthenticated]
    serializer_class = IndividualEntrepreneurSerializer


class IndividualEntrepreneurView(generics.RetrieveAPIView):
    model = IndividualEntrepreneur
    permissions = [permissions.IsAuthenticated]
    serializer_class = IndividualEntrepreneurSerializer
    queryset = IndividualEntrepreneur.objects.all()


class IndividualEntrepreneurUpdateView(generics.UpdateAPIView):
    model = IndividualEntrepreneur
    permissions = [permissions.IsAuthenticated]
    serializer_class = IndividualEntrepreneurSerializer
    queryset = IndividualEntrepreneur.objects.all()


class IndividualEntrepreneurDeleteView(generics.DestroyAPIView):
    model = IndividualEntrepreneur
    permissions = [permissions.IsAuthenticated]
    serializer_class = IndividualEntrepreneurSerializer
    queryset = IndividualEntrepreneur.objects.all()


class IndividualEntrepreneurListView(generics.ListAPIView):
    model = IndividualEntrepreneur
    permissions = [permissions.IsAuthenticated]
    serializer_class = IndividualEntrepreneurSerializer
    queryset = IndividualEntrepreneur.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['city']
    ordering = ['city']
    search_fields = ['city']
