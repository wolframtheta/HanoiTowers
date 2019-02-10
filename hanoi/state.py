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

        :param move_id: Identifier of the move. Ideally, the step number.
        :param depth: Recursion depth at which this state is generated.
        :param moved_disc: The disc moved to reach this state. Ideally, a disk is defined just by its size.
        :param source: Tower from which the disc is moved.
        :param target: Tower to which the disc is moved.
        :param towers: Towers of the game.
        :param n_discs: Number of discs of the game.
        """

        self.move_id = move_id
        self.depth = depth

        self.moved_disc = moved_disc
        self.source = source
        self.target = target
        self.n_discs = n_discs
        #
        self.towers = []
        for x in towers:
            self.towers.append(x.as_list())
        #
        # # How the towers will be stored? Directly? Is that a good idea?
        # raise NotImplementedError()

    def get_tower(self, idx):
        """
        Returns the tower corresponding to the idx. Depending on the implementation of the state, this method can be
        invalid. If so, raise an exception and justify it in the report.

        :param idx: Index of the tower.
        :return: The tower corresponding to the idx.
        """

        return self.towers[idx]

    def __repr__(self):
        """
        Returns a string with the internal representation of the state. This method can be used to represent the state
        information in a different format than the requested.

        :return: A string with the internal representation of the state.
        """
        raise NotImplementedError()

    def __str__(self):
        """
        Returns a string with the representation of the state in the requested format.

        :return: A string with the representation of the state in the requested format
        """
        res = ""
        if self.move_id != None:
            res = "\nMove id " + str(self.move_id) + " Rec Depth " + str(self.depth) + '\n' + "Last move: " \
                  + str(self.moved_disc) + " Disk, from " + str(self.source) + " to " + str(self.target) + '\n'

        for i in range(self.n_discs - 1, -1, -1):
            res += (print_line(self.n_discs, self.towers[0][i] if len(self.towers[0]) > i else 0) + ' ' +
                    print_line(self.n_discs, self.towers[1][i] if len(self.towers[1]) > i else 0) + ' ' +
                    print_line(self.n_discs, self.towers[2][i] if len(self.towers[2]) > i else 0) + '\n')
        res += "Tower 1".center((self.n_discs * 2) + 1) + ' ' + "Tower 2".center((self.n_discs * 2) + 1) + ' ' \
               + "Tower 3".center((self.n_discs * 2) + 1) + '\n'
        return res

def print_line(n_discs, actual):
    return State.NON_DISC_CHAR * (n_discs - actual) + (State.DISC_CHAR * actual) + State.ROD_CHAR + (actual * State.DISC_CHAR) + State.NON_DISC_CHAR * (n_discs - actual)
