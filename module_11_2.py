import inspect


def introspection_info(obj):
    result = {}

    # Определение типа объекта
    result["Тип"] = type(obj).__name__

    # Получение атрибуов объекта
    attributes = dir(obj)
    public_attributes = [attr for attr in attributes if not attr.startswith('_')]
    result["Атрибуты"] = public_attributes

    # Получение методов объекта
    methods = [method for method in attributes if callable(getattr(obj, method))]
    result["Методы"] = methods

    # Получение модуля, к которому относится объект
    module = getattr(obj, '__module__', None)
    result["Модуль"] = module

    # Дополнительные свойства в зависимости от типа объекта
    if isinstance(obj, int):
        result["Свойства числа"] = {
            "Знак": "Положительное" if obj >= 0 else "Отрицательное",
            "Четность": "Четное" if obj % 2 == 0 else "Нечетное"
        }
    elif isinstance(obj, str):
        result["Свойства строки"] = {
            "Длина": len(obj),
            "Является ли строка пустой": bool(obj)
        }
    elif isinstance(obj, list):
        result["Свойства списка"] = {
            "Количество элементов": len(obj),
            "Первый элемент": obj[0] if obj else None,
            "Последний элемент": obj[-1] if obj else None
        }
    elif inspect.isclass(obj):
        result["Класс"] = {
            "Базы класса": obj.__bases__,
            "Методы класса": [func for func in dir(obj) if callable(getattr(obj, func))],
            "Документирование класса": obj.__doc__
        }

    return result


# Пример использования
number_info = introspection_info(42)
print(number_info)