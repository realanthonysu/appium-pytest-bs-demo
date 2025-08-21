# core/page_factory.py
from typing import Type, TypeVar
from appium.webdriver.webdriver import WebDriver
from core.base_page import BasePage
from loguru import logger # 导入 logger

# 使用 TypeVar 来获得更好的类型提示
T = TypeVar('T', bound=BasePage)

class PageFactory:
    """
    一个专门用于创建和管理 Page Object 实例的工厂。
    它实现了 Page Factory 模式的核心职责：
    1. 接收 Driver 实例。
    2. 根据请求的类创建 Page Object。
    3. 缓存已创建的实例以供复用。
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self._page_cache = {}
        logger.debug(f"PageFactory initialized with cache ID: {id(self._page_cache)}")
        # print(f"PageFactory initialized with cache ID: {id(self._page_cache)}")

    def create_page(self, page_class: Type[T]) -> T:
        """
        获取一个页面对象的实例。
        如果实例已存在于缓存中，则直接返回；否则，创建一个新实例并缓存。
        """
        # 使用 page_class 的名字作为缓存的 key
        page_name = page_class.__name__
        if page_name not in self._page_cache:
            # 当页面不在缓存中时，使用 driver 来实例化它
            # 当创建一个新的页面对象实例时，记录一条 DEBUG 日志
            logger.debug(f"Creating a new instance of [Page: {page_name}].")
            # print(f"Creating a new instance of {page_name}...")
            self._page_cache[page_name] = page_class(self.driver)

        print(f"Returning instance of {page_name}.")
        return self._page_cache[page_name]

    # --- 新增方法 ---
    def clear_cache(self):
        """
        清空所有已缓存的页面对象。
        当应用状态发生重大变化时（如登出），应调用此方法。
        """
        # 清空缓存是一个重要事件，使用 INFO 级别
        logger.info("Clearing all page object caches.")
        # print(f"Clearing page cache. Current cache size: {len(self._page_cache)}")
        self._page_cache.clear()
        # print("Page cache cleared.")

    def invalidate_page(self, page_class: Type[T]):
        """
        从缓存中移除指定的页面对象。
        """
        page_name = page_class.__name__
        if page_name in self._page_cache:
            # print(f"Invalidating single page '{page_name}' from cache.")
            # 失效单个页面也是一个值得关注的事件
            logger.info(f"Invalidating [Page: {page_name}] from cache.")
            del self._page_cache[page_name]