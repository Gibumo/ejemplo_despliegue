import time

def contar(inicio=1, fin=50, espera=30):
    for i in range(inicio, fin + 1):
        print(i, flush=True)
        if i < fin:  # no espera después del último número
            time.sleep(espera)


def main():
    print("Iniciando conteo...", flush=True)
    contar(1, 50, 30)
    print("Conteo terminado.", flush=True)


if __name__ == "__main__":
    main()