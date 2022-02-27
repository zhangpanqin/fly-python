from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def visit_baidu():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com/')
    # 获取百度搜索框元素
    element = driver.find_element(value="kw", by='id')
    # 在搜索框中输入关键词python，并模拟键盘的enter操作
    element.send_keys("python", Keys.ENTER)
    driver.close()


def visit_python():
    browser = webdriver.Chrome()
    browser.get('http://mflyyou.cn/')
    # print(browser.page_source)
    print(browser.find_element(by=By.XPATH, value='/html/body/div[5]').text)
    browser.close()


if __name__ == '__main__':
    visit_python()
