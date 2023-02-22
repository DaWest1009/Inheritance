import PersonClass as pc


def main():
    person = pc.Person('John', '1234 North Central Street', '289-337-4281')
    # customer = pc.Customer('Nathan', '2345 Southlake Avenue',
    # '314-986-1114', '892582443', True)

    show_person_info(person)
    # show_person_info(customer)


def show_person_info(person):
    if isinstance(person, pc.Person):
        person.print_person()
    else:

        print(f"{person} is not from the person class")


main()
