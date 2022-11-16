from typing import Protocol, Any


class Order(Protocol):
    def run(self) -> None:
        """Run the order."""


class OrderFactory(Protocol):
    def create(self, args: dict[str, Any]) -> Order:
        """Create a new order."""


class OrderRegistry:
    def __init__(self) -> None:
        self.registry: dict[str, OrderFactory] = {}

    def register(self, order_type: str, factory: OrderFactory) -> None:
        if order_type in self.registry:
            print(f"{order_type} already registered, skipping.")
            return None

        self.registry[order_type] = factory

    def unregister(self, order_type: str) -> None:
        self.registry.pop(order_type, None)

    def create(self, args: dict[str, Any]) -> Order:
        args_copy = args.copy()

        if (order_type := args_copy.pop("type", None)) is not None:
            factory = self.registry[order_type]
            return factory.create(args_copy)

        raise ValueError("Invalid data format: Missing TYPE.")
