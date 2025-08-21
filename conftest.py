
import pytest
from core.driver_factory import create_driver
from core.page_factory import PageFactory
from core.navigator import Navigator
from dsl.user_actions import UserActions
from loguru import logger
from utils.logger import setup_logger

@pytest.fixture(scope="session")
def driver(request):
    """
    创建并返回 Appium Driver 的 fixture。
    测试会话结束后自动退出。
    """
    config_path = "config/browserstack.yml"
    app_driver = create_driver(config_path)
    
    yield app_driver
    
    print("\nQuitting driver...")
    app_driver.quit()

@pytest.fixture(scope="function")
def page_factory(driver):
    """
    创建 PageFactory 实例的 fixture。
    它依赖于 driver fixture。
    """
    return PageFactory(driver)

@pytest.fixture(scope="function")
def navigator(page_factory):
    """
    创建 Navigator 实例的 fixture。
    它现在依赖于 page_factory fixture。
    """
    return Navigator(page_factory)

@pytest.fixture(scope="function")
def user(navigator):
    """
    创建 DSL 实例的 fixture。
    这个 fixture 保持不变，因为它依赖的 navigator 接口没有变化。
    """
    return UserActions(navigator)

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    """
    一个自动执行的、会话级别的 fixture，用于在测试开始前配置日志。
    """
    setup_logger()
    logger.info("="*20 + " TEST SESSION STARTED " + "="*20)
    yield
    logger.info("="*20 + " TEST SESSION FINISHED " + "="*20)