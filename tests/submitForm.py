from playwright.sync_api import expect
from ..common import utils


def test_page_title(page):
    assert page.title() == "Book Your Free Demo Now - Phptravels"


def test_preenchimento_form(page):
    page.fill("input[name='first_name']", "My First Name")
    page.fill("input[name='last_name']", "My Last Name")
    page.fill("input[name='business_name']", "Python Coder's")
    page.fill("input[placeholder='Email']", "test@test-qa-python.com")

    utils.soma_valores(page)

    page.click("button[id='demo']")

    expect(page.locator(".completed h2")).to_have_text("Thank you!")


def test_firstName_obrigatorio(page):
    utils.dialog_validate(page, 'Please type your first name')

    page.fill("input[name='last_name']", "My Last Name")
    page.fill("input[name='business_name']", "Python Coder's")
    page.fill("input[placeholder='Email']", "test@test-qa-python.com")

    utils.soma_valores(page)

    page.click("button[id='demo']")


def test_lastName_obrigatorio(page):
    utils.dialog_validate(page, 'Please type your last name')

    page.fill("input[name='first_name']", "My First Name")
    page.fill("input[name='business_name']", "Python Coder's")
    page.fill("input[placeholder='Email']", "test@test-qa-python.com")

    utils.soma_valores(page)

    page.click("button[id='demo']")


def test_businessName_obrigatorio(page):
    utils.dialog_validate(page, 'Please type your business name')

    page.fill("input[name='first_name']", "My First Name")
    page.fill("input[name='last_name']", "My Last Name")
    page.fill("input[placeholder='Email']", "test@test-qa-python.com")

    utils.soma_valores(page)

    page.click("button[id='demo']")


def test_email_obrigatorio(page):
    utils.dialog_validate(page, 'Please type your email name')

    page.fill("input[name='first_name']", "My First Name")
    page.fill("input[name='last_name']", "My Last Name")
    page.fill("input[name='business_name']", "Python Coder's")

    utils.soma_valores(page)

    page.click("button[id='demo']")


def test_soma_obrigatorio(page):
    utils.dialog_validate(page, 'Please input result number')

    page.fill("input[name='first_name']", "My First Name")
    page.fill("input[name='last_name']", "My Last Name")
    page.fill("input[name='business_name']", "Python Coder's")
    page.fill("input[placeholder='Email']", "test@test-qa-python.com")

    page.click("button[id='demo']")
