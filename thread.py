"""
Crie um programa em Python que utilize para imprimir sequências numéricas diferentes:
Thread-1 deve imprimir os números de 1 a 10.
Thread-2 deve imprimir os números de 50 a 60.
Utilize time.sleep() para simular tempo de processamento.
Garanta que o programa só finalize após ambas terminarem.
Comente o máximo possível no código, explicando os detalhes de cada ponto.
Entregar um arquivo em formato .py por meio de repositório GitHub.
"""

import threading #importa biblioteca
import time #importa biblioteca

def x (nome, inicio, fim): #cria uma função X
    for i in range (inicio, fim +1): #cria um laço de repetição para incrementar de 1 em 1
        print(f"{nome} -> {i}") #imprime o nome e o incremento a cada repetição
        time.sleep(0.5) #o tempo de uma repetição para outra é de 0.5 segundos

thread1 = threading.Thread(target=x, args=("Thread1", 1, 10)) #cria a thread1 e relaciona o laço de repetição a ela, e ainda informa o inicio e o fim da contagem.
thread2 = threading.Thread(target=x, args=("Thread2", 50, 60)) #cria a thread2 e relaciona o laço de repetição a ela, e ainda informa o inicio e o fim da contagem.

thread1.start() #inicia a thread1
thread2.start() #inicia a thread1

thread1.join() #finaliza thread1
thread2.join() #finaliza a thread2

print("Programa finalizado") #imprime mensagem que finaliza o programa


