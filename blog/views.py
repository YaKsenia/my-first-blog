from __future__ import unicode_literals
from django.utils import timezone
from .models import HuckYou
from .models import Murich
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import ImageForm
from django.shortcuts import redirect
from django.views.generic import ListView
from .models import Post
from .models import Images
from hitcount.views import HitCountDetailView


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
    posts = HuckYou.objects.order_by('-published_date')
    images = Images.objects.order_by('-image')
    #.filter(author=request.user, published_date__lte=timezone.now())
   # HuckYou.objects.all()
    #Post.objects.get(pk=pk)
    return render(request, 'blog/post_list.html', {'posts': posts, 'images' : images})


def post_images(request, slug):
    image = get_object_or_404(Images, slug = slug)
    return render(request, 'blog/post_images.html', {'image': image})



def practice(request):
    practice_posts = HuckYou.objects.filter(label='practice').order_by('published_date')
    images = Images.objects.order_by('image')
    #.filter(author=request.user, published_date__lte=timezone.now())
   # HuckYou.objects.all()
    #Post.objects.get(pk=pk)
    return render(request, 'blog/practice.html', {'practice_posts': practice_posts, 'images' : images})


def theory(request):
    theory_posts = HuckYou.objects.filter(label='theory').order_by('published_date')
    images = Images.objects.order_by('image')
    #.filter(author=request.user, published_date__lte=timezone.now())
   # HuckYou.objects.all()
    #Post.objects.get(pk=pk)
    return render(request, 'blog/theory.html', {'theory_posts': theory_posts, 'images' : images})

def about(request):
    posts = HuckYou.objects.order_by('published_date')
    #.filter(author=request.user, published_date__lte=timezone.now())
    HuckYou.objects.all()
    #Post.objects.get(pk=pk)
    return render(request, 'blog/about.html', {'posts': posts})

'''
def post_detail(request, pk):
    post = get_object_or_404(HuckYou, pk=pk)
    posts = HuckYou.objects.order_by('published_date')
    return render(request, 'blog/post_detail.html', {'post': post, 'posts': posts})
'''


class PostDetailView(HitCountDetailView):
    model = HuckYou
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': HuckYou.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context



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

class MainNavigationBaseTab(TabView):
    """Base class for all main navigation tabs."""
    tab_group = 'main_navigation'
    tab_classes = ['main-navigation-tab']

    def get_context_data(self, **kwargs):
        context = super(MainNavigationBaseTab, self).get_context_data(**kwargs)
        context['theory'] = 'theory'
        return context

    @property
    def tab_classes(self):
        """If user is logged in, set ``logged_in_only`` class."""
        classes = super(MainNavigationBaseTab, self).tab_classes[:]
        if self.current_tab.request.user.is_authenticated():
            classes += ['logged_in_only']
        return classes

class TheoryTab(MainNavigationBaseTab):
    _is_tab = True
    tab_id = 'theory'
    tab_group = 'main_navigation'
    tab_label = 'Theory'
    template_name = 'blog/post_list.html'



class PracticeTab(MainNavigationBaseTab):
    _is_tab = True
    tab_id = 'practice'
    tab_group = 'main_navigation'
    tab_label = 'Practice'
    template_name = 'blog/tabs.html'





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
