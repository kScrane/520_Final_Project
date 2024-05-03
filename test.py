from handle_users import *
import hashlib
import unittest

class TestUserDatabase(unittest.TestCase):
    def test_create_user(self):
        delete_user("Sophie")
        self.assertEquals(create_user("Sophie", "password", "org"), 1)
        self.assertEquals(create_user("Sophie", "password", "org"), 0)
        delete_user("Sophie")
    def test_delete_user(self):
        delete_user("test")
        self.assertEquals(delete_user("test"), 0)
        create_user("test", "password", "org")
        self.assertEquals( delete_user("test"), 1)
    def test_get_user(self):
        delete_user("test")
        self.assertEquals(get_user("test"), 0)
        create_user("test", "password")
        print(get_user("test"))
        self.assertNotEqual(get_user("test"), 0)
        delete_user("test")
    def test_login_user(self):
        delete_user("Sophie")
        create_user("Sophie", "password")
        self.assertNotEquals(login_user("Sophie", "password"), 0)
        self.assertEquals(login_user("Sophie", "notpassword"), 0)
        delete_user("Sophie")
        
def create_root():
    create_user("admin", "root", "org_name", 1)

if __name__ == '__main__':
    print_values()
    #unittest.main()