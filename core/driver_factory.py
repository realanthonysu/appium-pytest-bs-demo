# core/driver_factory.py
import yaml
from appium import webdriver
from config.capabilities import get_android_capabilities

def create_driver(config_file: str):
    """
    根据配置文件在 BrowserStack 上创建 Appium Driver。
    """
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)

    user = config['user']
    key = config['key']
    app_url = config['app_url']
    
    desired_caps = get_android_capabilities()
    desired_caps['app'] = app_url

    # BrowserStack 的连接地址
    remote_url = f'http://{user}:{key}@hub-cloud.browserstack.com/wd/hub'
    
    driver = webdriver.Remote(
        command_executor=remote_url,
        desired_capabilities=desired_caps
    )
    return driver