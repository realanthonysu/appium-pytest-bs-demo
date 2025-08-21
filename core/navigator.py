# core/navigator.py
from core.page_factory import PageFactory
from pages.login_page import LoginPage
from pages.home_page import HomePage

class Navigator:
    """
    管理页面间的导航逻辑。
    它使用 PageFactory 来获取页面对象，而不关心它们的创建细节。
    """
    def __init__(self, page_factory: PageFactory):
        self.factory = page_factory

    def navigate_to_login(self) -> LoginPage:
        """导航到登录页"""
        print("Navigating to Login Page...")
        # 从工厂获取 LoginPage 实例
        return self.factory.create_page(LoginPage)

    def login_to_home(self, user, password) -> HomePage:
        """
        执行从登录到主页的完整业务流程。
        """
        print(f"Performing login for user '{user}'...")
        # 1. 从工厂获取登录页
        login_page = self.factory.create_page(LoginPage)
  
        # 2. 在登录页上执行操作
        login_page.login(user, password)

        print("Login successful, navigating to Home Page.")
        # 3. 操作完成后，从工厂获取主页
        return self.factory.create_page(HomePage)

    # --- 新增方法 ---
    def logout_from_home(self) -> LoginPage:
        """
        从主页执行登出操作。
        这是一个改变应用核心状态的关键导航操作。
        """
        print("Executing logout flow...")
        home_page = self.factory.create_page(HomePage)
        home_page.click_logout()
        
        # 关键步骤：在确认应用状态改变后，清空缓存！
        self.factory.clear_cache()
        
        # 登出后，我们期望应用回到登录页，因此返回一个新的登录页实例
        return self.factory.create_page(LoginPage)