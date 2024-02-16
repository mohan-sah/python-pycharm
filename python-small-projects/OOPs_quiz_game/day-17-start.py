class User:

    def __init__(self, user_id, username):
        print("new user is being created...")
        self.id = user_id
        self.username = username
        self.follower = 0 #setted to defalut therefore no need to pass.
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1

    # pass


# PascalCase
# camelCase
# snake_case


user_1 = User("001", "mohan")
print(user_1.id)

user_2 = User("002", "sah")
print(user_2.follower)

user_1.follow(user_2)
print(f"user_1.follower {user_1.follower}")
print(f"user_1.following {user_1.following}")
print(user_2.follower)
print(user_2.following)
