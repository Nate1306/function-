def get_guest_name():
    return input("Enter a guest: ")

def is_list_shorter_than(guest_list, max_guests):
    return len(guest_list) < max_guests

def is_already_invited(name, guest_list):
    return name in guest_list


guest_list = []
for count in range(3):
    guest_list.append(get_guest_name())

print(guest_list)

while is_list_shorter_than(guest_list, 12):
    new_guest = get_guest_name()
    if not is_already_invited(new_guest, guest_list):
        if (len(guest_list) + 1) % 2 == 0:
            guest_list.insert(0, new_guest)
        else:
            guest_list.append(new_guest)
    else:
        print(new_guest, "is already invited")

print(guest_lIst)

