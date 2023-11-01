from game import Game, Point


def test_simple():
    g = Game()
    g.read_input("testcases/test01.txt")

    turns = 0
    while True:
        action = Point(8250, 4500)
        is_over = g.play_action(action)

        turns += 1

        if is_over:
            break

    assert turns == 9
    assert g.score == 10
