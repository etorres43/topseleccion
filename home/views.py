from django.shortcuts import render
from .forms  import SearchForm,PcommentForm, ScommentForm
from django.utils import timezone
from .models import Main_post, Profile, Tag_list,Comments,Reply
from django.db.models import Q
from django.db import connection

# Create your views here.
def tags_funct():
	all_posts = Main_post.objects.order_by('-Post_score')
	all_tags = Tag_list.objects.all()
	
	tag_list = str()
	cur = connection.cursor()
	post_tag = {}

	for post in all_posts:
		tag_list = []
		cur.execute('SELECT tag_list_id FROM home_main_post_Tag  WHERE main_post_id is '+str(post.pk)+';')
		items = cur.fetchall()
		for i in items:
			tag_list=i[0]

		post_tag.update({ post.pk : tag_list})
		#print(post_tag.keys())

	cur.close()
	return post_tag

def index(request):
	template = 'home/home.html'
	page_template = 'home/c_mainpage.html'
	Search_form = SearchForm(request.GET)
	Today = timezone.now().date()
	all_posts = Main_post.objects.order_by('-Post_date')
	top_posts = Main_post.objects.order_by('Post_date')[:5]
	all_tags = Tag_list.objects.all()
	all_profiles = Profile.objects.all()
	TAG = ''
	post_tag = tags_funct()

	context = {
		'all_posts': all_posts,	
		'page_template': page_template,
		'Search_form':Search_form,
		'all_profiles': all_profiles,
		'Today':Today,
		'post_tag':post_tag.items(),
		'top':top_posts,

	}


	return render(request, template, context)

def DetailView(request,pk):
	post = Main_post.objects.filter(pk=pk)
	template = 'home/home.html'
	page_template = 'home/Post_view.html'
	Search_form = SearchForm(request.GET)
	Today = timezone.now().date()
	all_posts = Main_post.objects.order_by('-Post_date')
	top_posts = Main_post.objects.order_by('Post_date')[:5]
	all_tags = Tag_list.objects.all()
	all_profiles = Profile.objects.all()
	all_comments = Comments.objects.all()
	all_scomments = Reply.objects.all()
	Pcomment_form = PcommentForm(request.POST)
	Scomment_form = ScommentForm(request.POST)
	TAG = ''
	post_tag = tags_funct()

	context = {
		#'all_posts': all_posts,
		'post': post,	
		'page_template': page_template,
		'Search_form':Search_form,
		'all_profiles': all_profiles,
		'Today':Today,
		'post_tag':post_tag.items(),
		'all_comments': all_comments,
		'all_scomments': all_scomments,
		'Pcomment_form':Pcomment_form,
		'Scomment_form':Scomment_form,
		'top':top_posts,

	}


	return render(request, template, context)
	
def Ubermensch(request):
	template = 'home/home.html'
	page_template = 'home/c_mainpage.html'
	Search_form = SearchForm(request.GET)
	top_posts = Main_post.objects.order_by('Post_date')[:5]
	Today = timezone.now().date()
	all_posts = Main_post.objects.order_by('-Post_date')
	all_tags = Tag_list.objects.all()
	all_profiles = Profile.objects.all()
	TAG = ''
	post_tag = tags_funct()
	
	cur = connection.cursor()


	cur.execute('SELECT main_post_id FROM home_main_post_Tag  WHERE Tag_list_id is 1;')
	post_id = cur.fetchall()

	count = 0
	for i in post_id:
		all_posts = Main_post.objects.filter(pk=i[0])
		if count >= 1:
			all_posts = all_posts | all_posta
		all_posta = all_posts
	
		count +=1
	all_posts = all_posts.order_by('-Post_date')
	
		
	cur.close()
	

	context = {
		'all_posts': all_posts,	
		'page_template': page_template,
		'Search_form':Search_form,
		'all_profiles': all_profiles,
		'Today':Today,
		'post_tag':post_tag.items(),
		'top':top_posts,

	}
	
	
	return render(request, template, context)
	
def Pensamientos(request):
	template = 'home/home.html'
	page_template = 'home/c_mainpage.html'
	top_posts = Main_post.objects.order_by('Post_date')[:5]
	Search_form = SearchForm(request.GET)
	Today = timezone.now().date()
	all_posts = Main_post.objects.order_by('-Post_date')
	all_tags = Tag_list.objects.all()
	all_profiles = Profile.objects.all()
	TAG = ''
	post_tag = tags_funct()
	
	cur = connection.cursor()


	cur.execute('SELECT main_post_id FROM home_main_post_Tag  WHERE Tag_list_id is 2;')
	post_id = cur.fetchall()

	count = 0
	for i in post_id:
		all_posts = Main_post.objects.filter(pk=i[0])
		if count >= 1:
			all_posts = all_posts | all_posta
		all_posta = all_posts
	
		count +=1
	all_posts = all_posts.order_by('-Post_date')
	
		
	cur.close()
	

	context = {
		'all_posts': all_posts,	
		'page_template': page_template,
		'Search_form':Search_form,
		'all_profiles': all_profiles,
		'Today':Today,
		'post_tag':post_tag.items(),
		'top':top_posts,

	}
	
	
	return render(request, template, context)
	
def Historias(request):
	template = 'home/home.html'
	page_template = 'home/c_mainpage.html'
	Search_form = SearchForm(request.GET)
	top_posts = Main_post.objects.order_by('Post_date')[:5]
	Today = timezone.now().date()
	all_posts = Main_post.objects.order_by('-Post_date')
	all_tags = Tag_list.objects.all()
	all_profiles = Profile.objects.all()
	TAG = ''
	post_tag = tags_funct()
	
	cur = connection.cursor()


	cur.execute('SELECT main_post_id FROM home_main_post_Tag  WHERE Tag_list_id is 3;')
	post_id = cur.fetchall()

	count = 0
	for i in post_id:
		all_posts = Main_post.objects.filter(pk=i[0])
		if count >= 1:
			all_posts = all_posts | all_posta
		all_posta = all_posts
	
		count +=1
	all_posts = all_posts.order_by('-Post_date')
	
		
	cur.close()
	

	context = {
		'all_posts': all_posts,	
		'page_template': page_template,
		'Search_form':Search_form,
		'all_profiles': all_profiles,
		'Today':Today,
		'post_tag':post_tag.items(),
		'top':top_posts,

	}
	
	
	return render(request, template, context)

def Ciencia(request):
	template = 'home/home.html'
	page_template = 'home/c_mainpage.html'
	Search_form = SearchForm(request.GET)
	top_posts = Main_post.objects.order_by('Post_date')[:5]
	Today = timezone.now().date()
	all_posts = Main_post.objects.order_by('-Post_date')
	all_tags = Tag_list.objects.all()
	all_profiles = Profile.objects.all()
	TAG = ''
	post_tag = tags_funct()
	
	cur = connection.cursor()


	cur.execute('SELECT main_post_id FROM home_main_post_Tag  WHERE Tag_list_id is 4;')
	post_id = cur.fetchall()

	count = 0
	for i in post_id:
		all_posts = Main_post.objects.filter(pk=i[0])
		if count >= 1:
			all_posts = all_posts | all_posta
		all_posta = all_posts
	
		count +=1
	all_posts = all_posts.order_by('-Post_date')
	
		
	cur.close()
	

	context = {
		'all_posts': all_posts,	
		'page_template': page_template,
		'Search_form':Search_form,
		'all_profiles': all_profiles,
		'Today':Today,
		'post_tag':post_tag.items(),
		'top':top_posts,

	}
	
	
	return render(request, template, context)

def Search(request):
	all_posts = Main_post.objects.order_by('-Post_date')
	Search_form = SearchForm(request.GET)
	Search_item = request.GET.get("search_field")
	all_profiles = Profile.objects.all()
	template = 'home/home.html'
	page_template = 'home/c_mainpage.html'

	Today = timezone.now().date()

	if Search_item:
		all_posts = all_posts.filter(Q(Title__icontains=Search_item) |Q(Post_content__icontains=Search_item) )
		if not all_posts:
			messages.error(request, 'Search result for {' + Search_item + '} was not found, but here are other posts you might like')
			all_posts = Main_post.objects.order_by('Post_score')

	context = {
		'all_posts': all_posts,	
		'Search_form':Search_form,
		'page_template': page_template,
		'Today':Today,
	}



	return render(request, template, context)
	
def Post_comment(request,pk):
	post = Main_post.objects.filter(pk=pk)
	template = 'home/home.html'
	page_template = 'home/Post_view.html'
	all_comments = Comments.objects.all()
	top_posts = Main_post.objects.order_by('Post_date')[:5]
	all_scomments = Reply.objects.all()
	Pcomment_form = PcommentForm(request.POST)
	Scomment_form = ScommentForm(request.POST)
	all_profiles = Profile.objects.all()
	pk = int(pk)

	if request.method == 'POST':
		p_comment = request.POST['p_comment']
		email = request.POST['email']
		website = request.POST['website']
		name = request.POST['name']
		date = str(timezone.now()).split()[0]
		subscribe = request.POST['subscribe']
		cur = connection.cursor()
		
		if subscribe == 0:
			cur.execute('INSERT INTO home_Comments (Name, body, Post_id_id, Comment_date,Subscribe,website,Email)  VALUES  ('+"'"+ str(name)+"'"+','+ "'"+ str(p_comment)+"'"+','+str(pk)+','+ "'"+str(date)+"'"+', 0,'+"'"+str(website)+"'"+",'"+str(email)+"'"+");")
		else:
			cur.execute('INSERT INTO home_Comments (Name, body, Post_id_id, Comment_date,Subscribe,website,Email)  VALUES  ('+"'"+ str(name)+"'"+','+ "'"+ str(p_comment)+"'"+','+str(pk)+','+ "'"+str(date)+"'"+', 0,'+"'"+str(website)+"'"+",'"+str(email)+"'"+");")
			
		cur.close()
	


	context = {
		'post': post,	
		'page_template': page_template,
		'pk': pk,	
		'all_profiles': all_profiles,
		'all_comments': all_comments,
		'all_scomments': all_scomments,
		'Pcomment_form':Pcomment_form,
		'Scomment_form':Scomment_form,
		'top':top_posts,
	}

#	url = str(request).split('next=')[1]
#	url = url.split("'")[0]
#	url =  urllib.parse.unquote(url) 


	return render(request, template, context)
	
def Post_scomment(request,pk):
	post = Main_post.objects.filter(pk=pk)
	template = 'home/home.html'
	page_template = 'home/Post_view.html'
	all_comments = Comments.objects.all()
	top_posts = Main_post.objects.order_by('Post_date')[:5]
	all_scomments = Reply.objects.all()
	Pcomment_form = PcommentForm(request.POST)
	Scomment_form = ScommentForm(request.POST)
	all_profiles = Profile.objects.all()
	pk = int(pk)

	if request.method == 'POST':
		s_comment = request.POST['s_comment']
		email = request.POST['email']
		website = request.POST['website']
		name = request.POST['name']
		date = str(timezone.now()).split()[0]
		subscribe = request.POST['subscribe']
		cur = connection.cursor()
		
		if subscribe == 0:
			cur.execute('INSERT INTO home_Reply (Name, body, Comment_id_id, Reply_date,Subscribe,website,Email)  VALUES  ('+"'"+ str(name)+"'"+','+ "'"+ str(s_comment)+"'"+','+str(pk)+','+ "'"+str(date)+"'"+', 0,'+"'"+str(website)+"'"+",'"+str(email)+"'"+");")
		else:
			cur.execute('INSERT INTO home_Reply (Name, body, Comment_id_id, Reply_date,Subscribe,website,Email)  VALUES  ('+"'"+ str(name)+"'"+','+ "'"+ str(s_comment)+"'"+','+str(pk)+','+ "'"+str(date)+"'"+', 0,'+"'"+str(website)+"'"+",'"+str(email)+"'"+");")
			
		cur.close()
	


	context = {
		'post': post,	
		'page_template': page_template,
		'pk': pk,	
		'all_profiles': all_profiles,
		'all_comments': all_comments,
		'all_scomments': all_scomments,
		'Pcomment_form':Pcomment_form,
		'Scomment_form':Scomment_form,
		'top':top_posts,
	}

#	url = str(request).split('next=')[1]
#	url = url.split("'")[0]
#	url =  urllib.parse.unquote(url) 


	return render(request, template, context)

