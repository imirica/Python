import random
from shipping import Carrier, ShippingOption, Shop

# Create a list of shops
shops = [
    Shop("Carrefour", 3.5),
    Shop("Metro", 2.0),
    Shop("Mega Image", 4.2),
    Shop("Lidl", 10)
]

# Create a list of carriers
carriers = [
    Carrier("TNT", "Romania"),
    Carrier("DPD", "Romania"),
    Carrier("DHL", "Germany")
]

# Iterate through the list of shops
for shop in shops:
    print(f"Shipping options for {shop.name}:")
    
    # Connect carriers to the current shop

    for carrier in carriers:
        shipping_option = carrier.connect_to_shop(shop)

        shipping_methods = ["standard", "express", "priority", "scheduled"] # available shipping methods
        shipping_option.shipping_method = random.choice(shipping_methods)  # Set the shipping method

        shipping_cost = shipping_option.get_shipping_cost(shop.package_weight)
        print(f"{carrier.name}: {shipping_cost:.2f}")
    
    print()  # Add a line break between shops
