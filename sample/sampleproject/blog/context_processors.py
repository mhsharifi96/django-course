
from .models import Post
# reference :https://stackoverflow.com/questions/60515797/default-context-for-all-pages-django

def add_variable_to_context(request):
    return {
        'context_last_posts': Post.objects.order_by('id').all()[:4],
        # 'categories': Category.objects.order_by("id").all(),
    }