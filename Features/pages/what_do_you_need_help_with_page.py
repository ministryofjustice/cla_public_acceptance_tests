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
        'You are losing my accommodation because UKVI is refusing support': 2,
        'Eviction': 3,
        'Unlawful eviction': 1,
        'Eviction with notice': 2,
        'Your home is in disrepair': 4,
        'YES this puts you in risk of injury or illness': 1,
        'NO you are not in risk of injury or illness': 2,
        'Harassment': 5,
        'By a neighbour or landlord': 1,
        'YES you are not immediate risk of harm': 1,
        'NO you are in immediate risk of harm': 2,
        'A partner expartner or family member': 2,
        'By someone else': 3,
        'Discrimination': 6,
        'By age': 1,
        '18 or over': 1,
        'Under 18': 2,
        'At work': 1,
        'While you were using a service': 2,
        'At a private club': 3,
        'When someone was carrying out a public function': 4,
        'At university': 5,
        'Other (debt discrimination problem)': 6,
    }.get(option)

def select_option(context, option):
    get_select_element_by_index(context, get_index_by_option(option)).click()