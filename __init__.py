from hanoi.hanoi import HanoiGame
from hanoi.hanoi_exception import HanoiException
from hanoi.tower import Tower

if __name__ == '__main__':
    try:
        hanoiGame = HanoiGame(-1)
        assert (False)

    except HanoiException:
        pass