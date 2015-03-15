import random


def hallo_welt():
    print "hallo Welt aus funktion"
    return True


def wuerfel():
    return random.randint(1, 6)


hallo_welt()
print wuerfel()
