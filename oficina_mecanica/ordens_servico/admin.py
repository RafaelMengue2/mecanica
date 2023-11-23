from django.contrib import admin
from .models import Cliente, Veiculo, Mecanico, Servico, Peca, OrdemServico

admin.site.register(Cliente)
admin.site.register(Veiculo)
admin.site.register(Mecanico)
admin.site.register(Servico)
admin.site.register(Peca)
admin.site.register(OrdemServico)
