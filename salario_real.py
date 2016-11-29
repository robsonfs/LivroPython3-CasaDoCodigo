salario = int(input('salario? '))
imposto = 27.

def get_real_value(salario, imposto):
    imposto /= 100
    return salario * (1 - imposto)

while imposto > 0:
    imposto = input("Imposto ou (0) para sair: ")
    imposto = float(imposto) if imposto else 27.
    if imposto == 0:
        print("Finalizando a execução do programa")
        break
    print("Valor real: {0}".format(get_real_value(salario, imposto)))
