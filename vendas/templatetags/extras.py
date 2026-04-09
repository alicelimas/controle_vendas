from django import template
from decimal import Decimal

register = template.Library()

@register.filter(name='br_currency')
def br_currency(value):
    """Formata valor para padrão brasileiro: 1.234,56"""
    if value is None:
        return "0,00"
    try:
        valor = Decimal(str(value))
        # Formata com ponto para milhar e vírgula para decimal
        return f"{valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    except:
        return "0,00"