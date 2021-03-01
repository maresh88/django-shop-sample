from decimal import Decimal

from django.conf import settings
from shop.models import Product


class Cart:
    """
    Cart class, that provides basic cart functionality
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        """
        saving changes to the cart
        """
        self.session.modified = True

    def add(self, product, quantity=1):
        """
        adding 1pc of product to the cart
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            price = product.discount_price if product.discount_price else product.price
            self.cart[product_id] = {'quantity': 0, 'price': str(price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        """
        removing product item with all its pieces from the cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def remove_one_item(self, product, quantity=1):
        """
        removing 1pc of particular product from the cart.
        if it only has 1pc, then completely remove product from the cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            if self.cart[product_id]['quantity'] > 1:
                self.cart[product_id]['quantity'] -= quantity
            else:
                self.remove(product)
            self.save()

    def __iter__(self):
        """
        list of items grouped by product
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        amount of products in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        total price of the cart
        :return:
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        removing cart from the user session
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()
