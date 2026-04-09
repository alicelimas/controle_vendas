from django.contrib import admin
from .models import Cliente, Compra, Pagamento

admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Pagamento)