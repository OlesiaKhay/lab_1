# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
class tovar_crm:
    def __init__(self, name: str, price: float):
        """
        Создание и подготовка к работе объекта "Карточка товара"
        :param name: Название товара
        :param price: Цена товара
        Пример:
        >>> tovar = tovar_crm('Веревка', 100)
        """
        if not isinstance(price, (int, float)):
            raise TypeError('Цена должна быть численной')
        if price <= 0:
            raise ValueError('Цена должна быть больше нуля')
        self.price = price
        if not isinstance(name, str):
            raise TypeError('Название должно быть строкой')
        self.name = name
    def change_price(self, new_price: float):
        """
        Функция изменения цены товара
        :param new_price: Новая цена товара
        :return: Меняет цену товара
        :raise ValueError: если введена неверная новая цена товара
        Пример:
        >>> tovar = tovar_crm("Веревка", 100)
        >>> tovar.change_price(150)
        """
        if not isinstance(new_price, (int, float)):
            raise ValueError("Цена должна быть больше нуля")

    def make_bonuses(self, name: str):
        """
        Функция возврата бонусов за товар (кэшбек/внутренняя система лояльности)
        :param name: Принимает название товара и сранвивает с актуальной таблицей бонусной системы
        :return: Вовзращает количество начисляемых бонусов
        Пример:
        >>> tovar = tovar_crm("Веревка", 150)
        >>> tovar.make_bonuses("Веревка")
        """

###
class tovar_buh:
    def __init__(self, SKU: str, price: float, uchet: bool):
        """
        Создание и подготовка к работе объекта "Карточка товара"
        :param SKU: Название позиции
        :param price: Цена в учете
        :param uchet: FIFO - 1, средняя - 0
        Пример:
        >>> tovar = tovar_buh('Веревка_12322', 100, True)
        """
        if not isinstance(price, (int, float)):
            raise TypeError('Цена должна быть численной')
        if price <= 0:
            raise ValueError('Цена должна быть больше нуля')
        self.price = price
        if not isinstance(SKU, str):
            raise TypeError('Название должно быть строкой')
        self.SKU = SKU
        if not isinstance(uchet, bool):
            raise TypeError('Учёт по УП не может вестись вне рамок FIFO/Средней')
        self.uchet = uchet
    def change_uchet(self, new_uchet: bool):
        """
        Функция изменения учета товара
        :param new_uchet: Новый порядок учета товара
        :return: Меняет учет товара
        :raise ValueError: если введен неверный новый учет товара
        Пример:
        >>> tovar = tovar_buh("Веревка_12322", 89, True)
        >>> tovar.change_uchet(False)
        """
        if not isinstance(new_uchet, bool):
            raise ValueError("Учёт по УП не может вестись вне рамок FIFO/Средней")
    def make_impairment(self, coeff: float):
        """
        Функция обесценения запасов товара
        :param coeff: Коэффициент обесценения
        :return: Вовзращает количество начисляемых бонусов
        :raise ValueError: если введена неверный коэффциент учет товара
        Пример:
        >>> tovar = tovar_buh("Веревка_12322", 100, True)
        >>> tovar.make_impairment(0.21)
        """
        if not isinstance(coeff, float):
            raise ValueError("Коэффициент обесценения должен быть численным")

###
class tabel:
    def __init__(self, pos: str, staj: int, wage: float):
        """
        :param pos: Должность работника
        :param staj: Стаж работник
        :param wage: Ставка работника
        Пример:
        >>> worker = tabel("Экономист", 3, 300)
        """
        if not isinstance(pos, str):
            raise TypeError('Введите корректную должность')
        self.pos = pos
        if staj < 0:
            raise ValueError('Стаж должен быть больше нуля')
        self.staj = staj
        if not isinstance(wage, (int, float)):
            raise TypeError('Ставка должна быть численной')
        if wage <= 0:
            raise ValueError('Ставка оплаты не может быть меньше 0')
        self.wage = wage
    def change_wage(self, new_wage: float):
        """
        :param new_wage: Новая ставка зп
        :return: Изменяет ставку в табеле
        :raise TypeError: Если ставка была введеа неверно
        :raise ValueError: Если ставка была меньше нуля
        Пример:
        >>> economist = tabel("Экономист", 2, 300)
        >>> economist.change_wage(400)
        """
        if not isinstance(new_wage, (int, float)):
            raise TypeError('Ставка должна быть численной')
        if new_wage <= 0:
            raise ValueError('Ставка оплаты не может быть меньше 0')
    def change_pos(self, pos: str, wage: float):
        """
        :param pos: Название новой должности
        :raise TypeError: Если должность была введеа неверно
        :param wage: Новая ставка ЗП
        :raise TypeError: Если ставка была введеа неверно
        :raise ValueError: Если ставка была меньше нуля
        :return: Новое значение должности и ставки ЗП
        """
        if not isinstance(pos, str):
            raise TypeError('Ставка должна быть численной')
        if not isinstance(wage, (float, int)):
            raise TypeError('Ставка должна быть численной')
        if wage <= 0:
            raise ValueError('Ставка оплаты не может быть меньше 0')