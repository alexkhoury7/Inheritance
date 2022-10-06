import exercise as p

def main():
    name = 'John'
    address = '1234 Main St'
    phone = '123-456-789'
    customer_num = 1234
    mail_list = False

    person1 = p.Person(name, address, phone)

    customer1 = p.Customer(name, address, phone, customer_num, mail_list)
    person1.print_person()

    print()
    print()
    print()

    customer1.print.person()



main()
    