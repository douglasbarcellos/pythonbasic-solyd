'''
EXERCICIO: Crie um software de gerenciamento bancário
Esse software poderá ser capaz de criar clientes e contas
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar_saldo
'''

from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Doug', '123.456.789-10', 30)


conta_do_doug = Conta(cliente1, 10.50, 1000)

print(conta_do_doug.cliente.nome, conta_do_doug.consulta_saldo())

conta_do_doug.depositar(1000.40)

print(conta_do_doug.consulta_saldo())

conta_do_doug.sacar(500)

print(conta_do_doug.consulta_saldo())

conta_do_doug.sacar(1000)

print(conta_do_doug.consulta_saldo())
