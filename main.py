import json
from pathlib import Path

from registry import OrderRegistry
from order_factory import PizzaFactory, MonsterEnergyFactory, SaladFactory

ORDER_FILE_PATH: str = f"{Path(__file__).parent.absolute()}/orders.json"


def main() -> None:
    # Registering order types
    order_registry = OrderRegistry()
    order_registry.register("pizza", PizzaFactory())
    order_registry.register("monster", MonsterEnergyFactory())
    order_registry.register("salad", SaladFactory())

    with open(ORDER_FILE_PATH, encoding="utf-8") as file:
        data = json.load(file)

        orders = (order_registry.create(item) for item in data["orders"])

        # Run the orders
        for order in orders:
            order.run()


if __name__ == "__main__":
    main()
