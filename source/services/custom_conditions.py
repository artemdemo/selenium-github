import services.utils as utils
import services.elements as elements

# Wait for an element with certain class
# @source https://selenium-python.readthedocs.io/waits.html
#
class element_has_css_class(object):
    def __init__(self, locator, css_class):
        self.locator = locator
        self.css_class = css_class

    def __call__(self, driver):
        el = utils.find_element(driver, self.locator)
        if elements.el_has_class(el, self.css_class):
            return el
        else:
            return False


# Wait for an element without certain class
#
class element_has_no_css_class(object):
    def __init__(self, locator, css_class):
        self.locator = locator
        self.css_class = css_class

    def __call__(self, driver):
        el = utils.find_element(driver, self.locator)
        if not elements.el_has_class(el, self.css_class):
            return el
        else:
            return False
