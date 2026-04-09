from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # Clientes
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/novo/', views.criar_cliente, name='criar_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/excluir/<int:pk>/', views.excluir_cliente, name='excluir_cliente'),
    
    # Compras
    path('compras/nova/', views.nova_compra, name='nova_compra'),
    path('compras/editar/<int:pk>/', views.editar_compra, name='editar_compra'),
    path('compras/excluir/<int:pk>/', views.excluir_compra, name='excluir_compra'),
    
    # Pagamentos
    path('pagamentos/novo/', views.novo_pagamento, name='novo_pagamento'),
    path('pagamentos/editar/<int:pk>/', views.editar_pagamento, name='editar_pagamento'),
    path('pagamentos/excluir/<int:pk>/', views.excluir_pagamento, name='excluir_pagamento'),
    
    path('historico/', views.historico, name='historico'),
]