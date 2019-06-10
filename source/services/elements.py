import re


def get_el_classes_list(el):
    class_str = el.get_attribute("class")
    class_str = re.sub('\s{2,}', ' ', class_str.strip())
    return class_str.split(' ')


def el_has_class(el, class_name):
    class_list = get_el_classes_list(el)
    return class_name in class_list
