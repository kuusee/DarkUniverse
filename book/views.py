from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from .models import Books
from datetime import datetime, timedelta
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator


class Home(ListView):
    paginate_by = 10
    model = Books
    template_name = "book/content.html"
    context_object_name = "posts"
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context["title"] = "Главная страница"
        return context

    def get_queryset(self):
        if self.request.GET.get("input_page"):
            print(self.request.GET.get)
        if self.request.GET.get("search_by") == "words":
            print(self.request.GET.get("search_by"))
            if self.request.GET.get("words"):
                query = self.request.GET.get("words")
                search = SearchVector("description", "name", "author")
                queryset = Books.objects.annotate(
                    search=search,
                ).filter(search=query)
                return queryset

        if self.request.GET.get("search_by") == "full":
            print(self.request.GET.get("search_by"))
            if self.request.GET.get("words"):
                query = self.request.GET.get("words")
                search = SearchVector("description", "name", "author")
                queryset = Books.objects.annotate(
                    search=search,
                ).filter(search=query)
            else:
                if self.request.GET["public-data-min"]:
                    data_min = datetime.strptime(
                        self.request.GET["public-data-min"], "%Y-%m-%d"
                    )
                else:
                    data_min = datetime.strptime("1962-03-09", "%Y-%m-%d")

                if self.request.GET["public-data-max"]:
                    data_max = datetime.strptime(
                        self.request.GET["public-data-max"], "%Y-%m-%d"
                    )
                else:
                    data_max = datetime.now()

                if data_min == data_max:
                    data_max += timedelta(days=1)

                if self.request.GET["source"] == "1":
                    queryset = Books.objects.all().filter(
                        date__range=[data_min, data_max]
                    )
                elif self.request.GET["source"] == "2":
                    queryset = Books.objects.all().filter(
                        Q(date__range=[data_min, data_max]) &
                        Q(public_site=True)
                    )

                elif self.request.GET["source"] == "3":
                    queryset = Books.objects.all().filter(
                        Q(date__range=[data_min, data_max]) & Q(public_tg=True)
                    )

                if self.request.GET["title"] and self.request.GET["author"]:
                    queryset = queryset.filter(
                        Q(name__search=self.request.GET["title"])
                        & Q(author__search=self.request.GET["author"])
                    )

                elif self.request.GET["title"]:
                    queryset = queryset.filter(
                        name__search=self.request.GET["title"])

                elif self.request.GET["author"]:
                    queryset = queryset.filter(
                        author__search=self.request.GET["author"]
                    )
            return queryset
        return Books.objects.all()


def search(request):
    context = {}
    if request.GET.get("words"):
        query = request.GET.get("words")
        search = SearchVector("description", "name", "author")
        posts = Books.objects.annotate(
            search=search,
        ).filter(search=query)
    else:
        if request.GET["public-data-min"]:
            data_min = datetime.strptime(
                request.GET["public-data-min"], "%Y-%m-%d")
        else:
            data_min = datetime.strptime("1962-03-09", "%Y-%m-%d")

        if request.GET["public-data-max"]:
            data_max = datetime.strptime(
                request.GET["public-data-max"], "%Y-%m-%d")
        else:
            data_max = datetime.now()

        if data_min == data_max:
            data_max += timedelta(days=1)

        if request.GET["source"] == "1":
            posts = Books.objects.all().filter(
                date__range=[data_min, data_max])

        elif request.GET["source"] == "2":
            posts = Books.objects.all().filter(
                Q(date__range=[data_min, data_max]) & Q(public_site=True)
            )

        elif request.GET["source"] == "3":
            posts = Books.objects.all().filter(
                Q(date__range=[data_min, data_max]) & Q(public_tg=True)
            )

        if request.GET["title"] and request.GET["author"]:
            posts = posts.filter(
                Q(name__search=request.GET["title"])
                & Q(author__search=request.GET["author"])
            )

        elif request.GET["title"]:
            posts = posts.filter(name__search=request.GET["title"])

        elif request.GET["author"]:
            posts = posts.filter(author__search=request.GET["author"])

    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    context["title"] = "Главная страница"
    context["posts"] = page_obj
    return render(request, "book/search.html", context=context)


def about(request):
    context = {"title": "Главная страница"}
    return render(request, "book/about.html", context=context)


class Post(DetailView):
    model = Books
    template_name = "book/post.html"
    pk_url_kwarg = "post_id"
    context_object_name = "post"


def pageNotFound(request, exception):
    return HttpResponseNotFound("404")
