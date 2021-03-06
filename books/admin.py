from django.contrib import admin

from .models import Publisher, Author, Book, UserProfile, likes


class AuthorAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name','email')
    search_fields = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'publisher', 'publicatin_date','descrp',)
    list_filter = ('publicatin_date',)
    date_hierarchy = 'publicatin_date'
    ordering = ('-publicatin_date',)
    fields = ('title','authors','publisher','publicatin_date',)
    filter_horizontal = ('authors',)

#raw_id_fields = ('publisher',)# we use raw_id_fields , because if we have so many objects in our publisher model our add book may take a while becuse it takes time to load all our publishers and to void this we use an option that is called " raw_id_fields#



admin.site.register(Publisher)
admin.site.register(likes)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(UserProfile)


