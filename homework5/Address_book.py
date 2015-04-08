class Address_Book(object):

    def __init__(self, owner, contacts):
        ''' owner is a string and contacts is a list
            of contact objects
        '''
        self.owner = owner
        self.contacts = contacts


class Contact(object):

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return self.name + ' ' + str(self.phone)
