from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from products.models import Product
from .forms import UserProfileForm

from checkout.models import Order

#class ProfileView(TemplateView):
    #template_name = 'profiles/profile.html'

    #def get(self, request):
        #products = Product.objects.exclude(id=request.product.id)
        #profile = get_object_or_404(UserProfile, user=request.user)
        #favourite = Favourite.objects.get(current_product=request.profile)
        #favourites = favourite.products.all()

    #args = {'users':users, 'favourites': favourites}
    #return render(request,self.template_name, args)

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    favourites = profile.favourites.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'favourites': favourites,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

def change_favourite(request, operation, pk):
    favourite = Product.objects.get(pk=pk)
    profile = get_object_or_404(UserProfile, user=request.user)
    if operation == 'add': 
        profile.favourites.add(favourite)
    elif operation == 'remove':
        profile.favourites.remove(favourite)
    return redirect('profile')
