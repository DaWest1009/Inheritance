

class Person:

    def __init__(self, name, addr, phone):
        self.__name = name
        self.__addr = addr
        self.__phone = phone

    def print_person(self):
        print(
            f"Name: {self.__name}, Address: {self.__addr}, Phone: {self.__phone}")


class Customer(Person):

    def __init__(self, name, addr, phone, cust_num, on_mail_list):
        Person.__init__(self, name, addr, phone)

        self.cust_num = cust_num
        self.on_mail_list = on_mail_list

    def print_person(self):
        print(f"Name: {self.__name} Address: {self.__addr} Phone: {self.__phone}
              Customer Number: {self.__customer_number}, On Mailing List: {self.__on_mailing_list}
