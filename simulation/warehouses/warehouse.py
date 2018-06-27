from simulation import BaseObject


class Warehouse(BaseObject):

    def __init__(self, initial_goods=None, *args, **kwargs):
        super().__init__()

        if initial_goods is not None:
            self.contains = initial_goods
        else:
            self.contains = {}

    def add_good(self, good, count):
        if good.name in self.contains:
            self.contains[good.name] += count
        else:
            self.contains[good.name] = count

    def remove_good(self, good, count):
        if good.name in self.contains:
            if count > self.contains[good.name]:
                raise ValueError("You don't have that many %s" % good.name)
            else:
                self.contains[good.name] -= count

        else:
            raise ValueError("You don't have any %s" % good.name)

    def trade(self, warehouse, good, count):
        self.remove_good(good, count)
        warehouse.add_good(good, count)

    def count(self, good):
        if good.name in self.contains:
            return self.contains[good.name]

        return 0
