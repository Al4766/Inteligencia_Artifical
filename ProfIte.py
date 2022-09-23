

from asyncio.windows_events import NULL


def bpi(origen, objetivo):
    prof = 0
    while x:
        res = bpl(origen, objetivo, prof)
        if res == objetivo:
            return res
        prof += 1

def bpl(nodo, objetivo, prof):
    if prof == 0 and nodo == objetivo
        return nodo
    if prof > 0:
        for hijo in expandir(nodo):
            res = bpl(hijo, objetivo, prof-1)
            if res is not NULL:
                return res
        return NULL
        