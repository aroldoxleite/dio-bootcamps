saldo = 1000
saque = 200
limite = 100

print(saldo > saque and saque <= limite)
print(saldo > saque or saque <= limite)

print('Lógica do AND')
print(False and False) #false
print(False and True) #false
print(True and True) #true

print('Lógica do OR')
print(False or False) #false
print(False or True) #true
print(True or True) #true