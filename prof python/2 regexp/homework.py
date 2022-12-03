from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern_number = re.compile(r"(\+7|8)\s*\(*(\w{,3})\)*(\-|\s)*(\w{,3})(\-|\s)*(\w{,2})(\-|\s)*(\w+)*")
pattern_extension_number = re.compile(r"\(*доб\.\s(\w+)\)*")

for contact in contacts_list[1:]:
    contact[-2] = pattern_number.sub(r"+7(\2)\4-\6-\8", contact[-2])
    contact[-2] = pattern_extension_number.sub(r"доб.\1", contact[-2])
    aux_list = contact[0].split() + contact[1].split()
    if len(aux_list) == 2:
        contact[0] = aux_list[0]
        contact[1] = aux_list[1]
    if len(aux_list) == 3:
        contact[0] = aux_list[0]
        contact[1] = aux_list[1]
        contact[2] = aux_list[2]

new_contacts_list = [contacts_list[0]]

for contact in contacts_list:
    c = 0
    for i in range(0, len(new_contacts_list)):
        if contact[0] == new_contacts_list[i][0] and contact[1] == new_contacts_list[i][1]:
            c += 1
            for k in range(2, 7):
                if new_contacts_list[i][k] == '':
                    new_contacts_list[i][k] = contact[k]
    if c == 0:
        new_contacts_list.append(contact)

pprint(new_contacts_list)

with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
    print('phonebook.csv was created/rewrote')
