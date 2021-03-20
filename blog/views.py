from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.core.mail import send_mail
from django.contrib import messages
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView
)


def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

@login_required
def PostCreateView(request):
    if request.method== 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save() 
            
            messages.success(request, f'Your hospital is registered!')
            return redirect("blog-home")
    else:
        form=PostForm()
        context = {
            "form": form,
        }
        return render(request,'blog/post_form.html',context)

@login_required
def PostDetailView(request,pk):
    if request.method== 'POST':
        form=BedForm(request.POST)
        if form.is_valid():
            # form.save()
            donation =Donation()
            post = get_object_or_404(Post, pk=pk)
            donation.receiver= request.user
            donation.donor= post.author
            donation.City= post.district
            donation.Hospital = post.author.profile.Hospital
            donation.save()
            send_mail('Health-a-gram has some great news for you',f' {request.user} ({request.user.email}) needs your help!',settings.EMAIL_HOST_USER,[f'{post.author.email}'],fail_silently=False)
            messages.success(request, f'We have notified the Donor, thankyou for the using Health-a-gram')
            return redirect('dash-view')
        else:
            pass
    else:
        # form=BedForm()
        context = {
            # "form": form,
            "post": get_object_or_404(Post, pk=pk),
        }
        return render(request,'blog/post_detail.html',context)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['name', 'content', 'covid_cap', 'norm_cap', 'city',
                'address'
            ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

