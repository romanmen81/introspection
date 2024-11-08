class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Привет {self.name}!"

def introspection_info(obj):
    # Определяем тип объекта
    obj_type = type(obj).__name__

    # Получаем список атрибутов, методов и их свойств
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Определяем модуль, к которому принадлежит объект
    module = getattr(obj, '__module__', '__main__')

    # Получаем специальные методы (обычно начинаются и заканчиваются на "__")
    special_methods = [method for method in dir(obj) if method.startswith("__") and method.endswith("__")]

    # Получаем длину объекта, если это возможно
    try:
        obj_length = len(obj)
    except TypeError:
        obj_length = None

    # Получаем словарь, содержащий свойства объекта
    properties = {attr: getattr(obj, attr) for attr in attributes}

    # Собираем всю информацию в словаре
    info = {
        'type': obj_type,
        'module': module,
        'attributes': attributes,
        'methods': methods,
        'special_methods': special_methods,
        'length': obj_length,
        'properties': properties,
    }

    return info

def print_introspection(info):
    for key, value in info.items():
        if isinstance(value, list):
            print(f"{key}:")
            for item in value:
                print(f"  - {item}")
        elif isinstance(value, dict):
            print(f"{key}:")
            for k, v in value.items():
                print(f"  - {k}: {v}")
        else:
            print(f"{key}: {value}")

# Создаем объект класса Person
person = Person("Роман", 43)

# Интроспекция объекта
person_info = introspection_info(person)
print()
print_introspection(person_info)
