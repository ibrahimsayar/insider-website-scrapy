import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest


class InsiderWebsiteTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--window-size=1920,1080')
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get('https://useinsider.com/')

    def test_check_page_load(self):
        print(self.driver.title)
        # expected_title = '#1 Leader in Individualized, Cross-Channel CX — Insider'
        # self.assertIn(expected_title, self.driver.title, 'Page not load')

    def test_check_carrier_page_load(self):
        print(self.driver.title)
        # print(self)
        # self.driver.find_element(By.XPATH, '//*[@id="navbarNavDropdown"]/ul[1]/li[6]').click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, '//*[@id="navbarNavDropdown"]/ul[1]/li[6]/div/div[2]/a[2]').click()
        # time.sleep(20)
        # expected_carrer_title = 'Ready to disrupt? | Insider Careers'
        # self.assertIn(expected_carrer_title, self.driver.title, 'Career page not load')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
