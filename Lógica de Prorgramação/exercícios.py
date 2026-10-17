 #1.	Implemente o programa que calcule o volume de uma esfera de raio R. O usuário fornecerá o dado necessário.           
R=float(input('Qual o valor do raio da esfera?'))
PI=3.14159
volume=(4/3)*PI*R**3
print('o volume da esfera é ',volume)
#2.	 A água é um nutriente essencial. Sem ela, o corpo não pode funcionar com perfeição. 
#Cada pessoa precisa de uma quantidade diferente de água para hidratar o corpo. 
#A dose ideal, ou seja, a necessidade diária em litros é calculada através da fórmula: massa (em kg) vezes 0,03. 
#Elabore o programa que realize esse cálculo. 
massa=float(input('Qual o valor da sua massa em kg?'))
água= massa*0.03
print('A quantidade ideal de água é',água,'litros')
#3.	Construa o programa que tendo como dados de entrada dois pontos quaisquer do plano cartesiano, P(x1, y1) e Q(x2, y2), 
#calcule a distância entre eles:
x1=float(input('Qual o valor da primeira cordenada do ponto P(x1)?'))
y1=float(input('Qual o valor da segunda cordenada do ponto P(y1)?'))
x2=float(input('Qual o valor da primeira cordenada do ponto Q(x2)?'))
y2=float(input('Qual o valor da segunda cordenada do ponto Q(y2)?'))
distância=((x2-x1)**2+(y2-y1)**2)**(1/2)
print('a distância entre os dois pontos é', distância)
#4.	Elabore o programa que simule uma calculadora com as quatro operações aritméticas básicas. O usuário fornecerá dois números e a operação aritmética desejada
#Mostre o menu com estes símbolos (+ , - , * , / ) para o usuário escolher a operação aritmética. 
# Utilize o comando “se . . . senão . . . ” encadeado, ou seja, “if . . . else . . . ” encadeado. 
número1=float(input('Digite o primeiro número:'))
número2=float(input('Digite o segundo número:'))
operação=str(input('Digite a operação:( +,-,*,/ ) '))
if operação == '-': 
 print('o resultado é',número1-número2)
elif operação == '+':
 print('o resultado é', número1+número2)
elif operação == '*':
 print('o resultado é',número1*número2)
elif operação == '/':
 print('o resultado é', número1/número2)
else:
 print('operação inválida')
