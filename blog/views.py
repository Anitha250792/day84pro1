from django.views.generic import ListView
from django.db.models import Q
from .models import Post, Category

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        qs = Post.objects.select_related('category').all()
        query = self.request.GET.get('q', '').strip()
        category = self.request.GET.get('category', '').strip()

        if query:
            qs = qs.filter(Q(title__icontains=query) | Q(content__icontains=query))
        if category:
            qs = qs.filter(category__name=category)
        return qs.order_by('-published_date')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.all()
        ctx['q'] = self.request.GET.get('q', '')
        ctx['selected_category'] = self.request.GET.get('category', '')
        return ctx
