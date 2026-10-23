
def get_user_role(user):
    return user["role"]


def can_access_admin(user):
    if get_user_role(user) == "admin":
        return True
    return False
