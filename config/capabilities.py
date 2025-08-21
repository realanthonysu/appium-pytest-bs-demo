# config/capabilities.py
def get_android_capabilities():
    """定义 Android 测试设备的能力"""
    return {
        "platformName": "android",
        "platformVersion": "12.0",
        "deviceName": "Google Pixel 6",
        "automationName": "UiAutomator2"
    }

def get_ios_capabilities():
    """定义 iOS 测试设备的能力"""
    return {
        "platformName": "ios",
        "platformVersion": "15",
        "deviceName": "iPhone 13",
        "automationName": "XCUITest"
    }