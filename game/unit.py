from __future__ import annotations

from typing import Generator

from .point import Point


class Unit(Point):
    alive: bool
    target: Unit
    targetDist2: float

    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.alive = True
        self.target = None

    def clone(self):
        copy = Unit(self.x, self.y)
        copy.target = self.target
        copy.alive = self.alive
        return copy

    def kill(self):
        self.alive = False

    def set_target(self, *units: list[Unit]):
        d = float("inf")

        for unit in units:
            current_distance = self.distance2(unit)

            if current_distance < d:
                d = current_distance
                self.target = unit

    def move_toward(self, p: Point, range: int):
        vector = p - self

        if vector.getNorm() < range:
            self.x = p.x
            self.y = p.y
        else:
            vector.setNorm(range)
            vector.round()
            self.x += vector.x
            self.y += vector.y

    def kill_zombies(self, zombies: list[Unit], human_alive: int) -> int:
        score = 0
        factors = self.fibonacci()
        for zombie in zombies:
            if self.distance2(zombie) < 4000000:
                zombie.kill()
                factor = next(factors)
                score += human_alive * human_alive * 10 * factor
        return score

    def fibonacci(self) -> Generator[int, None, None]:
        first = 1
        second = 2

        yield first
        yield second

        while True:
            first, second = second, second + first
            yield second
