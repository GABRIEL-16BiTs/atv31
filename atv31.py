def valor_imposto(valor):
    if valor <= 1000:
        return valor * 0.1
    elif valor <= 2000:
        return valor * 0.13
    else:
        return valor * 0.20

# Receber os valores dos produtos
produtos = []
for i in range(1, 5):  # Loop de 1 a 4 para os 4 produtos
    valor = float(input(f"Digite o valor do produto {i}: "))
    produtos.append(valor)

# Calcular e exibir o imposto para cada produto
for i, produto in enumerate(produtos, start=1):
    imposto = valor_imposto(produto)
    print(f"O imposto do produto {i} (R${produto:.2f}) é R${imposto:.2f}")
