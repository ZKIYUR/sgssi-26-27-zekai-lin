"""Ataque de fuerza bruta contra el cifrado César.

Prueba las 26 claves posibles sobre un mensaje cifrado y elige la que produce
texto en castellano.

Uso: python3 cesar.py [mensaje cifrado]
Si no se indica mensaje, se usa el del enunciado del laboratorio.
"""
import sys

MENSAJE_LABORATORIO = "Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb"

# Palabras frecuentes del castellano, usadas para puntuar cada candidata.
PALABRAS = {
    "de", "la", "el", "en", "y", "que", "los", "un", "una", "con", "por",
    "las", "del", "se", "su", "al", "lo", "es", "no", "para", "como", "pero",
    "sus", "le", "ya", "este", "esta", "sin", "sobre", "hay", "nos", "todo",
    "desde", "entre", "muy", "mas", "porque", "cuando",
}


def descifrar(texto, clave):
    # Solo se desplazan las letras ASCII; el resto de caracteres se copia igual.
    salida = ""
    for c in texto:
        if "a" <= c <= "z":
            salida += chr((ord(c) - ord("a") - clave) % 26 + ord("a"))
        elif "A" <= c <= "Z":
            salida += chr((ord(c) - ord("A") - clave) % 26 + ord("A"))
        else:
            salida += c
    return salida


def puntuacion(texto):
    # Cuenta cuántas palabras del texto están en la lista de palabras frecuentes.
    limpio = "".join(c if c.isalpha() else " " for c in texto.lower())
    return sum(1 for palabra in limpio.split() if palabra in PALABRAS)


def main():
    mensaje = " ".join(sys.argv[1:]) or MENSAJE_LABORATORIO
    mejor_clave, mejor_puntos = 0, -1
    for clave in range(26):
        candidato = descifrar(mensaje, clave)
        puntos = puntuacion(candidato)
        print(clave, candidato, "| puntos:", puntos)
        if puntos > mejor_puntos:
            mejor_clave, mejor_puntos = clave, puntos
    print("\nClave más probable:", mejor_clave)
    print("Mensaje:", descifrar(mensaje, mejor_clave))


if __name__ == "__main__":
    main()