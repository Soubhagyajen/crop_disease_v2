from django.shortcuts import render,get_object_or_404

def landing_page(request):
    return render(request, 'landing.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def how_it_works(request):
    return render(request, 'how_it_works.html')

# def blogs(request):
#     return render(request, 'blogs.html')

def contact(request):
    return render(request, 'contact.html')




from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def blog_list(request):
    query = request.GET.get('q')  # Search feature
    if query:
        blogs = Blog.objects.filter(title__icontains=query)
    else:
        blogs = Blog.objects.all().order_by('-created_at')  # Show latest blogs first

    return render(request, "blog_list.html", {"blogs": blogs})

# def add_blog(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('blog_list')
#     else:
#         form = BlogForm()
    
#     return render(request, 'add_blog.html', {'form': form})

# def add_blog(request):
#     if request.method == "POST":
#         form = BlogForm(request.POST, request.FILES)  # Handle images
#         if form.is_valid():
#             form.save()  # Save to DB
#             return redirect('blog_list')  # Redirect to blog list page
#     else:
#         form = BlogForm()
#     return render(request, "add_blog.html", {"form": form})


def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)  # Don't save yet
            blog.author = "Anonymous"  # Set a default author if needed
            blog.save()
            return redirect("blog_list")  # Redirect to blog list
    else:
        form = BlogForm()
    return render(request, "add_blog.html", {"form": form})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, "blog_detail.html", {"blog": blog})



def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)  # Get the blog or return 404
    if request.method == "POST":
        blog.delete()  # Delete the blog
        return redirect("blog_list")  # Redirect to blog list after deletion
    return render(request, "delete_blog.html", {"blog": blog})