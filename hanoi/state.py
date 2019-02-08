from .hanoi_exception import HanoiException


class State:
    """
    Class for storing and managing Hanoi game states.
    """

    DISC_CHAR = '#'
    NON_DISC_CHAR = '.'
    ROD_CHAR = '|'

    def __init__(self, move_id, depth, moved_disc, source, target, towers, n_discs):
        """
        Initializes a state with all the information needed to represent it in the requested format.

        :param move_id: l'identificador del moviment, conegut com el numero
        :param depth: Profunditat de la recursió de l'estat
        :param moved_disc: El disc mogut per arribar aquest estat. Els discos s'identifiquen pel seu tamany.
        :param source: torres d'on surten els discs moguts
        :param target: torres on van a parar els discs moguts
        :param towers: torres del joc
        :param n_discs: Nombre de discos
        """

        self.move_id = move_id
        self.depth = depth

        self.moved_disc = moved_disc
        self.source = source
        self.target = target
        self.n_discs = n_discs

        self.towers = towers

        # How the towers will be stored? Directly? Is that a good idea?
        raise NotImplementedError()

    def get_tower(self, idx):
        """
        Returns the tower corresponding to the idx (num_torre). Depending on the implementation of the state, this
        method can be invalid. If so, raise an exception and justify it in the report.

        :param idx: Index of the tower.5
        :return: The tower corresponding to the idx.
        """
        return self.towers[idx]

        raise NotImplementedError()

    def __repr__(self):
        """
        Returns a string with the internal representation of the state. This method can be used to represent the state
        information in a different format than the requested.

        MOVIEMENT DE LA REPRESENTACIÓ ÒPTIMA

        :return: A string with the internal representation of the state.
        """


        raise NotImplementedError()

    def __str__(self):
        """
        Returns a string with the representation of the state in the requested format.

        MOVIEMTN MANUAL

        :return: A string with the representation of the state in the requested format
        """
        t1 = self.towers[0].__str__().split('\n')
        t2 = self.towers[1].__str__().split('\n')
        t3 = self.towers[2].__str__().split('\n')

        res = ""
        for i in range(self.n_discs):
            res += t1[i] + ' ' + t2[i] + ' ' + t3[i] + '\n'
        return res 

        raise NotImplementedError()
