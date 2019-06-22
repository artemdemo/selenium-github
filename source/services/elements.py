import services.utils as utils
from services.locator_creators import create_xpath_locator


def el_has_class(el, class_name):
    class_list = el.get_attribute("class")
    return class_name in class_list


def get_parent_of_el(el):
    return utils.find_element(el, create_xpath_locator("./.."))
