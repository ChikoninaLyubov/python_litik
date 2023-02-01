import view
import model

def start():
    choice = ''
    while choice != 8:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
            case 2:
                model.save_file()
            case 3:
                view.show_contacts(model.get_phone_book())
            case 4:
                new_contact = list(view.create_new_contact())
                model.add_new_contact(new_contact)
            case 5:
                contact = view.del_contact()
                result, index = model.search_contact(contact)
                view.show_contacts_index(result, index)
                index = view.index_view()
                model.delete_contact(index)
                view.exit_in_menu
            case 6:
                find = view.find_contact()
                result = model.search_contact(find)
                view.show_contacts(result)
            case 7:
                   exit(0)
            case _:
                view.input_error()
