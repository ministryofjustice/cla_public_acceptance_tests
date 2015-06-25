__author__ = 'milror00'


def verify_on_page(context):
    element = context.browser.find_element_by_xpath(".//*[@id='content']/div[2]/article/h1")
    assert (element.text == "Check if Civil Legal Advice can help you")


def click_start(context):
    element = context.browser.find_element_by_xpath(".//*[@id='start']")
    element.click()
