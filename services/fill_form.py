import re
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class FillTest:
    def __init__(self, driver: Chrome, index: int) -> None:
        self.base = f'//*[@id="test"]/div/div[{index}]'
        self.driver = driver
        self.index = index

    def fill_question(self, question: str):
        xpath_title = f'{self.base}/input'
        question = re.sub(r'^\d+\.\s', '', question)
        self.driver.find_element(By.XPATH, xpath_title).send_keys(question)

    def click_checkbox(self, xpath_checkbox: str):
        self.driver.find_element(By.XPATH, xpath_checkbox).click()

    def add_answer(self, xpath_answer: str, answer: str):
        answer = re.sub(r'^\.?\d+\)\s', '', answer)
        self.driver.find_element(By.XPATH, xpath_answer).send_keys(answer)

    def add_row(self, xpath_row: str):
        self.driver.find_element(By.XPATH, xpath_row).click()

    def fill_answer(self, answers: list[str]):
        for row, answer in enumerate(answers, 1):
            base = f'{self.base}/div[2]/table/tbody'
            if row > 3:
                self.add_row(f'{base}/tr[{row - 1}]/td[4]/a[2]/span/i')
            if answer.startswith('.'):
                self.click_checkbox(f'{base}/tr[{row}]/td[1]/div/ins')
            self.add_answer(f'{base}/tr[{row}]/td[2]/input', answer)

    def click_submit(self):
        xpath = '//*[@id="test_form"]/fieldset/div[4]/a'
        self.driver.find_element(By.XPATH, xpath).click()

    def start(self, question: str, answers: list[str], submit=True):
        self.fill_question(question)
        self.fill_answer(answers)
        if submit:
            self.click_submit()
        time.sleep(.5)
