import glob

from game import Game, Point


def main():

    totalscore = 0

    for file in glob.iglob("testcases/*.txt"):
        g = Game()
        g.read_input(file)
        # g.describe()

        while True:
            action = Point(8250, 4500)
            is_over = g.play_action(action)

            if is_over:
                totalscore += g.score
                break
        print(file, g.score)

    print(totalscore)


if __name__ == "__main__":
    main()
