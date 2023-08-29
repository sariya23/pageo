from selenium.webdriver.common.by import By

from pageo.locators.abstract_locator import AbstractLocator


class NameLocator(AbstractLocator):
    """
    Класс представляет собой объект локатора,
    который создается на основе значения атрибута name тега элемента
    """
    by = By.NAME