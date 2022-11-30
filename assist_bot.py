from adress_book import *

CONTACTS = AddressBook()

def command_parser(command_string: str):
    command_elements = command_string.lower().split(' ')
    command = command_elements[0]
    args = ' '.join(i for i in command_elements[1:])
    return command, args

def split_args(args_string):
    sep_args = args_string.split(' ')
    name = sep_args[0]
    phone = ''.join(sep_args[1:])
    return name, phone

def input_error(func):
    """Handle user's input"""
    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except ValueError:
            return 'Not found'
        except IndexError:
            return 'type name and number'
        except TypeError:
            return 'Enter name and phone'
    return wrap

def do_command(input):
    new_input = input
    args = ''
    for key in COMMANDS:
        if input.startswith(key):
            new_input = key
            break
    args = input[len(new_input):].strip()
        
    result = COMMANDS.get(new_input, lambda : 'enter one of available commands' )
    return result(args) if args else result()

@input_error
def hello_handler():
    """Print hello!"""
    return 'hello!'

@input_error
def add_phone(args):
    """Add new contact"""
    name, phone = split_args(args)
    if name:
        return CONTACTS[name].add_phone(phone)
    else: return f'Enter name'

@input_error
def change_number(args):
    """Change number"""
    old_phone, new_phone = split_args(args)
    for _, record in CONTACTS.items():
        if old_phone in record.get_record_phones():
            return record.change_phone(old_phone, new_phone)
    return 'no such phone number'

@input_error
def remove_phone(args):
    """Remove record from book"""
    phone, _ = split_args(args)
    for record in CONTACTS.values():
        if phone in record.get_record_phones():
            return record.remove_phone(phone)
    


@input_error
def add_new_record(args):
    """add new record"""
    name, phone = split_args(args)
    if name not in CONTACTS.keys():
        record = Record(name, phone)
        return CONTACTS.add_record(record)
    else: return(f'record {name} is already exists')

@input_error
def search_records(name, phone=''):
    if name.isdigit():
        phone = name
    if phone:
        for contact, record in CONTACTS.items():
            if phone in record.get_record_phones():
                return CONTACTS.search_contact(contact, record.phones)
    elif name:
        for contact, record in CONTACTS.items():
            if name == record.name.value:
                return CONTACTS.search_contact(contact, record.phones)
    else: f'Contact not founded'



@input_error
def show_all_handler():
    """shows all contacts"""
    return CONTACTS

@input_error
def good_bye_handler():
    """Print Bye"""
    return "Bye!"

COMMANDS = {'hello': hello_handler,
            'show all': show_all_handler,
            'exit': good_bye_handler,
            'new_record' : add_new_record,
            'new_phone': add_phone,
            'change_phone': change_number,
            'remove' : remove_phone,
            'add' : add_new_record,
            'search' : search_records
            }

def main():
    while True:
        user_input = input('Enter command ')
        result = do_command(user_input)
        print(result)
        if result == 'Bye!':
            break 

if __name__ == '__main__':
    main()