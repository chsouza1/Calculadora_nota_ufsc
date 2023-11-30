def calculadora_notas():
    print("Seja bem-vindo à Calculadora de Nota da UFSC BY da cabeça da minha nomorada kkkkk")
    # Nota da prova
    while True:
        try:
            porcentagem_prova = float(input("Digite qual o modelo de porcentagem da prova *SOMENTE O NUMERO* SEM A (%): "))
            nota_prova = float(input("Digite a nota que obteve na prova atual: "))
            porcentagem_trabalho = float(input("Digite o modelo de porcentagem dos trabalho: "))
            nota_trabalho = float(input("Digite qual sua nota no trabalho *SOMENTE O NUMERO* SEM A (%): "))
            if 0 <= nota_prova <= 10 and 0 <= porcentagem_prova <= 100 and 0 <= nota_trabalho <= 10 and 0 <= porcentagem_trabalho <= 100:
                break
                ## aqui divide a porcentagem que o aluno colocou no começo do programa
                porcentagem_prova /= 100
                ## aqui ele multiplica a nota da prova com a porcentagem dividida.
                calculo_nota = nota_prova * porcentagem_prova
                nota_necessaria = 6.0
                resultado_prova = calculo_nota
                ## calculo do trabalho
                porcentagem_trabalho /= 100
                calculo_trabalho = nota_trabalho * porcentagem_trabalho
                resultado_trabalho = calculo_trabalho
                print(f"O calculo da sua prova com a porcentagem da materia fica: {resultado_prova:.3f}")
                print(f"O calculo da seu trabalho com a porcentagem da materia fica: {resultado_trabalho:.3f}")

                ##calculo previsto
                nota_aleatoria = float(input("Digite qual a nota mais baixa que voce consegue tirar na prova: "))
                calculo_aleatoria = nota_aleatoria * porcentagem_prova
                calculo_completo = calculo_aleatoria + resultado_trabalho + resultado_prova
                print(f"Essa é a sua nota calculando tudo: {calculo_completo:.2f}")
            else:
                print("Favor, digite uma nota válida entre 0 e 10.")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

# Chama a função principal
calculadora_notas()
