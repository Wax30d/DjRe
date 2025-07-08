from django.contrib import admin
from .models import Person, Passport, Reporter, Article, ModelFuel, CarModel

admin.site.register(Person)
admin.site.register(Passport)
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(ModelFuel)
admin.site.register(CarModel)
