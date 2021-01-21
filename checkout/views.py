from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I1I5VHsbwV3pP3YL1nWt2uiGg7vXjRDU7dY2SmiAJ4JfUItzD4m0mfbK4I59jtCo0MU7G89fmaasSLpBYbj28Ym00hPF1fDlv'
    }

    return render(request, template, context)