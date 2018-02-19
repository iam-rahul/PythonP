class Spy:
    def __init__(self,name,age,rating,online):
        self.name = name
        self.age = age
        self.rating = rating
        self.online = True
        self.chats = []
        self.current_status = None

class Spy_friend:
    def __init__(self,name,age,rating,chat):
        self.name = name
        self.age = age
        self.rating = rating
        self.online = True
        self.chat = chat
        self.current_status = None

spy = Spy('Mr Rahul',27,4.0)

friend_one = Spy_friend('Mr Ashish',29,5.2,[])
friend_two = Spy_friend('Mr Deepak',31,4.8,[])
friend_three = Spy_friend('Mr Saini',41,6.2,[])

friends = [friend_one,friend_two,friend_three]
