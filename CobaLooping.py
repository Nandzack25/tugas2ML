words = ["apple", "banana", "cherry"]
for word in words:
    print(len(word))

#collection
user = {"jon": 'active', "sansa": 'inactive', "arya": 'active'}
for name, status in user.copy().items():
    if status == 'inactive':
        del user[name]

active_users = {}
for user, status in user.items():
    if status == 'active':
        active_users[user] = status