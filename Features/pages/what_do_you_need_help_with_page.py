import time

__author__ = 'milror00'

def verify_on_page(context):
    element = context.browser.find_element_by_xpath(".//*[@id='content']/div[2]/article/h1")
    assert (element.text == "What do you need help with?")

def get_select_element_by_index(context, index):
    return context.browser.find_element_by_xpath(
        ".//*[@id='content']/div[2]/article/div/ul/li[{0}]/a".format(str(index)))

def get_index_by_option(option):
    return {
        'You own my own home': 1,
        'You are living in rented accommodation': 2,
        'You are homeless': 3,
        'You owe money': 4,
        'YES you are in risk of losing your home': 1,
        'NO you are not in risk of losing your home': 2,
        'You are becoming homeless': 1,
        'Eviction': 1,
        'Unlawful eviction': 1,
        'Eviction with notice': 2,
    }.get(option)

def select_option(context, option):
    get_select_element_by_index(context, get_index_by_option(option)).click()