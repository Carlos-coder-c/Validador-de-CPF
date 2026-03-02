cpf = "23577912320"

# Vamos agora fazer que o python pegue os primeiros 9 digitos

cpf_nove_digitos = cpf[:9] 

contagem_10 = 10

resultado = 0

for digito_1 in cpf_nove_digitos:
    resultado += int(digito_1 ) * contagem_10 
    contagem_10 -= 1

digito_1 = (resultado * 10) % 11
digito_1 = digito_1  if digito_1 <= 9 else 0
print(digito_1)
