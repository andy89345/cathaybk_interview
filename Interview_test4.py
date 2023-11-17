from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from appium.webdriver.common.touch_action import TouchAction

appium_server_url = "http://127.0.0.1:4723/wd/hub"

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '11',
    'deviceName': 'rong',
    'udid': 'e09037f',
    'chromedriverExecutableDir': r"C:\Users\lwx1210731\Desktop\test_programe",
    'appPackage': 'com.android.chrome', 
    'appActivity': 'com.google.android.apps.chrome.Main',
    'automationName':'uiautomator2',
    #'autoWebview': True,
    'noReset': True, 
}

chrome_options = {
    'args': ['--disable-notifications'], 
}

desired_caps['chromeOptions'] = chrome_options

driver = webdriver.Remote(appium_server_url, desired_caps)
#print(f"get_web_view : {driver.contexts}")
webview_context = None


driver.implicitly_wait(10)
########################首頁截圖###########################
url_to_scrape = "https://cathaybk.com.tw/cathaybk/"
driver.get(url_to_scrape)

wait = WebDriverWait(driver, 10)
screenshot_path = "HomePage.png"
driver.implicitly_wait(10)
time.sleep(5)#等javascript全部跑完才截圖
driver.save_screenshot(screenshot_path)
########################首頁截圖###########################

element_hbg = wait.until(EC.presence_of_element_located((By.XPATH, '//android.webkit.WebView[@text="國泰世華銀行"]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]')))

get_web_view=driver.contexts
print(f"get_web_view : {get_web_view}")
time.sleep(5)
wait = WebDriverWait(driver, 10)
element_hbg.click()
wait = WebDriverWait(driver, 30)
time.sleep(5)



# for context in get_web_view:
#     if 'WEBVIEW' in context:
#         webview_context = context
#         driver.switch_to.context(webview_context)
#         break


print('No Webview context found.')
print("click button 產品介紹")
print(driver.contexts)
get_web_vie=driver.contexts


    

element_select_btn1 = wait.until(EC.presence_of_element_located((By.XPATH, '//android.webkit.WebView[@text="國泰世華銀行"]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[1]')))
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
element_select_btn1.click()
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
print("產品介紹 done~~")



print(driver.contexts)
print("click button 信用卡")
element_select_visa_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//android.webkit.WebView[@text="國泰世華銀行"]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]')))
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
element_select_visa_btn.click()
wait = WebDriverWait(driver, 10)
print("信用卡 done~")

print(driver.contexts)

print("查詢信用卡欄位")

xpath = '//android.webkit.WebView[@text="國泰世華銀行"]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View'

elements = driver.find_elements_by_xpath(xpath)


element_count = len(elements)
########################抓取信用卡欄位底下有多少物件##############################
print(f"底下有 {element_count} 個物件")

for element in elements:
    content_desc = element.get_attribute("content-desc")
    resource_id = element.get_attribute("resource-id")
    print(f"content-desc: {content_desc}, resource-id: {resource_id}")
########################抓取信用卡欄位底下有多少物件##############################


#######################信用卡欄位截圖#########################
screenshot_path = "CardPage.png"
driver.save_screenshot(screenshot_path)
#######################信用卡欄位截圖#########################
wait = WebDriverWait(driver, 10)
element_select_CARD_info = wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@content-desc="卡片介紹"]')))
wait = WebDriverWait(driver, 10)
element_select_CARD_info.click()
wait = WebDriverWait(driver, 10)
time.sleep(3)


width = driver.get_window_size()['width']
height = driver.get_window_size()['height']

print(f"width : {width}")
print(f"height : {height}")

touch_action = TouchAction(driver)

start_x = width * 0.5
start_y = height * 0.7
end_x = width * 0.5
end_y = height * 0.3

#driver.swipe(start_x, start_y, end_x, end_y, 600)
touch_action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()
time.sleep(3)
touch_action.tap(x=30, y=100).perform()
time.sleep(2)

driver.quit()