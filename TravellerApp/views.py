from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Trip
from .forms import CommentForm, TripForm
from django.db.models import Q, Count
from utils.constants import TAGS
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class TripList(generic.ListView):
    model = Trip
    queryset = Trip.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class TripDetail(View):
    """
    Custom view to display full recipe detail
    trip: object, object from Trip model matching the requested slug
    comments: queryset, items from Comment model with matching trip
    foreign key
    comment_form: form, form for users to add comments to Comment model
    liked: boolean, True if user has like recipe
    """
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
    """
    Toggles like status on submission of like form/button on trip page.
    Also sends notification to trip author
    Login required
    """
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
            temp = trip_form.cleaned_data.get('tags')
            trip = trip_form.save(commit=False)
            trip.tags = temp
            trip_form.save()

            slug = trip_form.instance.slug

            return redirect(reverse("post_detail", kwargs={"slug": slug}))
        else:
            data = {
                'title': trip_form.instance.title,
                'slug': trip_form.instance.slug,
                'featured_image': trip_form.instance.featured_image,
                'content': trip_form.instance.content,
                'budget': trip_form.instance.budget,
                'route': trip_form.instance.route,
                'accommodation': trip_form.instance.accommodation,
                'guide': trip_form.instance.guide,
                'additional_info': trip_form.instance.additional_info,
                'tags': trip_form.instance.tags,
                }
            # https://docs.djangoproject.com/en/dev/ref/forms/api/#dynamic-initial-values
            # https://www.reddit.com/r/django/comments/4oie1d/how_to_automatically_prepopulate_data_in_forms/
            return render(
                request,
                'add_trip.html',
                {'trip_form': TripForm(data)}
                )


class EditTrip(LoginRequiredMixin, View):
    """
    View to host form for users to edit their existing trip posts.
    Login required
    trip_form: form, updates instance of trip in model
    once submitted
    trip: object, trip to edit
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Trip.objects.filter(status=1)
        trip = get_object_or_404(queryset, slug=slug)

        trip_form = TripForm(
            instance=trip,
            initial={'tags': trip.list_of_tags}
            )

        return render(
            request,
            'edit_trip.html',
            {
                'trip_form': trip_form,
                'trip': trip
            })

    def post(self, request, slug, *args, **kwargs):
        queryset = Trip.objects.filter(status=1)
        trip = get_object_or_404(queryset, slug=slug)

        trip_form = TripForm(
            request.POST,
            request.FILES,
            instance=trip
            )

        if trip_form.is_valid():
            temp = trip_form.cleaned_data.get('tags')
            trip = trip_form.save(commit=False)
            trip.updated_on = datetime.now()
            trip.tags = temp
            updated_trip = trip_form.save()

            slug = updated_trip.slug

            return redirect(reverse("post_detail", kwargs={"slug": slug}))
        else:
            data = {
                'title': trip_form.instance.title,
                'author': trip_form.instance.author,
                'featured_image': trip_form.instance.featured_image,
                'content': trip_form.instance.content,
                'budget': trip_form.instance.budget,
                'route': trip_form.instance.route,
                'accommodation': trip_form.instance.accommodation,
                'guide': trip_form.instance.guide,
                'additional_info': trip_form.instance.additional_info,
                'tags': trip_form.instance.tags,
                }
            # https://docs.djangoproject.com/en/dev/ref/forms/api/#dynamic-initial-values
            # https://www.reddit.com/r/django/comments/4oie1d/how_to_automatically_prepopulate_data_in_forms/
            return render(
                request,
                'edit_trip.html',
                {
                    'trip_form': TripForm(data),
                    'trip': trip
                    }
                )


@login_required
def delete_comment(request, comment_id):
    """
    Deletes user's comment from the Comment data model when url called.
    Login required
    """
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.commenter:
        comment.delete()

    # Return to previous page from
    # https://stackoverflow.com/questions/50006147/how-to-return-redirect-to-previous-page-in-django-after-post-request
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_trip(request, slug):
    """
    Deletes trip from the Trip data model when url called.
    Login required
    """
    trip = get_object_or_404(Trip, slug=slug)
    if request.user == trip.author:
        trip.delete()

    return redirect('/')