from typing import List

from .unit import Unit
from .point import Point


class Game:
    zombies: List[Unit]
    humans: List[Unit]
    ash: Unit | None
    score: int
    game_over: bool
    game_won: bool

    def __init__(self):
        self.zombies = []
        self.humans = []
        self.ash = None
        self.score = 0
        self.game_over = False
        self.game_won = False

    def read_input(self, testcase: str):
        with open(testcase, "r") as f:
            x, y = map(int, f.readline().split())
            self.ash = Unit(x, y)

            human_count = int(f.readline())
            for _ in range(human_count):
                human_id, human_x, human_y = map(int, f.readline().split())
                self.humans.append(Unit(human_x, human_y))

            zombie_count = int(f.readline())
            for _ in range(zombie_count):
                zombie_id, zombie_x, zombie_y, *_ = map(int, f.readline().split())
                self.zombies.append(Unit(zombie_x, zombie_y))

    def play_actions(self, actions: List[Point]) -> int:
        for action in actions:
            is_over = self.play_action(action)
            if is_over:
                break

        return self.score

    def play_action(self, action: Point) -> bool:
        if action.x < 0 or action.x > 16000 or action.y < 0 or action.y > 9000:
            self.game_over = True
            return True

        for zombie in self.zombies:
            zombie.set_target(self.ash, *self.humans)
            zombie.move_toward(zombie.target, 400)

        self.ash.move_toward(action, 1000)
        self.score += self.ash.kill_zombies(self.zombies, len(self.humans))

        for zombie in self.zombies:
            if zombie.target == zombie:
                zombie.target.kill()

        if self.is_game_over():
            self.score = 0
            return True
        if self.is_victory():
            return True

        return False

    def describe(self):
        print(f"\nGame = {self.score} pts")
        print(f"{len(self.humans)} humans & {len(self.zombies)} zombies")
        print(f"Ash    : ({self.ash.x}, {self.ash.y})")
        for zombie in self.zombies:
            print(f"Zombie : ({zombie.x}, {zombie.y})")
        for human in self.humans:
            print(f"Human  : ({human.x}, {human.y})")

    def is_game_over(self) -> bool:
        return all(not x.alive for x in self.humans)

    def is_victory(self) -> bool:
        return all(not x.alive for x in self.zombies)
