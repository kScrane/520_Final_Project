from handle_users import *
import hashlib

def test_create_users():
    username = "Sophie Crane"
    password = hashlib.sha256("passwordhahah".encode()).hexdigest()
    r = create_user(username, password, 1)
    print_values()
    r = login_user(username, password)
    if (r == 0):
        print("Error finding user")
    else:
        print("Logged in successfully")
    delete_user(username)
    r = login_user(username, password)
    if (r == 0):
        print("Deleted User")
    else:
        print("User not deleted correctly")
    username = "john smith"
    password = hashlib.sha256("asdfrgtreterw".encode()).hexdigest()
    r = create_user(username, password, 0)
    print_values()
    r = login_user(username, password)
    if (r == 0):
        print("Error finding user")
    else:
        print("Logged in successfully")
        delete_user(username)
    r = login_user(username, password)
    if (r == 0):
        print("Deleted User")
    else:
        print("User not deleted correctly")
    print_values()

def test_get_user():
    username = "testing_Get_user"
    delete_user(username)
    r = get_user(username)
    if r != []:
        print("Error in get - user shouldnt exist")
    print(r)
    r = create_user(username, "asdfasd", 0)
    r = get_user(username)
    if r == []:
        print("Error in get - user not found")
    print(r)
    r = delete_user(username)

def create_root():
    create_user("admin", "root", 1)

print_values()
r = get_user('admin')
r = delete_user("asdfa")
print(r)
r = get_user("asdfaweferg")
print(r)
print(r)