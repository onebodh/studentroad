WIP
from datetime import datetime

positivo = ['sim', 'Sim']  # Trying to avoid lowercase inputs to not end the program
msg = ()
data = ()
end = ()

while end not in positivo:
    msg = input('Digite sua mensagem: ')
    data = datetime.today().strftime('%d/%m/%Y')
    dbteste = {msg:data}
    end = input('Deseja finalizar o programa? ')
else:
    print(dbteste)  #todo: include multiple inputs in lib
    exit()
    
