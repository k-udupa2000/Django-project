from django.contrib import admin
from .models import Student

#admin.site.register(Users)
@admin.register(Student)
class PostAdmin(admin.ModelAdmin):
    list_display = ('studentName', 'phone1', 'phone2', 'lastFeesPaid', 'lastAttended')
    search_fields = ('studentName',)
    ordering = ('studentName',)

    list_filter = ('lastAttended', 'lastFeesPaid')