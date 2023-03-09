import inspect

from position import EarthPosition
from utility import typename


def auto_repr(cls):
    # print(f"Decorating {cls.__name__} with auto_repr")
    # OBADAJ RÓŻNICE W PRZYSZŁOŚCI JESZCZE RAZ, WYDAJE SIE TO DOŚĆ ISTOTNE HEHE ;D
    members = vars(cls)                # w itinerary z list ?? tutaj jest słownik tam lista
    # for name, member in members.items():
    #     print('name = ', name, '||   member = ', member)
    #
    # members2 = list(vars(cls).items())
    # 
    # for name, member in members2:
    #     print(name, member)

    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} already defines __repr__")

    if "__init__" not in members:
        raise TypeError(f"{cls.__name__} does not override __init__")

    sig = inspect.signature(cls.__init__)
    parameter_names = list(sig.parameters)[1:]
    # print("__init__ parameter names: ", parameter_names)

    if not all(
        isinstance(members.get(name, None), property)
        for name in parameter_names
    ):
        raise TypeError(
            f"Cannot apply auto_repr to {cls.__name__} because not all "
            f"__init__ parameters have matching properties"
        )

    def synthesized_repr(self):
        return "{typename}({args})".format(             #use .format instead of f before string, because of compplexity
            typename=typename(self),
            args=", ".join(
                "{name}={value!r}".format(
                    name=name,
                    value=getattr(self, name)
                ) for name in parameter_names           #dlaczego name jest poza scoup ?
            )
        )

    setattr(cls, "__repr__", synthesized_repr)

    return cls


@auto_repr
class Location:

    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    # def __repr__(self):   - > zmuszamy komputer aby zrobił to za nas pozdro -> napierdalamy auto repr
    #     return f"{typename(self)}(name={self.name}, position={self.position} "

    def __str__(self):
        return self.name


hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))
rotterdam = Location("Rotterdam", EarthPosition(51.96, 4.47))
maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))
