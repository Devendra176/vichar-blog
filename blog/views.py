from django.shortcuts import render
from django.shortcuts import redirect

from .models import Post
from .models import Registeruser
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from django.contrib import messages


from django.views.generic import TemplateView,ListView,UpdateView,DetailView,DeleteView

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.urls import reverse	
from django.shortcuts import get_object_or_404

def logout(request):
	request.session.delete()
	return redirect('blog-home')


# to display home page and about page

class Homeview(TemplateView):
	template_name='frontpage/home.html'


class Homeaboutview(TemplateView):
	template_name='frontpage/about.html'
# -------------------------------------------------------


# used CreateView for user registration

class  RegistrationView(CreateView):
	template_name='user/registration.html'
	model=Registeruser
	fields='__all__'


	def post(self,request):
		fullname=request.POST['fullname']
		email=request.POST['email']
		contact=request.POST['contact']
		password=request.POST['password']
		check_reg = Registeruser.objects.filter(email=email).exists()
		check_username = User.objects.filter(username=fullname).exists()
		if not check_reg and not check_username:
			user=User.objects.create_user(username=fullname,password=password)
			userdata=Registeruser(user_id=user.id,contact=contact,email=email)
			userdata.save()
			messages.success(request,"you are ready to login")
			return redirect('blog-signin')
		else:
			messages.error(request,"username alredy exist")
			datas={
			'fullname': fullname,
			'email': email,
			'contact': contact,
			}
			return redirect('blog-registration')
# -------------------------------------------------------------------------------------------------------		

# used TemplateView for display login page and used post function for login the user

class Loginview(TemplateView):
	template_name='user/signin.html'
	success_url=reverse_lazy('blog-main')

	def post(self,request):
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		
		if user is not None:
			login(request,user)
			return HttpResponseRedirect(self.success_url)
		else:
			messages.error(request,"invalid credential")
			return redirect('blog-signin')



# for Blog's list used ListView

class BlogListView(ListView):
	model=Post
	template_name = 'post/all_post.html'
	ordering = ['-id']
	paginate_by =3
	def get_context_data(self, **kwargs):		
		context = super().get_context_data(**kwargs)
		pk=self.request.user.pk

		context['profile'] = Registeruser.objects.filter(user_id=pk).first()
		return context
# -----------------------------------------------------------------------------------------------

# to show a full blog used DetailView

class BlogIndiviualView(DetailView):
	model = Post
	template_name = 'post/post_detail.html'
	def get_context_data(self,*args,**kwargs):
		pk=self.kwargs.get("pk")
		context = super().get_context_data(**kwargs)
		a=Post.objects.filter(id=pk).first()
		context['profile']=Registeruser.objects.filter(id=a.author_id).first()
		return context
# ----------------------------------------------------------------------------------------------------

# to create blog post , I'm using html forms for post the data

class CreateBlogPost(CreateView):
	model=Post
	template_name ='post/post_form.html'
	fields=['title','content','author','blogphoto']
	success_url=reverse_lazy('blog-main')

	def get_context_data(self, **kwargs):
		kwargs['naming'] = 'Save'
		context = super(CreateBlogPost, self).get_context_data(**kwargs)
		pk=self.request.user.pk
		context['profile']=Registeruser.objects.filter(user_id=pk).first()
		return context
		
	def post(self,request):		
		id_=request.user.pk
		check_profile = Registeruser.objects.filter(user_id=id_).first()
		author=check_profile.id
		img=request.FILES.get('img')
		title=request.POST['title']
		content=request.POST['content']
		if 'img' in request.FILES:
			if check_profile:
				blog_post = Post.objects.create(author_id=author,title=title,content=content,blogphoto=img)
				messages.success(self.request,"your post created")
				return HttpResponseRedirect(self.success_url)
		else:
			blog_post = Post.objects.create(author_id=author,title=title,content=content)
			messages.success(self.request,"your post created")
			return HttpResponseRedirect(self.success_url)					



# -------------------------------------------------------------------------------------------------------------

# used updateview for edit the blog post and same template as i used for createing blog post

class PostUpdateview(UpdateView):
	model=Post
	template_name ='post/post_form.html'
	fields=['title','content','author','blogphoto']
	success_url=reverse_lazy('blog-main')

	def get_context_data(self, **kwargs):

		kwargs['naming']='Update'
		context = super(PostUpdateview, self).get_context_data(**kwargs)
		pk=self.request.user.pk
		
		context['profile']=Registeruser.objects.filter(user_id=pk).first()
		return context
	def post(self,form,**kwargs):
		pk=self.kwargs.get("pk")
		img=self.request.FILES.get('img')
		title=self.request.POST['title']
		content=self.request.POST['content']
		blog_post = Post.objects.filter(id=pk)
		
		if 'img' in self.request.FILES:
			blog_post.update(title=title,content=content)
			a=Post.objects.get(id=pk)
			a.blogphoto=img
			a.save()
			messages.success(self.request,"your post updated")
			return HttpResponseRedirect(self.success_url)
			
		else:
			blog_post.update(title=title,content=content)
			messages.success(self.request,"your post updated")
			
			return HttpResponseRedirect(self.success_url)


# -----------------------------------------------------------------------------------------------------

# using the DeleteView for deleting the post, using ajax to send data

class PostDeleteView(DeleteView):
	model=Post
	success_url = reverse_lazy('blog-main')
	
	def get_object(self):
		id=self.kwargs.get("pk")
		return get_object_or_404(Post,id=id)

# ------------------------------------------------------------------------------------------------------


# using DetailView for showing profile and  blog post which has been posted by the user 

class ProfileView(DetailView):
	model=Registeruser
	# template_name='blog/userprofile.html'
	template_name = 'userprofile/profile.html'
	ordering=['-id']

	def get_context_data(self,*args,**kwargs):
		context = super(ProfileView, self).get_context_data(**kwargs)
		activities= self.get_related_activities()
		context['object_list'] = activities
		context['page_obj'] = activities
		return context

# used get_related_activities function for showing blog post with pagination 
   # and for user profile data i already defined model and context_object_name name is registeruser by default

	def get_related_activities(self):
		pk=self.kwargs.get("pk")
		queryset = Post.objects.filter(author_id=pk)
		return queryset


	def post(self,form,**kwargs):
		pk=self.kwargs.get("pk")
		data=Registeruser.objects.get(id=pk)
		print(self.request.FILES)
		cover_img=self.request.FILES.get("coverpic_id")
		profile_img=self.request.FILES.get("change_profile_pic")
		# username=self.request.POST.get("username")
		# newpassword=self.request.POST.get("newpassword")
		# Profession=self.request.POST.get("Profession")
		# bio=self.request.POST.get("bio")
		if cover_img or profile_img:
			if cover_img:
				data.coverphoto=cover_img
				data.save()
				msg="cover pic changed "
				messages.success(self.request,msg)
				return redirect("blog-userprofile",pk)
			if profile_img:
				data.photo=profile_img
				data.save()
				msg="profile pic changed "
				messages.success(self.request,msg)
				return redirect("blog-userprofile",pk)
		msg='Choose File'
		messages.error(self.request,msg)
		return redirect("blog-userprofile",pk)