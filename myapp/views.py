from django.shortcuts import render, redirect
from django.http import HttpResponse
import logging
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Posts, Category
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404




@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

#static data
# posts = [
#         {'id':1,'title': 'post1', 'content':'content of post1'},
#         {'id':2,'title': 'post2', 'content':'content of post2'},
#         {'id':3,'title': 'post3', 'content':'content of post3'},
#         {'id':4,'title': 'post4', 'content':'content of post4'}
#   
#]



#using APIView also we can do the crud operations
class PostView(APIView):
    # Define the get_object method to fetch a post by its ID
    def get_object(self, post_id):
        # This method will return a post or raise a 404 if it doesn't exist
        return get_object_or_404(Posts, id=post_id)

    def get(self, request, post_id=None):
        if post_id:
            try:
                post=Posts.objects.get(id=post_id)

                post_data={
                    "id" :post.id,
                    "title":post.title,
                    "content":post.title,
                    "img_url":post.img_url,
                    "category":{
                        "id":post.category.id if post.category else None,
                        "name":post.category.name if post.category else None
                    }
                }
                return Response(post_data)
            except Posts.DoesNotExist:
                return Response({"error": "Post not found"})
        
        else:
            # Fetch all posts and include category ID and name
            posts = Posts.objects.all()
            posts_data = []
            for post in posts:
                posts_data.append({
                    "id": post.id,
                    "title": post.title,
                    "content": post.content,
                    "img_url": post.img_url,
                    "category": {
                        "id": post.category.id if post.category else None,  # Get category ID
                        "name": post.category.name if post.category else None  # Get category name
                    }
                })
            return Response(posts_data)     
    # POST method for creating a new post
    def post(self, request):
        data = request.data

        # Create or get the category
        category_name = data.get('category')
        category, created = Category.objects.get_or_create(name=category_name)

        # Create the post
        post = Posts.objects.create(
            title=data["title"],
            content=data["content"],
            img_url=data.get("img_url"),
            category=category  # Assign the category
        )
        return Response({
            "message": "Post created successfully",
            "post_id": post.id,
            "category_id": category.id
        })

    def put(self, request, post_id):
        try:
            post = Posts.objects.get(id=post_id)
        except Posts.DoesNotExist:
            return Response({"error": "Post not found"})

        data = request.data

        # Update the post fields
        post.title = data.get("title", post.title)
        post.content = data.get("content", post.content)
        post.img_url = data.get("img_url", post.img_url)

        # Check for category and get or create it
        category_name = data.get('category')
        if category_name:
            category, created = Category.objects.get_or_create(name=category_name)
            post.category = category  # Assign the new category if provided

        post.save()  # Save the updated post

        return Response({
            "message": "Post updated successfully",
            "post_id": post.id,
            "category_id": post.category.id  # Return the updated category ID
        })

    def patch(self, request, post_id):
        post = self.get_object(post_id)

        # Only update fields provided in the request
        title = request.data.get('title')
        content = request.data.get('content')
        img_url = request.data.get('img_url')

        if title:
            post.title = title
        if content:
            post.content = content
        if img_url:
            post.img_url = img_url

        post.save()  # Save the updated post

        return Response({
            'id': post.id,
            'title': post.title,
            
        })
    # DELETE method for removing an existing post
    def delete(self, request, post_id):
        # Fetch the post or return a 404 if it doesn't exist
        post = self.get_object(post_id)
        
        # Delete the post
        post.delete()
        return Response({"message": "Post deleted successfully"})


def index_view(request):
    blog_title = "Latest Posts"
    
    posts = Posts.objects.all().order_by('id')
    return render(request,'index.html', {'blog_title': blog_title, 'posts':posts})


def details(request, slug):
    #post = next((item for item in posts if item['id']==int(post_id)), None)
    # logger=logging.getLogger('TESTING')
    # logger.debug(f'post variable is:{post}')
    try:
        # getting data from model by post id
        post = Posts.objects.get(slug=slug)
        related_posts  = Posts.objects.filter(category = post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404("Post Does not Exist!")
    return render(request,'details.html', {'post':post, 'related_posts':related_posts})

def old_url_redirect(request):
    return redirect('new_url')

def newurl(request):
    return HttpResponse("this is new url")