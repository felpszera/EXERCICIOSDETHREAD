"""
Crie um programa em Python que utilize para imprimir sequências numéricas diferentes:
Thread-1 deve imprimir os números de 1 a 10.
Thread-2 deve imprimir os números de 50 a 60.
Utilize time.sleep() para simular tempo de processamento.
Garanta que o programa só finalize após ambas terminarem.
Comente o máximo possível no código, explicando os detalhes de cada ponto.
Entregar um arquivo em formato .py por meio de repositório GitHub.
"""


import threading #importa a biblioteca threading para trabalhar com threads
import time #importa a biblioteca time para usar sleep

# Função que será executada pela thread-1
def x ():
    # Laço de repetição que vai de 1 até 10
    for i in range(1, 11):
        print(f"Thread-1: {i}") #imprime o número de 1 a 10
        time.sleep(0.5) #pausa de 0,5s entre cada numero impresso que simula tempo de processamento


t1 = threading.Thread(target=x) # Cria a primeira thread e associa a função x.
t1.start() # inicia a execução da primeira thread.
t1.join() #aguarda a execução do laço para continuar o código.

# Função que será executada pela thread-2
def y ():
    # Laço de repetição que vai de 50 até 60
    for i in range(50, 61):
        print(f"Thread-2: {i}") #imprime o número de 50 até 60
        time.sleep(0.5) #pausa de 0,5s entre cada numero impresso que simula tempo de processamento


t2 = threading.Thread(target=y) # Cria a primeira thread e associa a função y.
t2.start() # inicia a execução da primeira thread.
t2.join() #aguarda a execução do laço para continuar o código.

print("Thread1 finalizada!") #mostra que a thread 1 foi finalizada
print("Thread2 finalizada!") #mostra que a thread 2 foi finalizada

print("Programa finalizado!") #mostra que o programa foi finalizado
    
