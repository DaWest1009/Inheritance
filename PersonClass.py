

class Person:

    def __init__(self, name, addr, phone):
        self.__name = name
        self.__addr = addr
        self.__phone = phone

    def print_person(self):
        print(
            f"Name: {self.__name} Address: {self.__addr} Phone: {self.__phone}")


class Customer(Person):

    def __init__(self, name, addr, phone, cust_num, on_mail_list):
        Person.__init__(self, name, addr, phone)

        self.__cust_num = cust_num
        self.__on_mail_list = on_mail_list

    def print_person(self):
        print(f"{Person.print_person(self)} Customer Number: {self.__cust_num} On Mailing List: {self.__on_mail_list}")