from abc import ABC, abstractclassmethod


class Pessoa:
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade
        
        
class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None
        
    def inserir_conta(self, conta):
        self.conta = conta

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        self.status()
        
    def status(self):
        print()
        print(f'Agência {self.agencia}')    
        print(f'Conta {self.conta}')    
        print(f'Saldo {self.saldo}')  
        print()  
        
    @abstractclassmethod
    def sacar(self, valor):
        pass
        
        
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo > 0:
            self.saldo -= valor
        else:
            print('Você não tem saldo suficiente')
        self.status()
        
class ContaCorrente(Conta):
    def sacar(self, valor , limite = 1000):
        self.saldo -= valor
        if self.saldo < limite:
            if self.saldo < 0:
                print(f'Você tem um saldo negativo de {self.saldo}')        
            self.status()
        else:
            print('Você ultrapassou o limite de saque permitido pelo banco! ')
            return

class Banco:
    def __init__(self):
        self.agencias = [112,323,556]
        self.contas = []
    
    
    def inserir_conta(self, conta):
        self.contas.append(conta)
        
    def verificador(self, cliente):  
        if cliente.conta not in self.contas:
            return False
        if cliente.conta.agencia not in self.agencias:
            return False

        return True
        

banco = Banco()

cliente1 = Cliente('Luiz', 30)
cliente2 = Cliente('Maria', 18)
cliente3 = Cliente('João', 50)

conta1 = ContaPoupanca(112, 989136, 0)
conta2 = ContaCorrente(399, 989137, 0)
conta3 = ContaPoupanca(556, 989138, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)


banco.inserir_conta(conta1)
banco.inserir_conta(conta2)


if banco.verificador(cliente1):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(200)
else:
    print('Cliente não autenticado.')
    
if banco.verificador(cliente2):
    cliente2.conta.depositar(58)
    cliente2.conta.sacar(300)
else:
    print('Cliente não autenticado.')
