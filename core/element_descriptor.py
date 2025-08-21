# core/element_descriptor.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger


class ElementDescriptor:
    """
    一个用于懒加载和缓存 Appium 元素的描述符。
    """
    def __init__(self, by: AppiumBy, value: str, timeout: int = 10):
        self.by = by
        self.value = value
        self.timeout = timeout
        self._element_cache = None

    def __get__(self, instance, owner):
        if instance is None:
            return self

        # 第一次访问时查找元素
        if self._element_cache is None:
            locator_str = f"({self.by}, '{self.value}')"
            # 记录底层的元素查找，这对于调试定位符问题至关重要
            logger.debug(f"Searching for element with locator: {locator_str}")
            try:
                driver = instance.driver
                wait = WebDriverWait(driver, self.timeout)
                element = wait.until(
                    EC.presence_of_element_located((self.by, self.value))
                )
                self._element_cache = element
                logger.debug("Element found and cached within descriptor.")
            except NoSuchElementException as e:
                logger.error(f"Failed to find element with locator: {locator_str}")
                raise NoSuchElementException(
                    f"Element not found with locator: ('{self.by}', '{self.value}')"
                ) from e
        return self._element_cache
