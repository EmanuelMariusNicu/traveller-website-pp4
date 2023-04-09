from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Trip
from .forms import CommentForm
from django.db.models import Q
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
    # Tutorial to retrieve search term available at
    # https://www.youtube.com/watch?v=AGtae4L5BbI
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