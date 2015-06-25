from Features.pages import problem_page, maybe_able_to_get_advice_from_a_legal_advisor_page, journey
from Features.pages import maybe_able_to_get_advice_from_a_legal_advisor_page
from Features.pages import legal_aid_not_normally_available_for_personal_injury_page
from Features.pages import legal_aid_is_not_usually_available_for_this_problem
from Features.pages import what_do_you_need_help_with_page
from Features.pages import about_you_page

__author__ = 'milror00'

from behave import given, when, then


@given(u'I am on the public problem page')
def step_impl(context):
    journey.goto_problem_page(context)


@then(u'I am redirected to the what do you need help with page')
def step_impl(context):
    what_do_you_need_help_with_page.verify_on_page(context)


@when(u'I select {scope}')
def step_impl(context, scope):
    problem_page.select_scope(context, scope)


@when(u'I click option {option}')
def step_impl(context, option):
    what_do_you_need_help_with_page.select_option(context, option)


@then(u'I verify I am on the legal aid is not usually available for personal injury page')
def step_impl(context):
    legal_aid_not_normally_available_for_personal_injury_page.verify_on_page(context)


@then(u'I verify I am on the legal aid is not usually available for this problem page')
def step_impl(context):
    legal_aid_is_not_usually_available_for_this_problem.verify_on_page(context)


@then(u'I verify I am on the eligible for advise from a legal advisor page')
def step_impl(context):
    maybe_able_to_get_advice_from_a_legal_advisor_page.verify_on_page(context)


@then(u'I verify I am on the about me page')
def step_impl(context):
    about_you_page.verify_on_page(context)
