from django.contrib import admin
from .models import Account, Currency, Customer, Notification, Receipt,Transaction, Wallet,Card,ThirdParty,Loan,Reward

class CustomerAdmin(admin.ModelAdmin):
    list_display= ("first_name","last_name","address",)
    search_fields= ("firstname","lastname",)

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Card)
admin.site.register(ThirdParty)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)
admin.site.register(Transaction)


# Register your models here.
