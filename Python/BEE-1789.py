while True:
    try:
        quantidadeLesmas = int(input())
        velocidadesLesmas = input().split(" ")
        nivelLesmaMaisVeloz = 1
        velocidadeLesmaMaisVeloz = 0

        i = 0
        while i < quantidadeLesmas:
            if int(velocidadesLesmas[i]) > int(velocidadeLesmaMaisVeloz):
                velocidadeLesmaMaisVeloz = int(velocidadesLesmas[i])
            i += 1

        if velocidadeLesmaMaisVeloz < 10:
            nivelLesma = 1
        elif velocidadeLesmaMaisVeloz >= 20:
            nivelLesma = 3
        else:
            nivelLesma = 2

        print(nivelLesma)

    except EOFError:
        break