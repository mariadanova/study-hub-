
#1. Elabore o programa que gere e mostre a sequência dos números naturais múltiplis de 3 até 21
print('números naturais múltiplos de 3 até 21')
for i in range(3,24,3):
 print(i)

#2. Elabore o programa que gere a sequência do dobro dos números naturais até 10 na ordem crescente
print('sequência do dobro dos números naturais até 10')
for i in range(0,12,2):
  print(i)

#3. Implemente o programa que gere a sequência dos números naturais na ordem decrescente até o valor 0
#e o valor inicial será fornecido (digitado) pelo usuário. Mostre também a quantidade de valores da sequência gerada
ct=0
valor=int(input('Digite um valor:'))
for i in range(valor,-1,-1):
  ct+=1
  print(i)
print('quantidade de valores gerados:',ct)

#4.mplemente o programa que gere a sequência dos números naturais na ordem decrescente até o valor 0
#e o valor inicial será fornecido (digitado) pelo usuário. Mostre também a quantidade de valores da sequência gerada
ct=0
valor=int(input('Digite um valor:'))
for i in range(valor,-1,-1):
  ct+=1
  print(i)
print('quantidade de valores gerados:',ct)