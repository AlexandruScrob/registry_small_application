from enum import StrEnum, auto

from pydantic import BaseModel, Field


class MonsterEnergyTypes(StrEnum):
    ORIGINAL = auto()
    RIPPER = auto()
    JUICED = auto()


class Pizza(BaseModel):
    count: int
    ingredients: list[str] = Field(default_factory=list)

    def run(self) -> None:
        print(
            f"Ordered {self.count} Pizza with ingredients: "
            f"{', '.join(self.ingredients)}."
        )


class MonsterEnergy(BaseModel):
    count: int
    drink_type: MonsterEnergyTypes

    def run(self) -> None:
        print(f"Ordered {self.count} {self.drink_type} Monster energy.")


class Salad(BaseModel):
    ingredients: list[str] = Field(default_factory=list)
    with_croutons: bool = True

    def run(self) -> None:
        print(
            f"Ordered a salad with: {', '.join(self.ingredients)} "
            f" {'with' if self.with_croutons else 'without'} croutons."
        )
