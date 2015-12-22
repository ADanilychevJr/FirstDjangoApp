from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
	#TabularInline more compact than Stackedinline
	model = Choice
	extra = 3 #provides three extra choice slots when looking at Question in admin mode

class QuestionAdmin(admin.ModelAdmin):
	#fields = ['pub_date', 'question_text'] #Makes pub_date come first
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	#Displays Question_text, pub_date, and column with output from was_published_recently method
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInline]
	list_filter = ['pub_date']#Adds "Filter" sidebar allowing people to filter the change list by the pub_date field. Because pub_date is a DateTimeFiled, Django knows what filter options to provide
	search_fields = ['question_text']#adds a search box at top of change list

admin.site.register(Question, QuestionAdmin)



