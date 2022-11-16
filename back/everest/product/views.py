from django.shortcuts import render


def comment(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        post = self.get_object()
        form.instance.user = request.user
        form.instance.post = post
        form.save()
        # return redirect(reverse('detail', kwargs={'categories_blog': post.slug}))
    user = request.user
