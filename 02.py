# -*- coding: utf-8 -*-


class Youki(object):
    def __init__(self, limit=None):
        self.water = 0
        if limit is None:
            limit = 0
        self.limit = limit

    def set_water(self, water):
        self.water = water

    def add_water(self, add_water):
        sum_water = self.water + add_water
        sa_water = 0
        if sum_water > self.limit:
            self.water = self.limit
            sa_water = sum_water - self.limit
        else:
            self.water = sum_water
        return sa_water

    def move_water(self, a_youki):
        sa = self.add_water(a_youki.water)
        a_youki.set_water(sa)


a = Youki(3)
b = Youki(5)

a.add_water(10)
print(a.water, b.water)
b.move_water(a)
print(a.water, b.water)
a.add_water(10)
print(a.water, b.water)
b.move_water(a)
print(a.water, b.water)
b.set_water(0)
print(a.water, b.water)
b.move_water(a)
print(a.water, b.water)
a.add_water(10)
print(a.water, b.water)
b.move_water(a)
print(a.water, b.water)
