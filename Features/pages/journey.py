__author__ = 'milror00'

from Features.pages import start_page, problem_page
from Features.pages import problem_page


def goto_start_page(context):
    context.browser.get(context.baseurl)
    start_page.verify_on_page(context)


def goto_problem_page(context):
    goto_start_page(context)
    start_page.click_start(context)
    problem_page.verify_on_page(context)
