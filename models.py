from datetime import datetime

class Entity:
    """Base class for all entities in the system.
    Used to demonstrate class inheritance."""
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        """Returns a developer-friendly string representation of the entity."""
        return f"{self.__class__.__name__}({self.id})"


class Product(Entity):
    """Represents a product available for sale.Inherits from Entity."""
    def __init__(self, id, name, category, base_price):
        super().__init__(id)
        self.name = name
        self.category = category
        self.base_price = float(base_price)

    def __str__(self):
        """Returns a user-friendly string representation of the product."""
        return f"{self.name} ({self.category}) - ${self.base_price:.2f}"


class Customer(Entity):
    """Represents a customer.Inherits from Entity."""
    def __init__(self, id, name, email, lifetime_value=0.0):
        super().__init__(id)
        self.name = name
        self.email = email
        self.lifetime_value = float(lifetime_value)

    def __str__(self):
        """Returns a user-friendly string representation of the customer.:"""    
        return f"{self.name} (${self.lifetime_value:.2f})"


class Order:
    """Represents a customer order."""
    def __init__(self, order_id, customer, product, quantity, unit_price, order_date, status):
        self.order_id = order_id
        self.customer = customer
        self.product = product
        self.quantity = int(quantity)
        self.unit_price = float(unit_price)
        self.order_date = datetime.strptime(order_date, "%Y-%m-%d") if isinstance(order_date, str) else order_date
        self.status = status

    @property
    def amount(self):
        """Calculates the total order amount.
        Returns: float: Total price of the order."""
        return self.quantity * self.unit_price

    def __str__(self):
        """Returns a user-friendly string representation of the order."""
        return f"Order {self.order_id}: {self.product.name} x {self.quantity} for {self.customer.name}"
