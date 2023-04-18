import random

def jogo(*jogador):
    #variável de controle para controlar o while loop e não cair no loop infinito
    c=0

    while c!=6:
        
        c+=1
        '''a cada iteração conta uma unidade
        que representa a quantidade de vezes que
        o jogador jogou.
        proporcional a quantidade de vezes de 
        chances.
        '''
        
        #note que temos 2 variáveis, essa se chama tempo jogador(tj)
        tj=6
        ''' representa a contagem de vezes que o 
        jogador tentou, ele contas as chances.
        '''
        
        jogador=int(input('selecione seu número(inteiro, limite:1,5):'))
        
        n=random.randint(1,10)
        
        #if verifica se o valor inserido é igual a n(numero) para vencer
        if jogador == n: 
            
         print('voce venceu') 
         
         break        
        
        #verifica as chances de vezes tentada
        elif tj == c:

         print('voce perdeu')
        
        #verifica vezes jogadas(tentativa)
        elif jogador != n:  
           
         print(f' {c} tentativa' )
        
         
jogo()