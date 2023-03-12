# import json
#
# username = input("what is you name? " )
#
# filename = 'username.json'
# with open(filename,"a") as f_obj:
#     json.dump(username,f_obj)
#     print("we'll remeber you when you com back, " + username + "!")
#
import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("what is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_boj:
        json.dump(username, f_boj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("welcom back " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
