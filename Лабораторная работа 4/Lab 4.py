if __name__ == "__main__":
    class Animal:
        """Базовый класс, представляющий животных."""

        def __init__(self, species: str, sound: str):
            self._species = species  # Species of the animal
            self._sound = sound  # Sound the animal makes

        def make_sound(self) -> str:
            """
            Издать характерный звук животного.
            Returns:
            str: Звук, издаваемый животным.
            """
            return self._sound

        def get_species(self) -> str:
            """
            Получить вид животного.
            Returns:
            str: Вид животного.
            """
            return self._species

        def __str__(self) -> str:
            return f"Животное {self._species}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}({self._species}, {self._sound})"


    class Dog(Animal):
        """Производный класс, представляющий собак."""

        def __init__(self, species: str, sound: str, breed: str):
            super().__init__(species, sound)
            self._breed = breed  # Breed of the dog

        def make_sound(self) -> str:
            """
                 Издать характерный звук собаки.
                 Returns:
                 str: Звук, издаваемый собакой.
                 """
            return "Гав! Гав!"


    def __str__(self) -> str:
        return f"Собака породы {self._breed} {self._species}"


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._species}, {self._sound}, {self._breed})"


class Cat(Animal):
    """Производный класс, представляющий кошек."""

    def __init__(self, species: str, sound: str, color: str):
        super().__init__(species, sound)
        self._color = color  # Color of the cat

    def get_color(self) -> str:
        """
            Получить окрас кошки.
            Returns:
            str: Окрас кошки.
        """
        return self._color

    def make_sound(self) -> str:
        """
            Издать характерный звук кошки.
            Returns:
            str: Звук, издаваемый кошкой.
        """
        return "Мяу!"

    def __str__(self) -> str:
        return f"Кошка окраса  {self._color} {self._species}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._species}, {self._sound}, {self._color})"

    pass
