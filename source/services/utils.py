from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def find_element(search_scope, locator):
    try:
        element = search_scope.find_element(*locator)
        return element
    except NoSuchElementException:
        return None


def find_elements(search_scope, locator):
    try:
        elements = search_scope.find_elements(*locator)
        return elements
    except NoSuchElementException:
        return None


def wait_and_find_element(search_scope, timeout, locator):
    wait_until_element_is_located(search_scope, timeout, locator)
    return find_element(search_scope, locator)


def wait_and_find_elements(search_scope, timeout, locator):
    wait_until_element_is_located(search_scope, timeout, locator)
    return find_elements(search_scope, locator)


def is_element_located(search_scope, timeout, locator):
    try:
        wait_until_element_is_located(search_scope, timeout, locator)
        return True
    except TimeoutException:
        return False


def wait_for_popup_to_close(driver, timeout, popup_locator):
    WebDriverWait(driver, timeout).until(
        expected_conditions.invisibility_of_element(popup_locator)
    )


def wait_until_element_clickable(driver, timeout, locator):
    WebDriverWait(driver, timeout).until(
        expected_conditions.element_to_be_clickable(locator)
    )


def wait_until_element_is_located(search_scope, timeout, locator):
    WebDriverWait(search_scope, timeout).until(
        expected_conditions.visibility_of_element_located(locator)
    )


def wait_for_element_to_load(search_scope, timeout, locator):
    WebDriverWait(search_scope, timeout).until(
        expected_conditions.visibility_of_element_located(locator)
    )


def create_element_if_needed(element, search_scope, timeout, locator):
    if element is None:
        element = wait_and_find_element(search_scope, timeout, locator)
    return element


def create_elements_if_needed(elements, search_scope, timeout, locator):
    if elements is None:
        elements = wait_and_find_elements(search_scope, timeout, locator)
    return elements


def get_first_element_with_text(search_scope, timeout, locator, text):
    elements = wait_and_find_elements(search_scope,
                                      timeout,
                                      locator)
    return next((element for element in elements if element.text == text), None)


def has_element_with_text(search_scope, timeout, locator, text):
    return get_first_element_with_text(search_scope, timeout, locator, text) is not None
