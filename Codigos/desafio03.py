capacidade_atual, aumento_percentual = map(int, input().split())

# Valor Total=Valor Original+Valor Original×Taxa de Aumento Percentual (formula)
nova_capacidade_total = int(capacidade_atual * (1 + aumento_percentual / 100))

print(nova_capacidade_total)
