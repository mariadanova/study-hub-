
#1. Desenvolva um programa que leia vários valores reais e no final mostra as seguintes informações:
#A quantidade de valores digitados;
# A soma dos valores digitados;
#A média aritimética dos valores digitados;
#O maior valor digitados;
#O menor valor digitado;
#E a quantidade de valores digitados maior ou igual a 50.
ct=0
soma=0
maior_valor=-99999
menor_valor= 99999
maiores_50=0
while True:
  numero=float(input('digite alguns números reais:'))
  print('digite 0 para sair')
  if numero==0:
          break
  ct+=1
  soma+=numero
  if maior_valor<numero:
    maior_valor=numero
  if menor_valor>numero:
    menor_valor=numero  
  if numero>=50:
    maiores_50+=1 
  
   
print('quantidade de valores digitados:', ct)
print('soma dos valores digitados:', soma)
print('média aritimética dos valores digitados:', soma/ct)
print('maior valor:', maior_valor)
print('menor valor:', menor_valor)
print('valores maiores ou iguais a 50:', maiores_50)

#2. Escreva o prgrama que leia o salário dos funcionários de uma empresa e calcule quantos ganham menos que cinco
#salários mínimos, quantos estão na faixa de cinco(inclusive) até dez(exclusive) e quantos ganham dez ou mais
#salários mínimos. O valor do salário minímo será fornecido pelo usuário. Na tela de saída,álem da quantidade 
#de funcionários em cada faixa salarial, informe também o valor total da folha de pagamento da empresa.

funcionarios1=0
funcionarios2=0
funcionarios3=0
soma=0
salario_minimo=int(input('qual o valor do salário mínimo?'))
while True:
   salario=int(input('Qual o valor do salário?'))
   print('Digite 0 para sair')
   if salario==0:
      break
   soma+=salario
   if salario<salario_minimo*5:
    funcionarios1+=1
   elif salario>=salario_minimo*5 and salario<salario_minimo*10:
      funcionarios2+=1
   else:
     funcionarios3+=1

print(' quantidade de funcionários que ganham menos que 5 salários mínimos:', funcionarios1) 
print(' quantidade de funcionários que ganham entre 5(inclusive) até 10(exclusive) salários mínimos: ', funcionarios2)  
print(' quantidade de funcionários que ganham 10 ou mais salários mínimos: ', funcionarios3)   
print('folha de pagamento da empresa: ',soma )

