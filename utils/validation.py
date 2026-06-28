def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid number. Try again.")
        return None


def get_non_empty(prompt):
    value = input(prompt)
    if value.strip() == "":
        print("Input cannot be empty.")
        return None
    return value


def get_contact(prompt):
    contact = input(prompt)

    if len(contact) != 10 or not contact.isdigit():
        print("Invalid contact number. Must be 10 digits.")
        return None

    return contact