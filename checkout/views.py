from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        massages.error(request, "There's nothing in your bag at the moment")
        return render(reversed('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JPvlDDVZmU4ipz3fDAur4GILUEy8d8idHYnbLfrppYGNTaH1xDauiIyQUYeFK3kRIlYuR9GHmZkMFKlum5paLSv00yPYZf4gq',
        'client_secret': 'test client secret',
    }

    return render(request, template , context)