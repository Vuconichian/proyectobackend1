from django.contrib import admin
from futbolistas.models import Futbolista, Director, Estadio, User

# Register your models here.

admin.site.register(Futbolista)
admin.site.register(User)
admin.site.register(Director)
admin.site.register(Estadio)
