import time
import unittest

from selenium import webdriver


class UserInterfaceTestCase(unittest.TestCase):
    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.client = webdriver.Chrome(options=options)
        # self.client = webdriver.Chrome()
        if not self.client:
            self.skipTest('Web browser not available.')

    def tearDown(self) -> None:
        if self.client:
            self.client.quit()

    def test_index(self):
        self.client.get('http://127.0.0.1:5000')
        time.sleep(2)
        self.assertIn('你好', self.client.page_source)

    def test_submit(self):
        self.client.get('http://127.0.0.1:5000')
        username_item = self.client.find_element_by_id('username')
        username_item.send_keys('测试用户')
        body_item = self.client.find_element_by_id('body')
        body_item.send_keys('测试内容')
        submit_item = self.client.find_element_by_id('submit')
        submit_item.click()
        time.sleep(1)
        self.assertIn('发布成功', self.client.page_source)


if __name__ == '__main__':
    unittest.main()
