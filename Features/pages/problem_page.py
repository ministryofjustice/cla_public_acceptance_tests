__author__ = 'milror00'


def get_verifier(context):
    return context.browser.find_element_by_xpath(".//*[@id='content']/div[2]/article/h1")


def verify_on_page(context):
    assert (get_verifier(context).text == "What do you need help with?")


def get_select_element_by_index(context, index):
    return context.browser.find_element_by_xpath(
        ".//*[@id='content']/div[2]/article/div[1]/ul/li[{0}]/a".format(str(index)))

def get_index_by_scope(scope):
    return {
        'clinical negligence': 1,
        'community care': 2,
        'debt': 3,
        'domestic violence': 4,
        'discrimination': 5,
        'education': 6,
        'employment': 7,
        'family': 8,
        'housing': 9,
        'immigration and asylum': 10,
        'mental health': 11,
        'personal injury': 12,
        'public law': 13,
        'trouble with the police': 14,
        'welfare benefits': 15,
    }.get(scope)    # 9 is default if x not found


def select_scope(context, scope):
    get_select_element_by_index(context, get_index_by_scope(scope)).click()


