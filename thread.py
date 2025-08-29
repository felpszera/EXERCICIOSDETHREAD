"""
Crie um programa em Python que utilize para imprimir sequências numéricas diferentes:
Thread-1 deve imprimir os números de 1 a 10.
Thread-2 deve imprimir os números de 50 a 60.
Utilize time.sleep() para simular tempo de processamento.
Garanta que o programa só finalize após ambas terminarem.
Comente o máximo possível no código, explicando os detalhes de cada ponto.
Entregar um arquivo em formato .py por meio de repositório GitHub.
"""

import threading
import time

def x (nome, inicio, fim):
    for i in range (inicio, fim +1):
        print(f"{nome} -> {i}")
        time.sleep(0.5)

thread1 = threading.Thread(target=x, args=("Thread1", 1, 10))
thread2 = threading.Thread(target=x, args=("Thread2", 20, 30))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Programa finalizado")
