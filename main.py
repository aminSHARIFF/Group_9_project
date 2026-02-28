class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id          # unique ID
        self.username = username        # login name
        self.password = password        # stored password
        self.role = role                # "admin" or "student"!!