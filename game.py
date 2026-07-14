ALL_PINS = 10
FRAMES_PER_GAME = 10


class Game:
    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        total = 0
        roll_index = 0
        for _ in range(FRAMES_PER_GAME):
            if self._rolls[roll_index] == ALL_PINS:
                total += ALL_PINS + self._rolls[roll_index + 1] + self._rolls[roll_index + 2]
                roll_index += 1
            elif self._rolls[roll_index] + self._rolls[roll_index + 1] == ALL_PINS:
                total += ALL_PINS + self._rolls[roll_index + 2]
                roll_index += 2
            else:
                total += self._rolls[roll_index] + self._rolls[roll_index + 1]
                roll_index += 2
        return total
