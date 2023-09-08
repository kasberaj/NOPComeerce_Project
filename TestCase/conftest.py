import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    # driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
    return driver


@pytest.fixture(params=[('kasbeee@gmail.com', 'Kasbe@1997'),
                        ('kasbeeegmail.com', 'Kasbe@1997'),
                        ('kasbeee@gmail.com', 'Kasb@1997'),
                        ('kasbeee@mail.com', 'Kasbe@197')])
def get_data_for_login(request):
    return request.param
