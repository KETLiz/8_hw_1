import view
import add_model
import delete_model
import redactor_model
import search_model
import add_model_to_txt
import logger

def buttom_click():
    mode = view.choose_mode()
    if mode == 1:
        add_model.create_json()
        add_model.add_contact()
        name = add_model_to_txt.add_to_txt()
        logger.write(*name)
    elif mode == 2:
        name = view.contact_to_s()
        base = logger.get_base()
        result = search_model.search_contact(base, name)
        view.search(result)
    elif mode == 3:
        delete_model.delete()
    elif mode == 4:
        redactor_model.red()
    