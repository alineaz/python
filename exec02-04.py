# Escreva um programa que receba o ano de nascimento, e que ele retorne a geração a qual a pessoa pertence. 
# Para definir a qual geração uma pessoa pertence, temos a seguinte tabela: 

# Baby Boomer -> até 1964
# Geração X - > 1965 - 1979 
# Geração Y -> 1980 - 1994  
# Geração Z -> 1995 - atual 

# Para testar se seu script está funcionando, considere os seguintes resultados esperados:

# ano nascimento = 1988: geração Y
# ano nascimento = 1958: geração baby boomer 
# ano nascimento = 1996: geração Z

ano = input("Digite o ano de nascimento: ")
ano = int(ano)

if ano <= 1964:
    print("Geração Baby Boomer!")

if ano >= 1965 and ano <= 1979:
    print("Geração X!")

if ano >= 1980 and ano <= 1994:
    print("Geração Y!")

if ano >= 1995:
    print("Geração Z!")

# correção:
    
nasc = int(input("Em que ano voce nasceu? "))

if nasc <= 1964:
    print("Voce pertence a geração Baby Boomer")
elif nasc <= 1979:
    print("Voce pertence a geração X")
elif nasc <= 1994:
    print("Voce pertence a geração Y")
else:
    print("Voce pertence a geração Z")
