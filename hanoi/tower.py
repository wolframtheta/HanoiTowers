from .hanoi_exception import HanoiException


class Tower:
    """
    Class for storing and managing Hanoi game towers.
    """

    def __init__(self, ndiscs):             #ndiscs = numero de discs totals que caben a la torre, discs = discs que hi ha actualment
        """
        Initializes the tower.
        """
        self.discs = []
        self.ndiscs = ndiscs

    def is_empty(self):
        """
        Returns if a tower is empty or not, it is, if the tower has no discs.

        :return: True if is empty, it is, if the tower has no discs, False otherwise
        """
        if len(self.discs) == 0:
            return True
        else:
            return False


    def size(self):
        """
        Returns the size (number of discs) of the tower.

        :return: The size (number of discs) of the tower.
        """
        return len(self.discs)


    def pop_disc(self):
        """
        Removes a disc from the top of the tower and returns it.
        Raises an HanoiException if the tower is empty.

        :return: The disc removed from the top of the tower.
        """
        if len(self.discs) == 0:
            raise HanoiException ("No hay ningun disco en esta torre!")
        return self.discs.pop

    '''
        Inserta un disco encima de la torre.
    '''
    def push_disc(self, disc):
        """
        Adds a dis to the top of the tower.
        Raises an HanoiException if the disc is bigger that the disc at the top of the tower.

        :param disc: The disc to be added to the top of the tower.
        """
        if len(self.discs) > 0 and self.discs[-1] < disc:
            raise HanoiException ("El disco es mayor!")
        return self.discs.append(disc)


    def as_list(self):
        """
        Returns the discs of the tower as a new list (it means that if the internal representation of the tower is a
        list, it should return a copy of it).

        :return: A list containing the discs of the tower.
        """
        return self.discs.copy


    def __repr__(self):
        """
        Returns a string with the internal representation of the tower. This method can be used to represent the tower
        information in a different format than the requested.

        :return: A string with the internal representation of the state.
        """

        return ",".join(str(x) for x in self.discs)                       #posa una coma entre cada element i ho ajunta "juntame este array y pon esto en medio"


    def __str__(self):
        """
        Returns a string with the representation of the state in the requested format.

        :return: A string with the representation of the state in the requested format
        """

        lista = []
        for i in range (0, self.ndiscs - len(self.discs)):                #genera ndiscs torres amb punts
                lista.append("."*self.ndiscs + "|" + "."*self.ndiscs)
        for i in range (self.ndiscs - len(self.discs), self.ndiscs):        #genera linies amb i sense discs (#)
            index = -(i - (self.ndiscs - len(self.discs)) + 1)
            lista.append("."*(self.ndiscs - self.discs[index]) + "#"*self.discs[index] + "|" + "#"*self.discs[index] + "."*(self.ndiscs - self.discs[index]))

        return "\n".join(lista)