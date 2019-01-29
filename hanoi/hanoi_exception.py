
class HanoiException(Exception):
    """
    Custom exception for the Hanoi game. To be used as is, to be able to identify an exception raise by Hanoi's
    game code.
    """
    pass

#Excepcions:
#IndexError (s'intenta accedir a una posició d'una llista inexistent)
#KeyError (s'accedeix a la clau d'un diccionari que no hi és)
#Keyboardinterrupt (L'execució del programa s'atura per un Ctrl+C)
#ImportError (error introduint un altre fitxer)
#MemoryError (el prorama s'ha quedat sense memòria)
#TypeError (operació aplicada a una variable que de tipus incorrecte)
#ZeroDivisionError (divisió per 0)
#NameError (s'utilitza una variable que no existeix)

#if ndiscs < 0:
    #raise HanoiException ("Introdueixi un nombre major que 0")

#Representades així:
#while True:
    #try:
        #x = int(input("Introdueix un nombre"))
    #except ValueError:



