import pytest
from selene import browser

@pytest.fixture(autouse=True)
def browser_config():
    browser.config.base_url = 'https://school.qa.guru'
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.quit()
