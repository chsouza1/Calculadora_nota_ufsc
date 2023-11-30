def calculadora_notas():
    print("Seja bem-vindo à Calculadora de Nota da UFSC BY da cabeça da minha nomorada kkkkk")
    # Nota da prova
    while True:
        try:
            porcentagem_prova = int(input("Digite qual o modelo de porcentagem da prova *SOMENTE O NUMERO* SEM A (%): "))
            nota_prova = float(input("Digite a nota que obteve na prova atual: "))
            porcentagem_trabalho = int(input("Digite o modelo de porcentagem dos trabalho: "))
            nota_trabalho = float(input("Digite qual sua nota no trabalho: "))
            if 0 <= nota_prova or porcentagem_prova or nota_aleatoria or porcentagem_trabalho or nota_trabalho <= 10:
                ## aqui divide a porcentagem que o aluno colocou no começo do programa
                porcentagem_prova /= 100
                ## aqui ele multiplica a nota da prova com a porcentagem dividida.
                nota_prova *= porcentagem_prova
                nota_necessaria = 6.0
                resultado_prova = porcentagem_prova
                print(f"O calculo da sua prova com a porcentagem da materia fica: {resultado_prova:.3f}")

                ##calculo previsto
                nota_aleatoria = float(input("Digite qual a nota mais baixa que voce consegue tirar na prova: "))
                nota_aleatoria *= porcentagem_prova
h

                break
            else:
                print("Favor, digite uma nota válida entre 0 e 10.")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

    print(f"A nota que voce precisa tirar na prova é: {resultado_prova:.3f}")
    print(f"A nota ajustada no trabalho é: {nota_trabalho:.3f}")

# Chama a função principal
calculadora_notas()
