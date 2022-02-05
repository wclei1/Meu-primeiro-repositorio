from datetime import datetime

ano_atual = datetime.now().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc
print(f'Em {ano_atual} sua idade é {idade}')
if idade > 18:
    print(f'Você deveria ter se alistado à {idade - 18} ano(s), Seu alistamento foi em {ano_nasc + 18}.')
elif idade < 18:
    print(f'Seu alistamento é daqui á {18 - idade} ano(s) em {ano_atual + (18 - idade)}.')
else:
    print('Você tem que se alistar IMEDIATAMENTE.')