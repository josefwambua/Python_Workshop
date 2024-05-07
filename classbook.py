class ContactBook:
    def __init__(self,name):
        self.name = name
        self.contacts = []
    
    def add_contact(self, first_name, last_name, email):
        self.contacts.append(
            {
                "First name": first_name,
                "Last name": last_name,
                "Email": email
            }
        )
    #def __getitem__ (self, item):
    #   return self.contacts[item]

    #def __iter__(self):
    #    return iter(self.contacts)
# best way 
    def __iter__(self):
        return ContactBookIterator(self.contacts)

class ContactBookIterator:
    def __init__(self, contacts):
        print("The __init__ method for contactbookiterator is clled")
        self.contacts = contacts
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        print("The next method for contactbookiterator is called")
        if self.index >= len(self.contacts):
            print("Iteration stopped")
            raise StopIteration
        contact = self.contacts[self.index]
        self.index += 1
        return contact

my_friends = ContactBook("My friends")
my_friends.add_contact("josef","Wambua","josefwambua@gmail.com")
my_friends.add_contact("felix","Wambutu","jaa@gmail.com")
my_friends.add_contact("John","Wajo","jaowagmail.com")
print(my_friends)

# using  for loop
#for friend in my_friends:
#    print(friend)

# using star
#print(*my_friends, sep=", ")

# using sorted
print(sorted(my_friends))