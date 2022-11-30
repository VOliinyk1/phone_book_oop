from collections import UserDict

class AddressBook(UserDict):
    def search_contact(self, name, phone):
            return f"{name} : {phone}"
                
                

    def add_record(self, record):
        self.data[record.name.value] = record
        return f"Record {record.name.value} {record.get_record_phones()} is added"
        
class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    def __repr__(self):
        return str(self.value)
        

class Phone(Field):
    def __repr__(self):
        return str(self.value)

class Record:
    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = [Phone(phone)] if Phone else []

    def get_record_phones(self):
        return [i.value for i in self.phones]
    
    def __repr__(self) -> str:
        return str(self.get_record_phones())

    def add_phone(self, phone=''):
        if phone:
            self.phones.append(Phone(phone))
            return f'{self.name} phone {self.get_record_phones()} is added'
        return "Enter phone nuber for adding"
    
    def change_phone(self,old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return f"{self.name.value}'s number is changed to {new_phone}"
        return 'No such number'

    def remove_phone(self, phone):
        for number in self.phones:
            if number.value == phone:
                self.phones.remove(number)
                return f"{phone} is removed from {self.name.value}"
            return 'No such phone number'
