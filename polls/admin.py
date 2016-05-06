from django.contrib import admin

from .models import Question, Choicex


# class QuestionAdmin(admin.ModelAdmin):
# 	fields = ['pub_date', 'question_text']

class ChoicexInline(admin.TabularInline):
	model = Choicex
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Datumseinstellungen bla bla yeah', {
			'classes': ('collapse',),
			'fields': ['pub_date']}),
	]

	# packt obiges Inline hier mit rein
	inlines = [ChoicexInline]

	# ändert die Anzeige auf der Auflistungsseite
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	
	# fügt einen Filter hinzu
	list_filter = ['pub_date']

	# fügt ein Suchfeld hinzu
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)