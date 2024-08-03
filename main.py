from address_book import AddressBook
from handlers import add_contact, change_phone, show_phone, show_all, add_birthday, show_birthday, birthdays


def parse_input(user_input):
    parts = user_input.split(maxsplit=1)
    command = parts[0].lower()
    args = parts[1].split() if len(parts) > 1 else []
    return command, args


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command in ["add", "add_contact"]:
            print(add_contact(args, book))

        elif command == "change":
            print(change_phone(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command in ["add-birthday", "add_birthday"]:
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
