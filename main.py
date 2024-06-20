from __future__ import annotations
import pytest
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):

    @property
    @abstractmethod
    def house(self) -> None:
        pass

    @abstractmethod
    def build_foundation(self) -> None:
        pass

    @abstractmethod
    def build_glass(self) -> None:
        pass

    @abstractmethod
    def build_walls(self) -> None:
        pass


class Builder1(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def house(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def build_foundation(self) -> None:
        self._product.add("Фундамент")

    def build_glass(self) -> None:
        self._product.add("Стёкла")

    def build_walls(self) -> None:
        self._product.add("Стены")


class Product1():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f'Построенные части: {', '.join(self.parts)}', end="")


@pytest.mark.myTests
def test_manyWalls():
    test_builder = Builder1()
    test_builder.build_walls()
    test_builder.build_walls()
    test_builder.build_walls()
    test_builder.build_walls()
    test_builder.build_walls()
    test_builder.build_walls()
    test_builder.build_walls()
    test_builder.build_walls()
    assert (test_builder.house.parts == ["Стены", "Стены", "Стены", "Стены", "Стены", "Стены", "Стены", "Стены"])


@pytest.mark.myTests
def test_reset():
    test_builder = Builder1()
    test_builder.build_walls()
    test_builder.reset()
    assert (test_builder.house.parts == [])


if __name__ == "__main__":

    builder = Builder1()

    print("Купленный участок: ")
    builder.house.list_parts()

    print("\n")

    print("Застроенный участок: ")
    builder.build_foundation()
    builder.build_walls()
    builder.build_glass()
    builder.house.list_parts()

    print("\n")


    print("Недостроенный участок: ")
    builder.build_foundation()
    builder.build_walls()
    builder.house.list_parts()


