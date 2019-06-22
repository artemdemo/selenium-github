

def el_has_class(el, class_name):
    class_list = el.get_attribute("class")
    return class_name in class_list
