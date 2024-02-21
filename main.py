def criar_conta(numero, titular, saldo, limite):
    conta = {
        "numero" : numero,
        "titular" : titular,
        "saldo" : saldo,
        "limite" : limite
    }
    return conta
def depositar(conta, valor):
    conta ["saldo"] += valor
def sacar(conta, valor):
    conta ["saldo"] -= valor
def imprimir_extrato(conta):
    print("Seu extrato é de {}".format(conta["saldo"]))
conta1 = {
        "numero" : 321,
        "titular" : "cleber",
        "saldo" : -10000,
        "limite" : 1000
    }
conta2 = {
        "numero" : 123,
        "titular" : "Leeh",
        "saldo" : 9999,
        "limite" : 1000
    }
conta3 = criar_conta(789, "Ciclana", 5000, 10000)
print("Conta 1: ", conta1)
print("Conta 2: ", conta2)
print("Conta 3: ", conta3)

depositar(conta3, 5000) #antes: 5000 depois: 10000
print(conta3["saldo"])
sacar(conta3, 2000) #antes 10000, depois: 80000
print(conta3["saldo"])
imprimir_extrato(conta3)

