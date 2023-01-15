from .cart import Cart


"""
 create a context processors to set the current cart into a request context
 You will be able to acess cart in any templates
 Edit the settings file of the project: cart.context_processors.cart
"""
def cart(request):
    return {'cart': Cart(request)}