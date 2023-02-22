

class Person:

    def __init__(self, name, addr, phone):
        self.__name = name  # hidden attributes can't be passed down through inheritance
        self.__addr = addr
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_addr(self):
        return self.__addr

    def get_phone(self):
        return self.__phone

    def print_person(self):
        print('Name:', self.__name)
        print('Address:', self.__addr)
        print('Phone:', self.__phone)


class Customer(Person):

    def __init__(self, name, addr, phone, cust_num, on_mail_list):
        Person.__init__(self, name, addr, phone)

        self.__cust_num = cust_num
        self.__on_mail_list = on_mail_list

    def print_person(self):
        # to access superclass attributes just call the method
        Person.print_person(self)

        print("Customer Number:",  self.__cust_num)
        if self.__on_mail_list:  # aka if self.__on_mail_list == True
            print("On Mailing List: Yes")
        else:
            print("Off Mailing List: No")
