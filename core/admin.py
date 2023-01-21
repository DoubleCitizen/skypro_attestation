from django.contrib import admin
from django.utils.html import format_html

from core.models import Factory, Contact, Product, RetailChain, \
    IndividualEntrepreneur


@admin.action(description='Обнулить задолженность')
def cancel_the_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city')


class RetailChainAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'debt', 'show_supplier')
    search_fields = ('name', 'city', 'supplier')
    actions = [cancel_the_debt]

    def show_supplier(self, obj):
        factory = Factory.objects.filter(id=obj.supplier_id).first()

        return format_html("<a href='{url}'>{description}</a>", description=f"Завод им. {factory}",
                           url=f"/admin/core/factory/{factory.id}")


class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'debt', 'show_supplier')
    search_fields = ('name', 'city', 'supplier')
    actions = [cancel_the_debt]

    def show_supplier(self, obj):
        retail_chain = RetailChain.objects.filter(id=obj.supplier_id).first()

        return format_html("<a href='{url}'>{description}</a>", description=f"Розничная сеть {retail_chain}",
                           url=f"/admin/core/retailchain/{retail_chain.id}")


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'city')
    search_fields = ('email', 'city')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Factory, FactoryAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(RetailChain, RetailChainAdmin)
admin.site.register(IndividualEntrepreneur, IndividualEntrepreneurAdmin)
