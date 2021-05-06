#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

North = 'north'
East = 'east'
South = 'south'
West = 'west'


class Maze:
    def add_room(self, room):
        pass


class Wall:
    pass


class BombedWall(Wall):
    pass


class Room:
    def __init__(self, number):
        self.number = number

    def set_side(self, side, kind):
        pass


class EnchantedRoom(Room):
    def __init__(self, number, cast_spell):
        self.cast_spell = cast_spell
        super().__init__(number)


class RoomWithABomb(Room):
    pass


class Door:
    def __init__(self, room1, room2):
        self.room1 = room1
        self.room2 = room2


class DoorNeedingSpell(Door):
    pass


class AbstractMazeFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_maze(self):
        pass

    @abstractmethod
    def make_wall(self):
        pass

    @abstractmethod
    def make_room(self, number):
        pass

    @abstractmethod
    def make_door(self, room1, room2):
        pass


class MazeFactory(AbstractMazeFactory):
    def make_maze(self):
        return Maze()

    def make_wall(self):
        return Wall()

    def make_room(self, number):
        return Room(number)

    def make_door(self, room1, room2):
        return Door(room1, room2)


class EnchantedMazeFactory(MazeFactory):
    @property
    def cast_spell(self):
        return ''

    def make_room(self, number):
        return EnchantedRoom(number, self.cast_spell)

    def make_door(self, room1, room2):
        return DoorNeedingSpell(room1, room2)


class BombedMazeFactory(MazeFactory):
    def make_wall(self):
        return BombedWall()

    def make_room(self, number):
        return RoomWithABomb(number)


class MazeGame:
    def create_maze(self, factory):
        a_maze = factory.make_maze()
        room1 = factory.make_room(1)
        room2 = factory.make_room(2)
        a_door = factory.make_door(room1, room2)

        a_maze.add_room(room1)
        a_maze.add_room(room2)

        room1.set_side(North, factory.make_wall())
        room1.set_side(East, a_door)
        room1.set_side(South, factory.make_wall())
        room1.set_side(West, factory.make_wall())

        room2.set_side(North, factory.make_wall())
        room2.set_side(East, factory.make_wall())
        room2.set_side(South, factory.make_wall())
        room2.set_side(West, a_door)

        return a_maze


def test_maze():
    maze_game = MazeGame()
    factory = MazeFactory()
    maze_game.create_maze(factory)


def test_enchanted():
    maze_game = MazeGame()
    factory = EnchantedMazeFactory()
    maze_game.create_maze(factory)


def test_bombed():
    maze_game = MazeGame()
    factory = BombedMazeFactory()
    maze_game.create_maze(factory)


if __name__ == '__main__':
    test_maze()
    test_enchanted()
    test_bombed()
