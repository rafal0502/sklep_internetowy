from decimal import Decimal
from django.conf import settings
from myshop.shop.models import Product



class Cart(object):

    def __init__(self, request):
        """
        Inicjalizacja koszyka na zakupy
        :param request:
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # utowrzenie pustego koszyka na zakupy w sesji
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, product, quantity=1, update_quantity=False):
        """
        Dodanie produktu do koszyka lub zmiana jego ilości
        :param quantity:
        :param update_quantity:
        :return:
        """
        product_id = str(product.id)
        if product_id not in self.session:
            self.cart[product_id] = {'quantity': 0,
                                       'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """
        Uaktualnienie koszyka w sesji
        :return:
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        # oznaczenie jako "zmodyfikowanej" aby upewnić się o jej zapisaniu
        self.session.modified = True


    def remove(self, product):
        """
        Usunięcie produktu z koszyka na zakupy
        :return:
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def __iter__(self):
        """
        Iteracja przez elementy koszyka i pobranie produktów z bazy danych
        :return:
        """
        product_ids = self.cart.keys()
        for product in product_ids:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    def __len__(self):
        """
        Obliczenie liczby wszystkich elementów w koszyku na zakupy
        :return:
        """
        return sum(item['quantity'] for item in self.cart.values())


    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())


    def clear(self):
        #Usunięcie koszyka na zakupy z sesji
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True


