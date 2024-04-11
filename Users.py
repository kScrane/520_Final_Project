class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_attempts = 0
    
class admin(user):
    def __init__(self, username, password):
        super().__init__(self,username, password); 
