from random import randint


def hallo_welt():
    print "hallo Welt aus funktion"
    return True


def wuerfel():
    return randint(1, 6)

anzahl = int(raw_input('wieviele Wuerfel sollen geworfen werde?: '))
i = 0

while i < anzahl:
    i += 1
    print wuerfel()


