class Conta():
    #função construtura
    def __init__(self, numero, titular, saldo, limite ):
        print("Construindo um Objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__poupanca = 0
    def depositar(self, valor):
        self.__saldo += valor
    def sacar(self,valor):
        self.__saldo -= valor
    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo
    def get_limite(self):
        return self.__limite
    def get_titular(self):
        return self.__titular
    def set_limite(self, valor):
        self.__limite = valor
    def imprimir_extrato(self):
        print("Saldo {} do titular {}.".format(self.get_saldo(), self.get_titular()))
    @property
    def poupanca(self):
        return self.__poupanca
    @poupanca.setter
    def poupanca(self, valor):
        if valor <= 0:
            print(f'Infelizmente não é possível poupar um valor negativo')
        else:
            self.__poupanca = valor
    def __verificar_saque(self, valor):
        if valor < (self.__saldo + self.__limite):
            return True
        else:
            return False
    def sacar(self, valor):
        if self.__verificar_saque(valor):
            self.__saldo -= valor
        else:
            print("---------------------------------------------------------------------")
            print("Infelizmente você não possui saldo e limite para o saque em questão")

conta_cleber = Conta(321, "Cleber", -10000, 100)
conta_leeh = Conta(456, "Leeh", 5000, 1000)
print("---------------------------------------------------------------------")
print(f'Valor da conta poupança:',conta_cleber.poupanca)
print("---------------------------------------------------------------------")
conta_cleber.poupanca = 20
print(f'Valor da conta poupança atualmente:',conta_cleber.poupanca)
print("---------------------------------------------------------------------")

conta_cleber.sacar(1)
conta_leeh.sacar(1)


conta_cleber.depositar(10000)
conta_cleber.imprimir_extrato()
conta_leeh.sacar(3000)
conta_leeh.imprimir_extrato()

conta_cleber.transferir(conta_leeh,1000)
conta_cleber.imprimir_extrato()
conta_leeh.imprimir_extrato()

conta_cleber.set_limite(9999)
print(conta_cleber.get_limite())
print("---------------------------------------------------------------------")
# conta_cleber._Conta__saldo = 1000
# print(conta_cleber._Conta__saldo)