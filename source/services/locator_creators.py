from selenium.webdriver.common.by import By


def create_data_qa_locator(data_qa_value):
    return By.XPATH, "//*[@data-qa='%s']" % data_qa_value


def create_id_locator(id_value):
    return By.ID, id_value


def create_class_locator(class_value):
    return By.CLASS_NAME, class_value


def create_tag_locator(tag_name):
    return By.TAG_NAME, tag_name
