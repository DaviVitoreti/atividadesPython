def soma_imposto(taxa, custo):
    soma = custo + (custo * taxa)
    return soma

taxa = 0.2
custo = 1000
preco_final = soma_imposto(taxa, custo)
print(f"Preço final = {preco_final}")