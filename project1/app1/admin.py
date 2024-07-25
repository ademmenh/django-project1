from django.contrib import admin
from . import models





class ClientAdmin (admin.ModelAdmin):
    #list form
    list_display = ("id", "fname", "lname", "bday", "iday", "salary")
    list_filter = ("salary", )

    #individual form
    fieldsets = (("Personal info", {"fields" : (("fname", "lname"), "bday")}),
                ("Job Info"      , {"fields" : ("iday", "salary")}))



class ClientSalaryAdmin (admin.ModelAdmin):
    #list form
    list_display = ("salary", "rating")
    list_filter = ("rating",)

    #individual form
    # fieldsets = (("Salary", {"fields" : ("salary", )}),
                #  ("Rating", {"fields" : ("rating", )}))
                



class UsersAdmin (admin.ModelAdmin):
    list_display = ("id", "fname")
    # list_filter = ()

    ''' fields = ("Personal Informations", {"fields" : ("fname", )}, ("", {"fields" : ("", "", )}) , )'''




admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.ClientSalary, ClientSalaryAdmin)
admin.site.register(models.Users, UsersAdmin)
