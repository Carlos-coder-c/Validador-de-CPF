cpf = "23577912320"

# Vamos agora fazer que o python pegue os primeiros 9 digitos

cpf_nove_digitos = cpf[:9] 

contagem_10 = 10

resultado = ''

for digito_1 in cpf_nove_digitos:
    digito_1 * 10 -= contagem_10 += resultado 

    digito_1 = (resultado * 10) % 11
    digito_1 = digito_1  if <9 else 0
    print(digito_1)
