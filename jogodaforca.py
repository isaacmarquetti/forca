encontradas = []
secreto = []
digitadas = []

palavra_secreta = 'PYTHON'

for p in palavra_secreta:
    secreto.append("_")

cont = 0
print("------------------------")
print("      JOGO DA FORCA     ")
print("------------------------")


while True:
    print()
    print('A palavra é: ', end='')
    print(' '.join(secreto))
    print(f"Letras digitadas: {' / '.join(digitadas)}")
    letra = input("Digite uma letra: ").upper()

    if not letra.isnumeric() and len(letra) == 1:

        if letra not in palavra_secreta and letra not in digitadas:
            cont += 1
            print(f"-> \033[31mVocê errou pela {cont}ª vez. Tente novamente!\033[0;0m")

        if letra in digitadas:
            print("-> \033[31mVocê já digitou essa letra!\033[0;0m")
        else:
            digitadas.append(letra)
            for pos, char in enumerate(palavra_secreta):
                if char == letra:
                    encontradas.append(pos)
                    secreto.pop(pos)
                    secreto.insert(pos, palavra_secreta[pos])

        if len(palavra_secreta) == len(encontradas):
            print()
            print(f'A palavra secreta é {palavra_secreta}')
            print("Você VENCEU!!! Parabéns !!!")
            break
        elif cont == 7:
            print()
            print("Você PERDEU!!! Tente novamente.")
            break
    else:
        if letra.isnumeric():
            print(f"-> \033[31mDigite apenas letras.\033[0;0m")
        elif letra == '':
            print(f"-> \033[31mVocê precisar digitar algo.\033[0;0m")
        elif letra != 1:
            print(f"-> \033[31mDigite apenas uma letra por vez.\033[0;0m")



