from django.apps import AppConfig


class HeartuserConfig(AppConfig):
    name = 'heartuser'
def ready(self):
    pass
    #for user in User.objects.all():   Token.objects.get_or_create(user=user)