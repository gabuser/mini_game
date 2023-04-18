import random

# == > jogo: Função principal do jog
def jogo(max_tentativas=6, num_min=1, num_max=10):
    '''
        Jogo de adivinhação do número atual aleatório.
        A cada loop é gerado um número aleatório ao qual o usuário (jogador)
        deverá adivinhar numa taxa pré definida nas variáveis `num_min` e `num_max
    '''

    # :: Redefinição (redundância) das variáveis de controle do loop.
    c=0
    max_tentativas = max_tentativas
    num_min = num_min
    num_max = num_max

    # :: Avisa ao jogador com antecedência o número de tentativas
    print(f"Número de tentativas: max_tentativas")

    # :: Início do Loop
    while c < max_tentativas:
        # :: Adição do contador, definição das chances restantes e definição do número aleatório
        c += 1
        tj = max_tentativas
        n = random.randint(num_min, num_max)

        # :: Tratamento de erro ( o loop é quebrado completamente caso o valor não possa ser transformado em inteiro, mas avisa ao usuário (jogador do por que o erro ocorreu) )
        try:
            jogador = input("Selecione seu número entre ({num_min} - {num_max}): ")
            jogador = int(jogador)

        except TypeError:
            print("Não foi possível tranformar em Inteiro. Execute a função novamente")
            break # quebra de loop

        # :: Verificação de valores ( numero igual = vitória; máximo de tentativas = derrota )
        if jogador == n:
         print('Voce venceu! :)')
         break

        elif tj == c:
         print('Voce perdeu! :(')

        if jogador != n:
         print(f' {c} tentativa' )

if __name__ == "__main__":
    jogo()
