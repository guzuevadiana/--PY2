class Particles:
    def __init__(self, name: str, coordinates: list, momentum: list, force: list, time: float) -> None:
        self.name = name
        self.coordinates = coordinates
        self.momentum = momentum
        self.force = force
        self.time = time

    def __str__(self) -> str:
        return f"Частица {self.name}. Время {self.time}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, time={self.time!r}, coordinates={self.name!r})"

    def prop(self, dt: float) -> None:
        """
        :param dt: изменение импульса на время dt.

        """
        self.momentum = [self.momentum[i] + dt * self.force[i] for i in range(len(self.momentum))]
        self.time = self.time + dt

    def force_in_time(self) -> None:
        print(f"Сила {self.force}. Время {self.time}")


class Fermions(Particles):
    def __init__(self, name: str, coordinates: list, momentum: list, force: list, time: float, mass: float) -> None:
        super().__init__(name=name, coordinates=coordinates, momentum=momentum, force=force, time=time)
        self.mass = mass

    def prop(self, dt: float) -> None:
        """
        :param dt: изменение координаты на время dt по закону Ньютона. Необходимо по причине того, что есть масса,
        по которой можно узнать изменение координаты.

        """
        self.coordinates = [self.coordinates[i] + dt * self.momentum[i] / self.mass +
                            (self.force / self.mass * dt * dt) / 2 for i in range(len(self.coordinates))]
        self.time = self.time + dt


if __name__ == "__main__":
    instance = Particles(name="electron", coordinates=[0, 0], momentum=[10, 0], force=[0, 1], time=0.0)
    print(instance)
    print(repr(Particles))
    instance_2 = Fermions(name="electron", coordinates=[0, 0], momentum=[10, 0], force=[0, 1], time=0.0, mass=1)
    pass
