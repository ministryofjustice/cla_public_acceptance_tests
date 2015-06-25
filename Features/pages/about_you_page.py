__author__ = 'milror00'

def verify_on_page(context):
    element = context.browser.find_element_by_xpath(".//*[@id='content']/div[2]/article/h1")
    assert (element.text == "About you")