import abc


class PokedexObject(abc.ABC):
    """
    The Abstract base class for which all Pokedex Objects will inherit.
    """
    def __init__(self, name: str, id_: int = None):
        self._name = name
        self._id = id_

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f"Name: {self._name}" if not self._id else f"Name: {self._name} ID: {self._id}"


class Stat(PokedexObject):
    def __init__(self, name: str, id_: int = None, is_battle_only: bool = None, base_value: int = None,
                 url: str = None):
        super().__init__(name, id_)
        self._is_battle_only = is_battle_only
        self._base_value = base_value
        self._url = url

    def __str__(self):
        return f"Type:{self.__class__.__name__}\n\tName: {self._name} ID: {self._id} Battle_only: {self._is_battle_only} Base_value: {self._base_value}" if self._is_battle_only is not None else f"Type:{self.__class__.__name__}\n\tName: {self._name}\n\tBase_value: {self._base_value}"

    @property
    def url(self):
        """
        Getter for url
        :return: url as a string
        """
        return self._url

    @property
    def is_battle_only(self):
        """
        Getter for is_Battle_only
        :return: boolean
        """
        return self._is_battle_only

    @is_battle_only.setter
    def is_battle_only(self, boolean):
        """
        Setter for is battle only
        :param boolean: the new value
        :return:
        """
        self._is_battle_only = boolean


class Move(PokedexObject):

    def __init__(self, name: str, id_: int = None, generation: str = None, accuracy: int = None, pp: int = None,
                 power: int = None, type: str = None,
                 damage_class: str = None, effect_short: str = None, level_aquired: int = None):
        super().__init__(name, id_)

        self._generation = generation
        self._accuracy = accuracy

        self._pp = pp

        self._power = power

        self._type = type

        self._damage_class = damage_class

        self._effect_short = effect_short

        self._level_aquired = level_aquired

    def display_summary(self, print_loc):
        """
        Summary function used to display output
        :param print_loc: either std.out or file opened via context manager.
        :return:
        """
        print("Name: ", self._name, file=print_loc)
        print("Generation: ", self._generation, file=print_loc)
        print("Accuracy: ", self._accuracy, file=print_loc)
        print("PP: ", self._pp, file=print_loc)
        print("Power", self._power, file=print_loc)
        print("Type: ", self._type, file=print_loc)
        print("Damage class: ", self._damage_class, file=print_loc)
        print("Effect_short: ", self._effect_short, file=print_loc)

    def get_generation(self):
        """
        Getter for the generation
        :return: generation as a string
        """
        return self._generation

    def __str__(self):
        return f"Type:{self.__class__.__name__}\n\tName:{self._name}\n\tID:{self._id}\n\t" \
               f"Generation {self.get_generation()}" if self._generation is not None else \
            f"Type: {self.__class__.__name__}\n\tName: {self._name}\n\tLevel Aquired: {self._level_aquired}"


class Ability(PokedexObject):
    def __init__(self, name: str, _id: int = None, generation: str = None, effect: str = None, effect_short: str = None,
                 pokemon: [str] = None):
        super().__init__(name, _id)
        self._generation = generation
        self._effect = effect
        self._effect_short = effect_short
        self._pokemon = pokemon

    def display_summary(self, print_loc):
        """
          Summary function used to display output
        :param print_loc: either std.out or file opened via context manager.
        :return:
        """
        print("Name: ", self._name, file=print_loc)
        print("ID: ", self._id, file=print_loc)
        print("Generation: ", self._generation, file=print_loc)
        print("Effect: ", self._effect, file=print_loc)
        print("Effect_short", self._effect_short, file=print_loc)
        print("Pokemon: ", self._pokemon, file=print_loc)

    def __str__(self):
        return f"Type:{self.__class__.__name__}\n\tName:{self._name}\n\tID:{self._id}\n\t" \
               f"Generation:{self._generation}\n\tEffect: {self._effect}\n\tEffect_Short: {self._effect_short}\n\tPokemon: {self._pokemon}" if self._generation is not None else f"Type:{self.__class__.__name__}\n\tName:{self._name}\n\t" \

class Pokemon(PokedexObject):
    def __str__(self):
        return f"{self.__class__} -> Name: {self._name}, Height: {self._height}, Weight: {self._weight}, Moves: {self._moves}"

    #       return f"{self.__class__} -> Name: {self._name}, Height: {self._height}, Weight: {self._weight}, Stats: {self._stats}, Types: {self._types}, Abilities: {self._abilities}, Moves: {self._moves}"
    def __init__(self, name: str, id_: int, height: int, weight: int, stats: [Stat], types: [str], abilities: [Ability],
                 moves: [Move]):
        super().__init__(name, id_)
        self._height = height
        self._weight = weight
        self._stats = stats
        self._types = types
        self._abilities = abilities
        self._moves = moves

    def display_summary(self, print_loc):
        """
        Summary function used to display output
        :param print_loc: either std.out or file opened via context manager.
        :return:
        """
        print("Type: ", self.__class__.__name__, file=print_loc)
        print("Name: ", self._name, file=print_loc)
        print("Weight: ", self._weight, file=print_loc)
        print("Height: ", self._height, file=print_loc)
        #  print("Moves: ", self._moves, file=print_loc)

        print("Moves:")
        for move in self._moves:
            print(f"\t{move}\n", file=print_loc)

        print("Stats:")
        for stat in self._stats:
            print(f"\t{stat}\n", file=print_loc)

        print("Abilities:")
        for ability in self._abilities:
            print(f"\t{ability}\n", file=print_loc)
