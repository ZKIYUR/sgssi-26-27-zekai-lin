"""Ataque al cifrado por sustitución simple mediante análisis de frecuencias.

Cuenta las letras del criptograma, propone una clave inicial a partir de las
frecuencias del castellano y permite corregirla de forma interactiva hasta
que el texto descifrado sea legible.

Uso: python3 sustitucion.py [archivo con el criptograma]
Si no se indica archivo, se usa el criptograma del enunciado del laboratorio.
Órdenes: LETRA=letra (asigna una letra), tabla (muestra la clave), Enter (sale).
"""
import sys
from collections import Counter

CIFRADO_LABORATORIO = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.

AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."""

# Letras del castellano de más a menos frecuente (tabla del enunciado).
ORDEN_ES = "eaolsndruitcpmyqbhgfvjñzxkw"


def descifrar(texto, clave):
    # Las letras sin asignar se dejan como están; el resto de caracteres no cambia.
    return "".join(clave.get(c, c) if c.isalpha() else c for c in texto)


def clave_inicial(texto):
    # Las mayúsculas y minúsculas se cuentan por separado: son símbolos distintos.
    cuentas = Counter(c for c in texto if c.isalpha())
    ranking = [letra for letra, _ in cuentas.most_common()]
    return dict(zip(ranking, ORDEN_ES)), cuentas


def asignar(clave, cifrada, plana):
    # Si otra letra cifrada ya usaba esa letra clara, se intercambian para no repetirla.
    otras = [k for k, v in clave.items() if v == plana and k != cifrada]
    for otra in otras:
        if cifrada in clave:
            clave[otra] = clave[cifrada]
        else:
            del clave[otra]
    clave[cifrada] = plana


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as archivo:
            cifrado = archivo.read()
    else:
        cifrado = CIFRADO_LABORATORIO

    clave, cuentas = clave_inicial(cifrado)
    print("Frecuencias del criptograma:", " ".join(f"{l}:{n}" for l, n in cuentas.most_common()))

    while True:
        print("\n" + descifrar(cifrado, clave))
        try:
            orden = input("\nCambio (ej. X=e), 'tabla' o Enter para salir: ").strip()
        except EOFError:
            break
        if not orden:
            break
        if orden == "tabla":
            for cifrada in sorted(clave):
                print(cifrada, "->", clave[cifrada])
            continue
        partes = [parte.strip() for parte in orden.split("=")]
        if len(partes) != 2 or len(partes[0]) != 1 or len(partes[1]) != 1:
            print("Formato: LETRA=letra")
            continue
        asignar(clave, partes[0], partes[1].lower())


if __name__ == "__main__":
    main()
