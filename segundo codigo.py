#O codigo começa te perguntando o dia, caso coloque o dia errado, o codigo repete e mostra a mensagem:"adicione uma data válida".
while True:
 dia = int(input('dia: '))
 if dia >31 or dia<1:
  print('adicione uma data válida')
  continue
 else: break

#Já o mês segue a mesma lógica do dia, mudando apenas a numeração
while True: 
 mês = int(input('mês: '))
 if mês >12 or mês<1:.
  print('adicione um mês válido')
  continue
 else: break

#O ano é diferente dos demais. Miha linha de raciocinio é:"Uma pessoa que nasceu após 2022 não conseguiria responder, porque seria muito nova para isso(levando em conta que estou em 2026),
#enquanto uma pessoa que nasceu em 1902 tem 124 anos, oque é quase impossivel levando em conta que a pessoa mais velha do mundo tinha 122 anos " 
while True:
 ano = int(input('ano: '))
 if ano >2022 or ano <1902:
  print('adicione um ano vàlido')
  continue
 else: break 
 

        
print('você nasceu em:',dia,'/',mês,'/',ano,'certo?')


