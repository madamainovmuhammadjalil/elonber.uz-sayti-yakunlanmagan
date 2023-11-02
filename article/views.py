
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


from .models import Article
from .forms import ArticleCreationForm
class ArticleListView(ListView):
    model = Article
    template_name = 'article_view.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail_view.html'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'summary', 'body')
    template_name = 'update_view.html'

    # def test_func(self):
    #     obj = self.get_object()
    #     return obj.auther == self.request.user

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'delete_view.html'
    success_url = reverse_lazy('article_view')

    # def test_func(self):
    #     obj = self.get_object()
    #     return obj.auther == self.request.user

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'create_view.html'
    fields = ('title', 'summary', 'body', 'photo')
    # form_class = ArticleCreationForm

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)
    # LoginRequiredMixin, UserPassesTestMixin,

    # def post(self, request, *args, **kwargs):
    #     form = ArticleCreationForm(request.POST,request.FILES)
    #     form.instance.auther = self.request.user
    #     return super().form_valid(form)
    #
    #
    #
    #
    # # user superuser ekanini tekshirish
    # def test_func(self):
    #     return self.request.user.is_superuser