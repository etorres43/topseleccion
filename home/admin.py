from django.contrib import admin
from home.models import Main_post, Tag_list, Profile, Comments, Reply

# Register your models here.
class Post_items(admin.ModelAdmin):
	fieldsets = [
	(None,               {'fields': ['Title','Main_img','Post_content','Profile_id','Tag','Post_short']}),
	('Date information', {'fields': ['Post_date'], 'classes': ['collapse']}),
	]

	list_display = ('Title', 'Post_date', 'Post_score')
	list_filter = ['Post_date']

admin.site.register(Main_post,Post_items)
admin.site.register(Profile)
admin.site.register(Tag_list)
admin.site.register(Comments)
admin.site.register(Reply)
