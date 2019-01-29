import logging

from .hanoi_exception import HanoiException
from .state import State
from .tower import Tower

logging.basicConfig(level = logging.INFO, format = '%(levelname)-10s  %(message)s')


class HanoiGame:
    """
    Main class for management of the data structures and moves of the game.
    """

    def __init__(self, n_discs, n_towers=3):
        """
        Initializes the game with n_discs and n_towers, which defaults to 3.
        At this step, the game can be solved and stored to consult.

        Raises a HanoiException if n_discs is negative or n_towers is less than 3.

        :param n_discs: Number of disks for this game.
        :param n_towers: Number of towers for this game. Default: 3
        """

        # Steps:
        # 1.- Check the parameters (Add the code after this comment)

        # 2.- Initialize the structure attributes (Add the code after this comment)

        # 3.- Initialize the towers (Add the code after this comment)

        # 4.- Solve and store the optimal solution

        if n_discs < 0:
            raise HanoiException("Number of disks must be positive")
        if n_towers < 3:
            raise HanoiException("Number of towers must be more or equal to 3")

        self.n_discs = n_discs
        self.towers = []
        for i in range(n_towers):
            self.towers.append(Tower(n_discs))

        for i in reversed(range(self.n_discs)):
            self.towers[0].push_disc(i + 1)
        self.states = []
        self.is_finished = False
        # self._solve()

    def get_state(self, step):
        """
        Returns the state at the requested step in the optimal solution.
        Raises a HanoiException if the step index is negative or bigger than the total of states in the optimal
        solution.

        :param step: The step index in the optimal solution.
        :return: The state at the requested step in the optimal solution.
        """

        if step < 0 or step > len(self.states):
            raise HanoiException("Step index negative or bigger than the total of states in optimal solution")
        return self.states[step]
    def get_n_discs(self):
        """
        Returns the number of disks of this game.

        :return: The number of disks of this game.
        """
        return self.n_discs

    def get_n_towers(self):
        """
        Returns the number of towers of this game.

        :return: The number of towers of this game.
        """
        return self.n_towers

    def get_n_states(self):
        """
        Returns the number of states of the optimal solution. Ideally, it should be the size of the structure used to
        store the optimal solution states.

        :return: The number of states of the optimal solution.
        """
        raise NotImplementedError()

    def move(self, source, target, move_id=None, depth=None):
        """
        Moves a disk from source tower to target tower.
        Raises a HanoiException if source and target are the same or if the move is invalid (the disk moved is bigger
        than the last disk in the target tower, the source tower is empty...)

        :param source: Tower from which a disk is going to be moved.
        :param target: Tower to which a disk is going to be moved.
        :param move_id: Identifier of the movement. Useful as information for the optimal state.
        :param depth: Depth of the recursion call. Useful as information for the optimal state.
        :return: The new state generated by the move.
        """

        if source == target or self.towers[target].discs[-1] > self.towers[source].discs[-1] or self.towers[source].is_empty():
            raise HanoiException("Invalid movement")
        self.towers[target].push_disc(self.towers[source].pop_disc())
        self.states.append(move_id)

        return self.states[-1]

    def _solve(self):
        """
        Generates and stores the optimal solution, reinitializing the towers afterwards.
        """
        raise NotImplementedError()

    def _solve_rec(self, n_discs, source, target, aux, depth=0):
        """
        Recursive call to solve the hanoi game optimally.

        :param n_discs: Number of disks to be moved.
        :param source: Tower from which a disk is going to be moved.
        :param target: Tower to which a disk is going to be moved.
        :param aux: Tower to be used as auxiliary.
        :param depth: Depth of the recursion call. Useful as information for the optimal state.
        """
        raise NotImplementedError()

    def print_optimal_state(self, step):
        """
        Prints the optimal state at the selected step in the required format.

        :param step: Step index of the optimal solution.
        """
        raise NotImplementedError()

    def print_optimal_solution(self):
        """
        Prints all the states of the optimal solution in the required format.
        """
        raise NotImplementedError()


    def is_finished(self):
        """
        Checks if the interactive game is finished, returns True if is finished, False otherwise.

        :return: True if the game is finished, False otherwise.
        """
        return self.is_finished

    def get_current_state(self):
        """
        Returns the current state of the game.

        :return: The current state of the game.
        """
        return self.states[-1]

    def __repr__(self):
        """
        Returns a string with the internal representation of the game. This method can be used to represent the game
        information in a different format than the requested.

        :return: A string with the internal representation of the game.
        """
        raise NotImplementedError()

    def __str__(self):
        """
        Returns a string with the representation of the current state of the game in the requested format.

        :return: A string with the representation of the current state of the game in the requested format
        """


        t1  = self.towers[0].__str__().split('\n')
        t2  = self.towers[1].__str__().split('\n')
        t3  = self.towers[2].__str__().split('\n')

        res = ""
        for i in range(self.n_discs):
            res += t1[i] + ' ' + t2[i] + ' ' + t3[i] + '\n'
        return res



