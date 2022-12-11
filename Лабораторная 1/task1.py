import random


class PhysTechStudent:
    def __init__(self, name: str, age: float, subject: str, average_mark: float = 0.0):
        """
        This method creates PhysTechStudent object that describes student of Phystech student
        :param name: Name of student Should be str type
        :param age: student graduate year
        :param subject: speciality is string from  [astronomy, plasma, nanostructure, biophysics, nuclear]
        :param average_mark: average student's mark

        Example:

        >>> student = PhysTechStudent("Bob", 6, "astronomy") # class initialisation
        """

        if not isinstance(name, str):
            raise TypeError("Use str type for name")
        else:
            self.name = name

        if not isinstance(age, (int, float)):
            raise TypeError("Please use int or float number for age")
        else:
            self.age = float(age)

        if not isinstance(subject, str):
            raise TypeError("Please use str for parameter subject")
        else:
            if not (subject in ["astronomy", "plasma", "nanostructure", "biophysics", "nuclear"]):
                raise TypeError("There is no subject " + subject + "in our faculty\n Use one number in ["
                                                                   "astronomy, plasma, nanostructure, "
                                                                   "biophysics, nuclear]")

            self.subject = subject

        if not isinstance(average_mark, (int, float)):
            raise TypeError("Please use int or float number for average_mark")
        else:
            self.average_mark = float(average_mark)

    def __str__(self):
        """
        Returns Student parameters

        :return:
        str with student parameters
        Example:
        >>> student = PhysTechStudent("Bob", 6, "astronomy") # create Student
        >>> print(str(student))
        Student: Bob age: 6.0(astronomy)
        """

        return "Student: " + self.name + " age: " + str(self.age) + "(" + self.subject + ")"

    def go_to_next_year(self) -> bool:
        """
        Change the age of student by 1.
        if age bigger than 6 returns False
        :return: boolen

        Example:
        >>> student = PhysTechStudent("Bob", 2, "astronomy") # create Student
        >>> print(student.go_to_next_year())
        True
        """

        if self.age >= 6 and self.average_mark >= 3:
            return False
        else:
            self.age += 1
            return True

    def change_mark(self, list_of_marks: list[float]) -> float:
        """
        Calculate average student's mark.
        :param list_of_marks: list of student's marks which were got at the end of the term
        :return: average mark

        Example:
        >>> student = PhysTechStudent("Bob", 2, "astronomy") # create Student
        >>> print(student.change_mark([3, 5, 4, 3, 4]))
        3.8
        """

        self.average_mark = sum(list_of_marks) / len(list_of_marks)
        return self.average_mark


class Package:
    def __init__(self, weight: int, hight: int, width: int, length: int):
        """
        Создание и подготовка к работе объекта "Посылка"
        :param weight: вес посылки
        :param hight: ширина посылки
        :param length: длина посылки
        :param width: ширина посылки
        Пример:
        >>> package = Package(2, 1, 3, 4)  # инициализация экземпляра класса
        """
        if not isinstance(weight, int):
            raise TypeError('Weight must be int')

        if weight <= 0:
            raise ValueError('Weight cannot be 0')
        self.weight = weight

        if not isinstance(hight, int):
            raise TypeError('Hight must be int')

        if hight <= 0:
            raise ValueError('Hight cannot be 0')
        self.width = hight

        if not isinstance(width, int):
            raise TypeError('Width must be int')

        if hight <= 0:
            raise ValueError('Width cannot be 0')
        self.width = width

        if not isinstance(length, int):
            raise TypeError('Length must be int')

        if length <= 0:
            raise ValueError('Length cannot be 0')
        self.length = length

    def send(self) -> None:
        """
        Отправление посылки.
        :raise ValueError: вызываем ошибку, если посылка будет слишком тяжелая для отправления
        Пример:
        >>> package = Package(2, 1, 3, 4)
        >>> package.send()
        """
        ...

    def break_package(self, breaking_tool: str) -> None:
        """
        Повреждение посылки при отправлении, если клиент редиска
        :param breaking_tool: то, чем повреждаем посылку
        :raise ValueError: вызываем ошибку, если обстоятельства не будут слишком жесткими для нанесения повреждений
        Пример:
        >>> package = Package(2, 1, 3, 4)
        >>> package.break_package('hammer')
        """
        if not isinstance(breaking_tool, str):
            raise TypeError('A tool for breaking a package must be a string!')


class Cat:
    def __init__(self, is_hungry: bool = False, is_tired: bool = False, is_bored: bool = False):
        """
        Cat is my beloved kitty.
        :param is_hungry: if the cat is hungry
        :param is_tired: if the cat is tired
        :param is_bored: if the cat is bored
        Example:
        >>> cat = Cat()
        """
        if isinstance(type(is_hungry), bool):
            raise TypeError("Use just True or False for this parameter")

        if isinstance(type(is_hungry), bool):
            raise TypeError("Use just True or False for this parameter")

        if isinstance(type(is_bored), bool):
            raise TypeError("Use just True or False for this parameter")

        if isinstance(type(is_tired), bool):
            raise TypeError("Use just True or False for this parameter")

        self.action = ""

        self.is_hungry = is_hungry
        self.is_bored = is_bored
        self.is_tired = is_tired

    def meow(self, times: int = 1, loud: int = 0):
        """
        make annoying sound to grab your attention
        :param times: number of times of pronouncing 'meow'
        :param loud: the volume of pronouncing 'meow'
        :return:
        Example:
        >>> cat = Cat()
        >>> cat.meow()
        ['meow']

        """
        e = "e"
        o = "o"
        for _ in range(loud):
            e += "e"
            o += "o"

        sound = "m" + e + o + "w"
        self.action = ""

        self.action = str([sound for _ in range(times)])
        print(self.action)

    def update_cat_state(self):
        """
        What action does the cat do.
        >>> cat = Cat(is_tired=True)
        >>> cat.update_cat_state()
        i'm_tired
        ['meeeooow']
        """

        if self.is_tired:
            print("i'm_tired")
            self.meow(1, 2)
            self.is_tired = False

        if self.is_hungry:
            print("i'm_hungry")
            self.meow(20, 20)
            self.is_hungry = False

        if self.is_bored:
            print("i'm_bored")
            self.meow(20, 0)
            self.is_bored = False

        if not self.is_bored and not self.is_hungry and not self.is_tired:
            key = random.choice(list(self.__dict__.keys())[1:])
            self.__dict__[key] = True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
