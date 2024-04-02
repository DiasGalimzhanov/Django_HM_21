from django.contrib.auth.models import User
def users(request):
    users = User.objects.all()
    return {
        'users': users
    }

def group_users(request):
    user = request.user
    user_groups = {}

    if user.is_authenticated:
        groups = user.groups.all()
        user_groups = {group.name: group for group in groups}

    return {
        'user': user,
        'user_groups': user_groups,
    }