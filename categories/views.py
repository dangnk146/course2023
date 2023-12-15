from django.shortcuts import render

from .models import *
from users.models import *

from users.helper import *


# Create your views here.
def ManageHomePage(request):
    user = User.objects.get(username=request.user.username)    
    data = GetUser(user)  
    
    d = {'data': data, }
    return render(request, 'dashboardHomePage.html', d)

def ManageHomePageCategory(request):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        data = GetUser(user)

        categories = Category.objects.all()
        warring = False

        try:
            Category.objects.get(name="News")
        except:
            warring = True

        d = {'data': data, 'categories': categories, 'warring':warring }
        return render(request, 'manageHomePageCategory.html', d)
    if request.method == "POST":
        category_name = request.POST["category"]
        is_notsubcategory = request.POST.get("is_notsubcategory")
        notsubcategory = False
        if is_notsubcategory:
           notsubcategory = True 
        if (category_name):
            category = Category.objects.create(name=category_name, is_notsubcategory=notsubcategory)
            if category.is_notsubcategory==True:
                SubCategory.objects.create(name="none", category=category)
            return redirect('manageHomePageCategory')
        return redirect('manageHomePageCategory')

def ManageHomePageCategoryEdit(request, category_id):
    user = User.objects.get(username=request.user.username)
    
    category = get_object_or_404(Category, id=category_id)
    if request.method == "GET":
        data = GetUser(user)
        d = {'data': data, 'category': category}
        return render(request, 'manageHomePageCategoryEdit.html', d)
    if request.method == "POST":
        new_category_name  = request.POST['category']

        category.name = new_category_name
        category.save()  # Save the changes to the database

        return redirect('manageHomePageCategory')

def ManageCategoryDelete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('manageHomePageCategory')

def ManageSubcategory(request, category_id):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    category = Category.objects.get(id=category_id)
    
    subcategories = SubCategory.objects.filter(category=category)
    
    result=''    
    if request.method == "GET":
        d = {'data': data, 'subcategories': subcategories, 'result':result, 'category': category }
        return render(request, 'manageSubCategory.html', d)
    if request.method == "POST":        
        name_subcategory  = request.POST['name_subcategory']        
        if (category_id and name_subcategory):
            SubCategory.objects.create(name=name_subcategory, category=category)
        return redirect('manageHomePageSubcategory', category.id)

def ManageSubcategoryEdit(request, category_id, subcategory_id):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    category = Category.objects.get(id=category_id)
    
    subcategory = SubCategory.objects.get(id=subcategory_id)
    result=''    
    if request.method == "GET":
        d = {'data': data, 'subcategory': subcategory, 'result':result, 'category': category }
        return render(request, 'manageSubCategoryEdit.html', d)
    if request.method == "POST":        
        name_subcategory  = request.POST['name_subcategory']        
        if (category_id and name_subcategory and subcategory.name != name_subcategory):
            subcategory.name = name_subcategory
            subcategory.save()
        return redirect('manageHomePageSubcategory', category.id)

def ManageSubCategoryDelete(request, category_id, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    subcategory.delete()
    return redirect('manageHomePageSubcategory', category_id)

def ManageBlogs(request, category_id, subcategory_id=""):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    category = Category.objects.get(id=category_id)
    subcategory=''

    if subcategory_id:
        subcategory = SubCategory.objects.get(id=subcategory_id)
    else:
        subcategory = SubCategory.objects.filter(category=category).first()

    blogs = Blogs.objects.filter(subcategory=subcategory)
    result=''    
    d = {'data': data, 'blogs': blogs, 'subcategory': subcategory, 'result':result, 'category': category }
    return render(request, 'manageBlogs.html', d)

def ManageBlogsAdd(request, category_id, subcategory_id):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    category = Category.objects.get(id=category_id)
    
    subcategory = SubCategory.objects.get(id=subcategory_id)    
    if request.method == "GET":
        result=''    
        d = {'data': data,'subcategory': subcategory, 'result':result, 'category': category }
        return render(request, 'manageBlogsAdd.html', d)
    if request.method == "POST":
        name  = request.POST.get('name', '')
        image  = request.POST.get('image', '')
        linkvideo  = request.POST.get('linkvideo', '')
        linkredirect  = request.POST.get('linkredirect', '')
        content  = request.POST.get('content', '')
        Blogs.objects.create(name=name, images= image, linkvideo=linkvideo, linkredirect = linkredirect, content=content, subcategory=subcategory)
        return redirect('manageHomePagBlogs', category.id, subcategory.id)


def ManageBlogsEdit(request, category_id, subcategory_id, blog_id):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    category = Category.objects.get(id=category_id)
    
    subcategory = SubCategory.objects.get(id=subcategory_id)  
    blog = Blogs.objects.get(id=blog_id)  
    if request.method == "GET":
        result=''    
        d = {'data': data, 'blog': blog,'subcategory': subcategory, 'result':result, 'category': category }
        return render(request, 'manageBlogsEdit.html', d)
    if request.method == "POST":
        name  = request.POST.get('name', '')
        image  = request.POST.get('image', '')
        linkvideo  = request.POST.get('linkvideo', '')
        linkredirect  = request.POST.get('linkredirect', '')
        content  = request.POST.get('content', '')
        if (name and blog.name != name):
            blog.name = name
        if (image and blog.image != image):
            blog.image = image
        if (linkvideo and blog.linkvideo != linkvideo):
            blog.linkvideo = linkvideo
        if (linkredirect and blog.linkredirect != linkredirect):
            blog.linkredirect = linkredirect
        if (content and blog.content != content):
            blog.content = content
        blog.save()
        return redirect('manageHomePagBlogs', category.id, subcategory.id)

def ManageBlogsDelete(request, category_id, subcategory_id, blog_id):
    user = User.objects.get(username=request.user.username)
    data = GetUser(user)
    category = Category.objects.get(id=category_id)
    
    subcategory = SubCategory.objects.get(id=subcategory_id)  
    blog = Blogs.objects.get(id=blog_id) 
    blog.delete()
    return redirect('manageHomePagBlogs', category.id, subcategory.id)