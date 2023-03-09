class Animal:
    @classmethod
    def description(cls):
        return "An Animal "


class Bird(Animal):
    @classmethod
    def description(cls):
        s = super()
        return s.description() + "with wings "


class Flaming(Bird):
    @classmethod
    def description(cls):
        s = super()
        print(s)
        print(s.description())
        return super().description() + "and with pinky features "
