class Base:
    def __init__(self):
        print('base initializer')

    def f(self):
        print('base.f()')


class Sub(Base):
    def __init__(self):
        super().__init__()
        print('Sub initializer')
