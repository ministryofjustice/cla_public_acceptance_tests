__author__ = 'milror00'

from selenium import webdriver


def before_feature(context, feature):
    if 'staging' in feature.tags:
        context.baseurl = 'https://cla-public.service.dsd.io/'
    elif 'demo' in feature.tags:
        context.baseurl = 'http://public-demo.cla.dsd.io/'
    elif 'training' in feature.tags:
        context.baseurl = 'http://public-training.cla.dsd.io/'
    else:
        context.baseurl = "http://public-demo.cla.dsd.io/"


# noinspection PyUnusedLocal
def before_scenario(context, scenario):
    browser = getattr(context, "browser", None)
    if not browser:
        context.browser = webdriver.Firefox()


# noinspection PyUnusedLocal
def after_scenario(context, scenario):
    context.browser.quit()
