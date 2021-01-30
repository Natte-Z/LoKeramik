from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import UserReview
from profiles.models import UserProfile
from .forms import ReviewForm

from django.contrib.auth.decorators import login_required


# Create your views here.


def all_reviews(request):
    """ A view to show all courses, including sorting and search queries """

    user_reviews = UserReview.objects.all()

    template = 'user_reviews/user_reviews.html'
    context = {
        'user_reviews': user_reviews,
    }

    return render(request, template, context)


@login_required
def new_review(request):
    """ Add a new review as a user """
    user_profile = UserProfile.objects.get(user=request.user)

    if request.user.is_authenticated:

        if request.method == 'POST':
            review_form = ReviewForm(request.POST)

            if review_form.is_valid():
                new_post = review_form.save(commit=False)
                new_post.user_profile = user_profile
                new_post.save()
                messages.success(request, 'Successfully added review!')
                return redirect(reverse('user_reviews'))
            else:
                messages.error(request, 'Failed to add review. \
                                Please ensure the form is valid.')
        else:
            review_form = ReviewForm()

        template = 'user_reviews/review_form.html'
        context = {
            'review_form': review_form,
        }
        return render(request, template, context)
