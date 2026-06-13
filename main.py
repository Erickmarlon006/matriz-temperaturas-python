horarios = ["Manhã", "Tarde", "Noite", "Madrugada"]
dias = ["Seg", "Ter", "Qua", "Qui", "Sex"]

mapa_temperaturas = [
    [{"Dia": dia, horario: "Indefinido"} for horario in horarios] for dia in dias
]


def ler_temperaturas():
    while True:
        for i in range(len(mapa_temperaturas)):
            for j in range(len(mapa_temperaturas[i])):
                while True:
                    temperatura = float(
                        input(
                            f"Digite a temperatura correspondente ao dia - {mapa_temperaturas[i][j]['Dia']} e horário - {horarios[j]} : "
                        )
                    )
                    if temperatura < -10 or temperatura > 50:
                        print("Temperatura inválida!, Digite um temperatura válida")

                    else:
                        mapa_temperaturas[i][j][horarios[j]] = temperatura
                        break
        break
    mostrar_tabela(mapa_temperaturas)
    medias(mapa_temperaturas)
    consultar(mapa_temperaturas)


def mostrar_tabela(matriz):
    print("Tabela de Temperaturas durante a semana: ")
    print("-------------------------------------")
    for i in range(len(matriz)):
        frase = ""
        print(dias[i])
        for j in range(len(matriz[i])):
            frase += str(matriz[i][j][horarios[j]]) + "ºC" + " | "
        print(frase)


def medias(matriz):

    print(f"Média de temperatura por dia: ")
    print("---------------------")
    for i in range(len(matriz)):
        media_dia = 0
        for j in range(len(matriz[i])):
            media_dia += matriz[i][j][horarios[j]]
        media_dia = media_dia / len(horarios)
        print(f"Média de temperatura de {matriz[i][j]['Dia']} : {media_dia:.2f}")

    print("Média de temperatura por horário:")

    print("---------------------")

    for j in range(len(horarios)):
        media_horario = 0
        for i in range(len(matriz)):
            media_horario += matriz[i][j][horarios[j]]
        media_horario /= len(dias)
        print(f"Média de temperatura da {horarios[j]} : {media_horario:.2f}°C")


def consultar(matriz):
    while True:
        print("Opções de dias para a busca: ")
        print("----------------------------------")
        for i in dias:
            print(f"{i}")
        dia = input("Digite o dia escolhido para fazer a pesquisa: ")
        if dia.capitalize() not in dias:
            print("Dia inválido!, Digite um dia para buscar")
        else:
            break

    while True:
        print("Opções de horários para a busca: ")
        print("----------------------------------")
        for i in horarios:
            print(f"{i}")
        horario = input("Digite o horario escolhido para fazer a pesquisa: ")

        if horario.capitalize() not in horarios:
            print("Horário inválido!, Digite um horário para buscar")
        else:
            break

    indice_dia = dias.index(dia.capitalize())
    indice_horario = horarios.index(horario.capitalize())

    temperatura = matriz[indice_dia][indice_horario][horario.capitalize()]

    print(
        f"Temperatura de {dia.capitalize()} no período da {horario.capitalize()}: {temperatura}°C"
    )


ler_temperaturas()
