# crie um programa que calcule a quantidade de bebidas e de carne
# para a organizaçao de um churrasco
#
# etapas de resoluçao:
# 1) solicitar o numero de convidados
# 2) criar uma funçao para calcular a quantidade total de bebidas
# 3) criar uma funçao para calcular a quantidade total de carnes
# 4) apresentar o resultado com os valores de total de carne e bebidas 
# a serem comprados 

# 1) solicitar o numero de convidados
# usamos o int por que convidamos deve ser um numero inteiro 
convidados= int(input("Digite o numero de convidados:"))
 
 # 2) Criar uma funçao para calcular a quantidade total de bebidas
def calcular_bebidas(convidados,consumo_por_pessoa_ml =800, volume_garrafa_litro=2.25 ):
    total_ml= convidados * consumo_por_pessoa_ml/1000

    garrafas= int(total_ml//volume_garrafa_litro)
    if total_litro % volume_garrafa_litro
        garrafas += 1
    return total_litro, garrafas

resultado=calcular_bebidas(convidados)
print