import threading
import time

def calcular_fn(n):
    resultado = 1
    lock = threading.Lock()

    def calcular_potencia():
        nonlocal resultado
        potencia = 1
        for _ in range(n):
            potencia *= n
        with lock:
            resultado *= potencia

    threads = []
    for _ in range(n):
        thread = threading.Thread(target=calcular_potencia)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return resultado

# Ejemplo de uso
n = 5
start = time.perf_counter()
resultado_fn = calcular_fn(n)
end = time.perf_counter()
tiempo_total = end-start
print(f"usando multi hilos el tiempo fue de: {tiempo_total}")
print(resultado_fn)
