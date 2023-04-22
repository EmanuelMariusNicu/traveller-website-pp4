from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Trip
from .forms import CommentForm, TripForm
from django.db.models import Q, Count
from utils.constants import TAGS
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


class TripList(generic.ListView):
    model = Trip
    queryset = Trip.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class TripDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Trip.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )
   
    def post(self, request, slug, *args, **kwargs):

        queryset = Trip.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class TripLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Trip, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class SearchResults(View):
    """
    Custom view for displaying search results. Checks if the inputted string
    appears in our trips.
    """
   
    def post(self, request, *args, **kwargs):
        searched = request.POST['search-bar']
        trips = Trip.objects.filter(
            Q(title__icontains=searched) |
            Q(additional_info__icontains=searched) |
            Q(route__icontains=searched),
            status=1
            )

        return render(
            request,
            'search_results.html',
            {'searched': searched, 'trips': trips}
            )

    def get(self, request, *args, **kwargs):
        return render(request, 'search_results.html')


class BrowseByTag(View):
    """
    Custom view to display trips matching the selected tag. Tags are accessed
    via a tuple of tuples called TAGS
    tag: str, the tag name, as it appears to the user
    slug: str, slugified version of the selected tag
    """
    def get(self, request, slug, *args, **kwargs):
        if slug == 'new':
            trips = Trip.objects.filter(status=1)\
                .order_by('-created_on')
            tag = 'New'
        elif slug == 'popular':
            trips = Trip.objects.filter(status=1)\
                .annotate(q_count=Count('likes')).order_by('-q_count')
            tag = 'Popular'
        else:
            for tuple in TAGS:
                if slug in tuple:
                    tag = tuple[0]

            trips = Trip.objects.filter(
                status=1,
                tags__contains=tag
                )

        return render(
            request,
            'browse.html',
            {
                'trips': trips,
                'tag': tag,
                'slug': slug,
            },
        )


def error_404_view(request, exception):
    """
    Custome 404 page
    Tutorial at https://www.geeksforgeeks.org/django-creating-a-404-error-page/
    """
    return render(request, '404.html')


def error_500_view(request):
    """
    Custome 500 page
    Inspired by https://www.geeksforgeeks.org/django-creating-a-404-error-page/
    """
    return render(request, '500.html')


class AddTrip(LoginRequiredMixin, View):
    """
    View to host form for users to post a new trip.
    Login required
    trip_form: form, creates new object in Trip model once submitted
    """
    def get(self, request, *args, **kwargs):

        return render(
            request,
            'add_trip.html',
            {'trip_form': TripForm()}
            )

    def post(self, request, *args, **kwargs):
        trip_form = TripForm(request.POST, request.FILES)

        if trip_form.is_valid():
            trip_form.instance.author = request.user
            # Idea for holding temporary data to clean
            # https://www.geeksforgeeks.org/multiplechoicefield-django-forms/
            temp = trip_form.cleaned_data.get('tags')
            trip = trip_form.save(commit=False)
            trip.tags = temp
            trip_form.save()

            slug = trip_form.instance.slug

            return redirect(reverse("post_detail", kwargs={"slug": slug}))
        else:
            data = {
                'title': trip_form.instance.title,
                'caption': recipe_form.instance.caption,
                'featured_image': recipe_form.instance.image,
                'ingredients': recipe_form.instance.ingredients,
                'steps': recipe_form.instance.steps,
                }
            # https://docs.djangoproject.com/en/dev/ref/forms/api/#dynamic-initial-values
            # https://www.reddit.com/r/django/comments/4oie1d/how_to_automatically_prepopulate_data_in_forms/
            return render(
                request,
                'add_trip.html',
                {'trip_form': TripForm(data)}
                )