#1)Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, 
#calcule e imprima (saída de dados) seu perímetro e sua área.
#Observação: a saída deve estar no formato: "perímetro: x - área: y
lado = float(input("Digite o lado de um quadrado qualquer: "))

perimetro = 4 * lado
area = lado ** 2

print (f"perímetro: {perimetro} - área: {area}")

#2) Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media= (nota1 + nota2 + nota3 + nota4) / 4

print (f"A média aritmética é {media}")

#######################
#EXERCICIOS ADICIONAIS#
#######################

#1) Uma empresa de cartão de crédito envia suas faturas por email com a seguinte mensagem:

#Olá, Fulano de Tal
#A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.

#Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, 
#o mês de vencimento e o valor da fatura  e imprima (saída de dados) a mensagem com os dados recebidos, no mesmo
#formato da mensagem acima. Note que o programa imprime a saída em duas linhas diferentes. Note também que, como 
#não é preciso realizar cálculos, o valor não precisa ser convertido para número, pode ser tratado como texto.

nome = input("Digite o nome do cliente: ")
dia = input("Digite o dia de vencimento: ")
mes = input("Digite o mês de vencimento: ")
valor =input("Digite o valor da fatura: ")

print(f"Olá, {nome}.\n A sua fatura com vencimento em {dia} de {mes} no valor de R$ {valor} está fechada.")

#2) Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em 
#Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. A saída deve 
#estar no formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato! 
#Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro
segundos = int(input("Insira um os segundos a serem convertidos: "))

dias = segundos // 86400
horas =  (segundos % 86400) // 3600
minutos = ((segundos % 86400) % 3600) // 60
segundo = ((segundos % 86400) % 3600) % 60

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundo} segundos.")

#3) Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. 
numero = int(input("Digite um número inteiro: "))
dezena = (numero // 10) % 10

print(f"O dígito das dezenas é {dezena}")