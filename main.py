import time

from game import Game, Point


def main():
    g = Game()
    g.read_input("testcases/test01.txt")

    g.describe()

    while True:
        start = time.time()

        action = Point(8250, 4500)
        score = g.play_action(action)

        print(f"Score: {score}")

        g.describe()

        end = time.time()
        print(f"Time: {end - start}")

        if g.is_game_over() or g.is_victory():
            break


if __name__ == "__main__":
    main()
