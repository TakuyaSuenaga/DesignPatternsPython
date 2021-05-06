#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Glyph(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, window):
        pass

    @abstractmethod
    def bounds(self, rect):
        pass

    @abstractmethod
    def intersects(self, point):
        pass

    @abstractmethod
    def insert(self, glyph, index):
        pass

    @abstractmethod
    def remove(self, glyph):
        pass

    @abstractmethod
    def child(self, index):
        pass

    @abstractmethod
    def parent(self):
        pass
