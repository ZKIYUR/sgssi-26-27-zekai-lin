"""Cifrado de flujo mediante XOR.

Cifra un mensaje aplicando XOR byte a byte con una clave, descifra el
criptograma con la misma operación, muestra mensaje, clave y criptograma en
hexadecimal y comprueba que el descifrado coincide con el mensaje original.

Uso: python3 xor.py [mensaje clave]
Si no se indican, se usan los datos del enunciado del laboratorio.
"""
import sys

MENSAJE_LABORATORIO = "ATAQUE AL AMANECER"
CLAVE_LABORATORIO = "CLAVE12345678901"


def xor_bytes(datos, clave):
    # Si la clave es más corta que los datos, se repite cíclicamente.
    return bytes(d ^ clave[i % len(clave)] for i, d in enumerate(datos))


def main():
    if len(sys.argv) == 3:
        texto, texto_clave = sys.argv[1], sys.argv[2]
    elif len(sys.argv) == 1:
        texto, texto_clave = MENSAJE_LABORATORIO, CLAVE_LABORATORIO
    else:
        sys.exit("Uso: python3 xor.py [mensaje clave]")

    mensaje = texto.encode("utf-8")
    clave = texto_clave.encode("utf-8")
    if not clave:
        sys.exit("La clave no puede estar vacía")
    if len(mensaje) != len(clave):
        print(f"AVISO: mensaje={len(mensaje)} bytes, clave={len(clave)} bytes; se repite la clave")

    criptograma = xor_bytes(mensaje, clave)
    recuperado = xor_bytes(criptograma, clave)

    print("Mensaje    :", texto, "->", mensaje.hex())
    print("Clave      :", texto_clave, "->", clave.hex())
    print("Criptograma:", criptograma.hex())

    if recuperado != mensaje:
        sys.exit("ERROR: el descifrado no coincide con el mensaje original")
    print("Descifrado correcto:", recuperado.decode("utf-8"))


if __name__ == "__main__":
    main()
