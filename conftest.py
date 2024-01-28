import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://phptravels.com/demo"


@pytest.fixture(scope="function")
def page(page):
    def create_page():
        page.goto(BASE_URL)
        return page

    yield create_page()
