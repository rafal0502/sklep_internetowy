from .cart import Cart

# Tworze egzemplarz koszyka na zakupy i udostępniam go wszystkim szablonom jako zmienna cart
def cart(request):
    return {'cart': Cart(request)}

