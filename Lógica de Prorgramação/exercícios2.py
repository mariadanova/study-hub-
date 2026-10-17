#1.Desenvolva um programa que leia vários valores reais e no final mostre as seguintes informações:
# A quantidade de valores digitados;
#A soma dos valores digitados;
#A média aritmética dos valores digitados;
#E a quantidade de valores digitados maiores que 20.
quantidade=0
soma=0
maioresque20=0
while True: 
 valor=float(input('Digite um valor: '))
 print('digite 0 para sair')
 if valor==0:
  break
 quantidade+=1
 soma+=valor
 if valor>20:
  maioresque20+=1
print('quantidade de valores digitados:', quantidade) 
print('soma dos valores:', soma) 
print('média dos valores:', soma/quantidade)
print('valores maiores que 20:', maioresque20)

#2. Implemnete um programa que leia a nota de vários alunos de uma turma e gere uma tela de saída com
#as seguintes informações: a quantidade de alunos que fizeram a prova, a quantidade de alunos aprovados 
#A quantidade de alunos reprovados e a média da turma. Considere que o aluno será aprovado ccom nota maior igual a cinco.
quantidade_de_alunos=0
quantidade_de_aprovados=0
quantidade_de_reprovados=0
soma_das_notas=0
while True:
    nota=int(input('Digite a nota:'))
    print('digite -1 para sair')
    if nota ==-1:
         break
    quantidade_de_alunos+=1
    soma_das_notas+=nota
    if nota>=5:
       quantidade_de_aprovados+=1
    if nota<=5:
       quantidade_de_reprovados+=1
print('quantidade de alunos', quantidade_de_alunos)
print('média da turma:', soma_das_notas/quantidade_de_alunos )
print('quantidade de alunos aprovados', quantidade_de_aprovados)
print('quantidade de alunos reprovados', quantidade_de_reprovados)

#3. Construa o programa que calcule a média aritimética dos números pares e a média aritimética dos números
#ímpares. O usuário fornecerá os valores de entrada que pode ser um número qualuqer par ou ímpar. 
# A condição de saída será o número 0. Na tela de saída, mostre também a quantidade de números digitados e a soma total dos números digitados.
quantidade_de_pares=0
soma_dos_pares=0
quantidade_de_impares=0
soma_dos_impares=0
while True:
    número=int(input('Digite um número: '))
    print('Digite 0 para sair')
    if número==0:
        break
    if número%2==0:
        quantidade_de_pares+=1
        soma_dos_pares+=número
    else:
        quantidade_de_impares+=1
        soma_dos_impares+=número
print('média aritimética dos números pares: ', soma_dos_pares/ quantidade_de_pares)
print('média aritimética dos números ímpares:', soma_dos_impares/ quantidade_de_impares)
print('quantidade de números digitados:', quantidade_de_impares+quantidade_de_pares)
print('soma total dos números digitados', soma_dos_impares+soma_dos_pares)
  