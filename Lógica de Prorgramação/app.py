print ('hello word')
print('alo mundo! \
um bom dia!') #é possível ultilizar uma função print quebrando-a em duas linhas 
(valor1)= 10 #coisas que eu aprendi na aula de lógica de programação e outras
print(valor1)# mas é mais lógica mesmo, porque talvez as outras eu não mexa muito com python
(valor2)=20
print(valor2)
('valor1+valor2')
print('valor1+valor3')
print('lista de compras') #não esquecer do apóstrofe e dos parenteses 
print('lista de compras: \n \n arroz \n feijão \n macarrão') #tudo dentro dos parenteses e apóstrofe 
#não esquecer de \n é diferente de /n, é \n não barra inversa n
#('bica d' água') da erro, mas(''bica d' água') não da erro, por isso é possível usar aspas 
#simples e dupla, isso é chamado de programação literal
#não esquecer o Ctrl+S para salvar
# não ta funcionando as aspas duplas, não sei porque, tenho que ver isso depois 
print(345)
print(12+5*9)
print((12+5)*9)
print('12+5*9=',12+5*9)#não esquecer da vírgula 
print('12+5*9=',57)#dois jeitos de escrever a mesma coisa 
print(12+4,4*9,67-12*2)
print(2+2-2*2+(2-2*(2+2)))
print(12/5)#não confundir / com \
print (12.5/2) #observar a diferença entre as duas expressões 
print (12,5/4)
(valor4)=15 # o valor do valor4 deve ser indicado por igual e fora do parenteses 
print(valor4)
(valor5)=18
valor6=(valor5+valor4)
print(valor6)#quando for escrever que um valor x é igual a soma, subtração, multiplicação de outros valores 
#escrever ele na frente, exatamente como está aqui 
valorx=10+4
print(valorx)
valory=2*valorx
print(valory)
amor=valorx*valory# obs: a variável amor é só um nome qualquer, poderia se chamar soma
print(amor)# e a operação ser uma multiplicação
valorw=1 #diferentes valores em diferentes momentos de tempo, a medida que são acrescentadas coisas no valorw
print(valorw)
valorw=1+amor 
print(valorw)
valorw=amor+valorx+valory
print(valorw)
x=3
print(x) #nesse caso, eu só quis demonstrar que a variável pode ser qualquer coisa 
idade_do_cliente=18#i don´t know about you, but i am feeling 22
print(idade_do_cliente)# nesse caso, meu objetivo é demonstrar que o nome da variável
#pode ser mais de uma palavra se unida com _ ´´idade_do_cliente´´
"bica d'água" # para digitar aspas duplas é shift+""(a tecla de aspas)
nome_do_cliente='Elisa' #para digitar valores textuais é necessário colocar aspas
print('Elisa') # o identificador não pode iniciar com um digito exemplo: 123Michelle
import keyword
print(keyword.kwlist)
#tipos de variáveis 
variável1=10
print(type(variável1))
variável1=2.45
print(type(variável1))
variável1=1+3j
print(type(variável1))
#operações aritiméticas 
print(15/3) #divisão #não confundir divisão com divisão inteira  
print(15//3) #divisão inteira #a divisão inteira ignora as casas decimais 
print(10//6) 
print(10/6)
print(7% 3) # resto da divisão inteira 
print(2**2) #potenciação
x1=31827
y1=87
print(x1, '//', y1,'=', x1//y1) #não esquecer a vírgula
print ('x1//y1,=', x1//y1) # aqui é mostrado x1 e y1 de forma literal
print (x1, '//', y1, '=', x1%y1)
x2=45
x3=14
x4= 45 //14
print(x4)
x4=x3% x4
x3=10
print(x4)
#função format 
print('{0}// {1} ={2}'.format (x2,x3,x4))
a="x"
b="y"
a1='a'
b1='b'
c1='c' 
d='z' #não esquecer das aspas 
print("{0} e {1} são a e b".format(a,b)) #a função format só deixa usar valores que já existem, sem criar novos valores 
print ("total: {0}+{1}".format(a,b))
print("{0}, {1} e {2} 'são números inteiros' ".format(a1,b1,c1))
print ("{0} +0 ={0}".format (d))
dia='22'
mês='8'
ano='2007'
print('{0}/{1}/{2}'.format(dia,mês,ano))
#x=int(input('Qual o valor de x?')) #int para números inteiros
y=int(input('Qual o valor de y?'))
print('divisão=', x//y)
print('resto=', x% y)
dividendo=float(input('Qual o valor do dividendo?')) #float para números inteiros ou quebrados
divisor=float(input('Qual o valor do divisor?'))
print('divisão=', x//y) #deu algo errado
print('rest=', x%y)
a=float(input('Qual o valor de a?'))
b=float(input('Qual o valor de b?'))
c=float(input( 'Qual o valor de c?'))
print('média dos valores=', (a+b+c)/3)
número_inteirox=float(input('Qual o número inteito?'))
print('resultado=', número_inteirox**3)
x=float(input('Qual o número?')) #lembrar de colocar parenteses na divisão, para primeiro fazer a divisão, depois a potenciação
print('resultado=', x** 1/3)
x0=float(input('Qual o valor de x0?'))
n=float(input('Qual o valor de n?'))
x0=float(input('Qual o valor de x0?'))
n=float(input('Qual o valor de n?'))
print('resultado=',x0**(1/n))
x=float(input('Qual o número?')) #não consegui 
print('resultado=', x** (1/3))
largura=float(input('Qual o valor da largura?'))
altura=float(input('Qual o valor da altura?'))
comprimento=float(input('Qual o valor do comprimento?'))
print('área da sala=', largura*comprimento)
print('volume da sala=', altura*comprimento*largura)
print('área das paredes da sala=', 2*altura*largura+2*altura*comprimento)