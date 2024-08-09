# Decorators are described in PEP 318 and PEP 3129


# Function decorator.
def big_container(collective_material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print("<strong>*</strong> The whole order would be packed with", collective_material)
            print()
        return internal_wrapper
    return wrapper


# Function decorator.
def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print("<strong>*</strong> Wrapping items from {} with {}".format(our_function.__name__, material))
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper


# Class decorator.
class WarehouseDecorator:
    def __init__(self, material):
        self.material = material

    def __call__(self, own_function):
        def internal_wrapper(*args, **kwargs):
            print("<strong>*</strong> Wrapping items from {} with {}".format(own_function.__name__, self.material))
            own_function(*args, **kwargs)
            print()
        return internal_wrapper


@big_container("plain cardboard")
@WarehouseDecorator("kraft")
def pack_books(*args):
    print("We'll pack books:", args)


@big_container("colourful cardboard")
@WarehouseDecorator("foil")
def pack_toys(*args):
    print("We'll pack toys:", args)


@big_container("strong cardboard")
@WarehouseDecorator("cardboard")
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books("Alice in Wonderland", "Winnie the Pooh")
pack_toys("doll", "car")
pack_fruits("plum", "pear")