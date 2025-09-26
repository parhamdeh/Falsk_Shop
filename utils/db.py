from pymongo import MongoClient
import config
# ODM = برای MongoDB (سندی)

class MongoManager:
    def __init__(self):
        self.client = MongoClient(config.MONGO_URI)
        self.db = self.client[config.DB_NAME]

        self.users = self.db.users

    def Add_User(self, username, email, password):
        user = self.users.find_one({"name":username})
        user_email = self.users.find_one({"email":email})
        if user:
            return 2
        elif user_email:
            return 3
        else:
            user = {
                "name":username,
                "email" : email,
                "password":password
            }
            self.users.insert_one(user)
            return 1
    
    def check_login(self, username, password):
        user = self.users.find_one({"name":username})
        if user:
            if user["password"] == password:
                return 1
            return "passwordError"
        else: 
            return "usernameError"
        

mongo = MongoManager()