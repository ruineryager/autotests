import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from pages.homepage import HomePage
from pages.product import Product


def test_opens6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click()
    product = Product(browser)
    product.check('Samsung galaxy s6')


def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(5)
    product = Product(browser)
    product.check_count(2)
