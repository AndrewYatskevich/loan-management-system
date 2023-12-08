from django.contrib import admin

from loan_application.models import (
    Contract,
    LoanApplication,
    LoanApplicationProduct,
    Manufacturer,
    Product,
)


class ProductInline(admin.TabularInline):
    model = LoanApplicationProduct
    extra = 1


class LoanApplicationAdmin(admin.ModelAdmin):
    inlines = (ProductInline,)


admin.site.register(LoanApplication, LoanApplicationAdmin)
admin.site.register(Contract)
admin.site.register(Product)
admin.site.register(Manufacturer)
