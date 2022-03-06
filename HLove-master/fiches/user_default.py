from django.contrib.auth.models import User


def genirate_default_user_name():
    pk = User.objects.all().last().id
    return 'User_'+str(pk)