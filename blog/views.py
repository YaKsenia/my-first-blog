from django.shortcuts import render
from django.utils import timezone
from .models import HuckYou
from .models import Murich
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import ImageForm
from django.shortcuts import redirect
from django.forms.models import modelformset_factory
from django.views.generic import ListView
from .models import Post
from .models import Images
from django.template import RequestContext

from django.shortcuts import render_to_response

'''
class HomePageView(ListView):
    #Post.objects.all().order_by('published_date')
    model = Post
    template_name = 'home.html'
    ordering = ['-published_date']
'''
class MurichPageView(ListView):
    #Post.objects.all().order_by('published_date')
    model = Murich
    template_name = 'murich.html'
    ordering = ['-published_date']

class AraPageView(ListView):
    #Post.objects.all().order_by('published_date')
    model = Post
    template_name = 'aryan.html'
    ordering = ['-published_date']


def post_list(request):
    posts = HuckYou.objects.order_by('published_date')
    #.filter(author=request.user, published_date__lte=timezone.now())
    HuckYou.objects.all()
    #Post.objects.get(pk=pk)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(HuckYou, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            for file in request.FILES.getlist('images'):
                instance = ImageForm(
                    post=HuckYou.objects.get(pk=post.pk),
                    image=file
                )
                instance.save()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(HuckYou, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        #image_form = ImageForm(request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            for file in request.FILES.getlist('image'):
                instance = ImageForm(
                    image=file
                )
                instance.save()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
'''

# post=HuckYou.objects.get(pk=post.pk),


#@login_required
def post_edit(request, pk):
    post = get_object_or_404(HuckYou, pk=pk)
    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    if request.method == 'POST':
        postForm = PostForm(request.POST, instance=post)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
        if postForm.is_valid():
            post_form = postForm.save(commit=False)
            post_form.author = request.user
            post_form.published_date = timezone.now()
            if formset.is_valid():
                for form in formset.cleaned_data:
                    image = form['image']
                    photo = Images(post=post_form, image=image)
                    photo.save()
            post_form.save()
            return redirect('post_detail', pk=post.pk)
            messages.success(request,
                                 "Posted!")
            #return HttpResponseRedirect("/")
        #else:
        #    print postForm.errors, formset.errors
    else:
        postForm = PostForm(instance=post)
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'blog/post_edit.html',
                  {'postForm': postForm, 'form': formset})
'''
