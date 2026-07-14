from game import Game


def roll_many(game, pins, times):
    for _ in range(times):
        game.roll(pins)


def test_gutter_game_scores_zero():
    game = Game()
    roll_many(game, 0, 20)
    assert game.score() == 0


def test_all_ones_scores_twenty():
    game = Game()
    roll_many(game, 1, 20)
    assert game.score() == 20


def test_one_spare():
    game = Game()
    game.roll(5)
    game.roll(5)
    game.roll(3)
    roll_many(game, 0, 17)
    assert game.score() == 16


def test_one_strike():
    game = Game()
    game.roll(10)
    roll_many(game, 0, 18)
    assert game.score() == 10


def test_all_spares_scores_150():
    game = Game()
    for _ in range(10):
        game.roll(5)
        game.roll(5)
    game.roll(5)
    assert game.score() == 150


def test_perfect_game():
    game = Game()
    roll_many(game, 10, 12)
    assert game.score() == 300


def test_nine_and_spare():
    game = Game()
    game.roll(9)
    game.roll(1)
    game.roll(3)
    roll_many(game, 0, 17)
    assert game.score() == 16


def test_spare_in_tenth_frame_gets_one_bonus_roll():
    game = Game()
    roll_many(game, 0, 18)
    game.roll(5)
    game.roll(5)
    game.roll(3)
    assert game.score() == 13


def test_strike_in_tenth_frame_gets_two_bonus_rolls():
    game = Game()
    roll_many(game, 0, 18)
    game.roll(10)
    game.roll(3)
    game.roll(4)
    assert game.score() == 17


def test_strike_followed_by_spare():
    game = Game()
    game.roll(10)
    game.roll(5)
    game.roll(5)
    roll_many(game, 0, 16)
    assert game.score() == 30


def test_two_consecutive_strikes():
    game = Game()
    game.roll(10)
    game.roll(10)
    game.roll(3)
    game.roll(4)
    roll_many(game, 0, 14)
    assert game.score() == 47


def test_strike_in_ninth_chains_into_tenth_frame_spare():
    game = Game()
    roll_many(game, 0, 16)
    game.roll(10)
    game.roll(5)
    game.roll(5)
    game.roll(3)
    assert game.score() == 33

