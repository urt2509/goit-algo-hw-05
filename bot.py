from functools import wraps


PATH = "./contacts.txt"


# decorator
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please, enter name and phone"
        except FileNotFoundError:
            return f"File not found"
        except Exception:
            print("Please, enter a command.")

    return inner


def get_contact_info(path: str = PATH) -> dict | None:
    with open(path, "r", encoding="utf-8") as file:
        contacts = {}
        for line in file:
            elements = line.strip().split(":", 1)
            if len(elements) == 2:
                key, value = elements
                contacts[key] = value
            else:
                pass
    return contacts


@input_error
def parse_input(user_input):

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def save_contact(contact):
    path = PATH
    with open(path, "a+", encoding="utf-8") as file:
        name, phone = contact
        file.seek(0)
        file.write(f"{name}: {phone} \n")


@input_error
def update_contact(contact):
    path = PATH
    name, phone = contact
    contacts = get_contact_info(path)
    name = name.strip()
    phone = phone.strip()
    contacts[name] = phone
    with open(path, "w", encoding="utf-8") as file:
        for name in contacts:
            file.write(f"{name}:{contacts[name]}\n")


@input_error
def add_contact(args, path: str = PATH):
    name, phone = args
    contacts = get_contact_info(path)
    if name in contacts:
        return f"Contact {name} is already exists"
    else:
        contact = name, phone
        contacts[name] = phone
        save_contact(contact)
        return "Contact added."


@input_error
def change_contact(args, path: str = PATH):
    name, phone = args
    contacts = get_contact_info(path)
    if name in contacts:
        contact = name, phone
        update_contact(contact)
        return "Contact updated."
    else:
        return f"There is no contact {name}"


@input_error
def show_phone(args, path: str = PATH):
    name, *args = args
    contacts = get_contact_info(path)
    if name in contacts:
        return contacts.get(name)
    else:
        return f"There is no contact {name}"


@input_error
def show_all():
    path = PATH
    contacts = get_contact_info(path)
    if len(contacts):
        return f"{contacts}"
    else:
        return "There are no contacts"


@input_error
def bot_main(path: str = PATH):

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "all":
            print(show_all())
        else:
            print("Invalid command.")


if __name__ == "__main__":
    bot_main()