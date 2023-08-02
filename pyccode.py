# -*- coding: utf-8 -*-
iniciar = '' #variável para iniciar a calculadora ou encerrá-la
num1 = 0.00 #número 1
num2 = 0.00 #número 2
contador = 0 #define número da operação sendo realizada, acumulativo
operacao = 0 #variável para armazenar número da operação sendo realizada
nova = '' #Identifica se usuário quer realizar nova operação (S) ou não (N)
while True: #confere se o usuário quer iniciar a calculadora
  iniciar = input('Iniciar Calculadora? [S/N]: ')
  if iniciar == 'S':
    break
  elif iniciar == 'N':
    print('Encerrando Calculadora.')
    break
  else:
    print('Opção Inválida!')
    continue
while iniciar != 'N': #código para inserir números e realizar operações, apenas executado quando iniciar for diferente de N
  print('===============================================================')
  contador = contador + 1 #define número da operação sendo realizada e acrescenta +1 toda vez que o loop reinicia
  print('Operação Nº' , contador)
  try: #condição try p/ verificar se valores digitados nos inputs abaixo são válidos
    num1 = float(input('Número 1: '))
    num2 = float(input('Número 2: '))
  except ValueError:
    print('Utilize Apenas Números.')
    continue
  print('===============================================================')
  print('1 - ADIÇÃO || 2 - SUBTRAÇÃO\n'
  '3 - MULTIPLICAÇÃO || 4 - DIVISÃO\n'
  '5 - EXPOENTE || 6 - RESTO\n'
  '7 - RAIZ QUADRADA || 8 - REDEFINIR NÚMEROS\n'
  '9 - SAIR')
  try: #condição try p/ verificar se valor digitado no input abaixo é válido (value error resulta na operação sendo reiniciada)
    operacao = int(input('Digite o Número da Operação a Ser Realizada: '))
  except ValueError:
    print('Favor Digitar Apenas Número da Operação.')
    continue
  #if do 1 ao 7 executa as operações correspondentes com os números inseridos pelo usuário
  if operacao == 1:
    print('Resultado da Adição: ' , num1 + num2)
  elif operacao == 2:
    print('Resultado da Subtração: ' , num1 - num2)
  elif operacao == 3:
    print('Resultado da Multiplicação: ' , num1 * num2)
  elif operacao == 4:
    print('Resultado da Divisão: ' , num1 / num2)
  elif operacao == 5:
    print('Resultado do Expoente: ' , num1 ** num2)
  elif operacao == 6:
    print('Resultado do Resto: ' , num1 % num2)
  elif operacao == 7:
    print('Resultado Raiz Quadrada: ' , num1 + num2 ** (1/2))
  elif operacao == 8: #reinicia calculadora para inserir os números novamente (conta como nova operação)
    print('Conta Descartada.')
    continue
  elif operacao == 9: #encerra a calculadora
    print('Encerrando Calculadora.')
    break
  else:
    print('Operação Não Reconhecida.')
    continue
  nova = input('Realizar Nova Operação? [S/N]: ')
  if nova == 'S': #reinicia loop para nova operação com novos valores definidos pelo usuário
    continue
  elif nova == 'N':
    print('Encerrando Calculadora.')
    break
  else:
    print('Opção Inválida!')
    continue
