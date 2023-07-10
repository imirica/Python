class Carrier:

    __slots__ = ["name", "country"]

    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country

    def connect_to_shop(self, shop):
        # if not isinstance(shop, Shop):
        #     raise TypeError('shop must be an instance of the Shop Class')
        return ShippingOption(self.name, self.country)


class ShippingOption(Carrier):
    
    __slots__ = ["name", "country", "shipping_method", "shipping_cost"]

    def __init__(self, name: str, country: str,):
        super().__init__(name, country)
        self.shipping_method = ""
        self.shipping_cost = 0.0

    def get_shipping_cost(self, package_weight: float):
        if self.shipping_method == "standard":
            cost_per_kg = 0.5
        elif self.shipping_method == "express":
            cost_per_kg = 1
        else:
            cost_per_kg = 0.75
    
        self.shipping_cost = cost_per_kg * package_weight
        return self.shipping_cost

class Shop:

    __slots__ = ["name", "package_weight"]

    def __init__(self, name: str, package_weight: float):

        # if not isinstance(name, str):
        #     raise TypeError("Name must be a string")
        self.name = name
        
        # if not isinstance(package_weight, (int, float)):
        #     raise TypeError("Package weight must be a number")
        self.package_weight = float(package_weight)
