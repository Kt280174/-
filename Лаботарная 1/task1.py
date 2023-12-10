# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Table:
    def __init__(self, length: float, width: float, height: float):
        """
        Создание и подготовка к работе обекта "Стол"
        :param length: длина стола
        :param width: ширина стола
        :param height: высота стола


        Примеры:
        >>> table = Table(100, 50, 50)
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина стола должен быть типа int или float")
        if length <= 0:
            raise ValueError("Длина стола должен быть положительным числом")
        self.length = length
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина стола должен быть типа int или float")
        if width <= 0:
            raise TypeError("Ширина стола должен быть положительным числом")
        self.width = width
        if not isinstance(height, (int, float)):
            raise TypeError("Высота стола должен быть типа int или float")
        if height <= 0:
            raise ValueError("Высота стола должен быть положительным числом")
        self.height = height

    def diagonal(self):
        """
        Функция которая вычисляет диагональ стола:
        :return: диагональ стола

        Примеры:
        >>> table = Table(100, 50, 50)
        >>> table.diagonal()
        """
        ...

    def perimeter(self):
        """
        Функция которая вычисляет периметр стола
        :return: периметр стола

        Примеры:
        >>> table = Table(100, 50, 50)
        >>> table.perimeter()
        """
        ...

    def square(self):
        """
        Функция которая вычисляет площадь стола
        :return: площадь стола

        Примеры:
        >>> table = Table(100, 50, 50)
        >>> table.square()
        """
        ...


class Facebook:
    def __init__(self, users: int, followers: int):
        """
            Создание и подготовка к работе обекта "Facebook"
            :param users: количество пользователей
            :param followers: количество подписчиков

        Примеры:
        >>> facebook = Facebook(100000, 130000)
        """
        if not isinstance(users, int):
            raise TypeError("Количество пользователей должно быть типа int")
        if users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным числом")
        self.users = users
        if not isinstance(followers, int):
            raise TypeError("Количество подписчиков должно быть типа int")
        if followers < 0:
            raise ValueError("Количество подписчиков не может быть отрицательным числом")
        self.followers = followers

    def add_users(self, number: int):
        """
        Добавление количества пользователей Facebook
        :param number: количество добавляемых пользователей

        Примеры:
        >>> facebook = Facebook(100000, 130000)
        >>> facebook.add_users(200)
        """
        if not isinstance(number, int):
            raise TypeError("Добавляемое количество пользователей должно быть типа int")
        if number < 0:
            raise ValueError("Добавляемое количество пользователей не может быть положительным числом")
        ...

    def remove_users(self, number: int):
        """
        Извеление количества пользователей
        :param number: количество извлекаемых пользователей
        :raise ValueError: Если количество извлекаемых пользователей превышает количество пользователей Facebook, то возвращается ошибка

        :return: количество реально извлеченных пользователей

        Примеры:
        >>> facebook = Facebook(1000000, 1300000)
        >>> facebook.remove_users(100)
        """
        ...

    def add_followers(self, number: int):
        """
        Добавление количества подписчиков Facebook
        :param number: количество добавляемых подписчиков

        Примеры:
        >>> facebook = Facebook(1000000, 1300000)
        >>> facebook.add_followers(300)
        """
        ...


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        """
        Создание и подготовка к работе обекта "Треугольник"
        :param a, b, c: стороны трехугольника

        Примеры:
        >>> triangle = Triangle(20, 30, 40)
        """
        if not isinstance(a, (int, float)):
            raise TypeError("Сторона треугольника должна быть типа int или float")
        if a <= 0:
            raise ValueError("Сторона треугольника должна быть положительным числом")
        self.a = a
        if not isinstance(b, (int, float)):
            raise TypeError("Сторона треугольника должна быть типа int или float")
        if b <= 0:
            raise ValueError("Сторона треугольника должна быть положительным числом")
        self.b = b
        if not isinstance(c, (int, float)):
            raise TypeError("Сторона треугольника должна быть типа int или float")
        if c <= 0:
            raise ValueError("Сторона треугольника должна быть положительным числом")
        self.c = c
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Трехугольник не существует")

    def is_right_triangle(self):
        """
        Функция которая проверяет является ли трехугольник прямоугольным

        :return: Является ли трехугольник прямоугольным

        Примеры:
        >>> triangle = Triangle(20, 30, 40)
        >>> triangle.is_right_triangle()
        """
        ...

    def is_isosceles_triangle(self):
        """
        Функция которая проверяет является ли трехугольник равнобедренным

        :return: Является ли трехугольник равнобедренным

        Примеры:
        >>> triangle = Triangle(20, 30, 40)
        >>> triangle.is_isosceles_triangle()
        """
        ...

    def is_equilateral_triangle(self):
        """
        Функция которая проверяет является ли трехугольник равноcторонним

        :return: Является ли трехугольник равносторонним

        Примеры:
        >>> triangle = Triangle(20, 30, 40)
        >>> triangle.is_equilateral_triangle()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

