
import numbers


class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
    
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def print_person(self):
        print('Method 1')
        print('Name:',self.__name)
        print('Addr:',self.get_address)
        print('Phone:',self.get_phone)

        print()
        print()

print('Customer Number:', self.__customer_num)
class Customer(Person):
    def __init__(self, name, address, phone, customer_num, mail_list):
        Person.__init__(self, name, address, phone)

        self.__customernum = customer_number
        self.__maillist = maillist
