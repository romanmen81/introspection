class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Привет {self.name}!"

def introspection_info(obj):
    # Определяем тип объекта
    obj_type = type(obj).__name__

    # Получаем список атрибутов
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем список методов
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Определяем модуль, к которому принадлежит объект
    module = getattr(obj, '__module__', '__main__')

    # Создаем словарь с полученной информацией
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return info

# Создаем объект класса Person
person = Person("Alice", 30)

# Интроспекция объекта
person_info = introspection_info(person)
print(person_info)