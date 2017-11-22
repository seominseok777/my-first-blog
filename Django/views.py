from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import  PostForm
# Create your views here.

def post_list(request):
    contacts = Post.objects.all()
    search = request.GET.get('search')

    if search:
        contacts=contacts.filter(title__icontains=search)

    paginator = Paginator(contacts,10)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    index = contacts.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    return render(request, 'Django/post_list.html', {
        'contacts': contacts,
        'page_range': page_range,
    })

def post_detail(request,id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'Django/post_detail.html', {'post':post,})

def post_writing(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('/Django')
    else:
        form = PostForm
    return render(request, 'Django/post_write.html',{'form':form,})
