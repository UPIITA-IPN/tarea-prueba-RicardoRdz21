import sys

def sumar_argumentos(n1, n2):
    resultado = int(n1) + int(n2)
    print(resultado)

if __name__ == "__main__":
    # Recibimos los números desde el script de Bash
    sumar_argumentos(sys.argv[1], sys.argv[2])
