import time

def calcular_fn(n):
    resultado = 1
    for i in range(n):
        resultado *= n
    return resultado

# Ejemplo de uso
n = 5
start = time.perf_counter()
resultado_fn = calcular_fn(n)
end = time.perf_counter()
tiempo_total = end - start
print(f"usando programacion sincrona el tiempo fue de: {tiempo_total}")
print(resultado_fn)