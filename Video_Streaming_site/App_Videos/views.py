from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from App_Videos.models import Video_post
from django.urls import reverse, reverse_lazy
from App_Videos.forms import CommentForm
from App_Videos.models import Comment


# Create your views here.

# def video_lists(request):
#     return HttpResponse('unf')


class CreateVideo( LoginRequiredMixin, CreateView):
    model = Video_post
    template_name = 'App_Videos/create_video.html'
    fields = ('link','title','description','category')

    #class based view te form submit er por kaj korbe:
    def form_valid(self, form):
        video_obj = form.save(commit=False)
        video_obj.author = self.request.user  # class er kisu use korte hole age "self." add korte hbe
        title = video_obj.title
        video_obj.save()

        return HttpResponseRedirect(reverse('App_Videos:video_lists'))
    


# class VideoList(ListView):
#     context_object_name = 'video_list'  # this 'blog' will be passed to html as dictionary
#     model = Video_post
#     template_name = 'App_Videos/video_lists.html'

def VideoList(request):
    video_list = Video_post.objects.all()
    results = None

    # search
    if request.method == 'GET':
        # store the keyword, jeta dia search deya hoise
        # search diye username ber kora hbe
        # <input name="search"> oi name string eta
        # full matching seacrh' result = User.objects.filter(username=search)'
        # partial match:'result = User.objects.filter(username__contains=search)'
        # ignore case-sensitivity:  'result = User.objects.filter(username__icontains=search)'
        search = request.GET.get('search', '').strip()

        if search:
            results = Video_post.objects.filter(title__icontains=search)
        #print(result)


    return render(request, 'App_Videos/video_lists.html', context={'video_list': video_list,'results': results})



def video_detail(request, pk):
    video = get_object_or_404(Video_post, pk=pk)

    # comment
    comment_form = CommentForm(request.POST)
    
    if request.method=='POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.video = video   # current video
            comment.save()

            return HttpResponseRedirect(reverse('App_Videos:video_detail', kwargs={'pk':pk}))
    


    return render(request, 'App_Videos/video_detail.html', {'video': video, 'comment_form': comment_form,})

