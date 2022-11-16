from typing import Any

from registry import Order
from orders import Pizza, MonsterEnergy, Salad


class PizzaFactory:
    def create(self, args: dict[str, Any]) -> Order:
        return Pizza(**args)


class MonsterEnergyFactory:
    def create(self, args: dict[str, Any]) -> Order:
        return MonsterEnergy(**args)


class SaladFactory:
    def create(self, args: dict[str, Any]) -> Order:
        return Salad(**args)
