from selenium.webdriver import Chrome

from core import get_driver
from services import FillTest, get_data


def run(*, driver: Chrome, data: dict, url: str):
    chunk = 25
    for index, (question, answers) in enumerate(data.items()):
        block = index % chunk + 1
        if block == 1:
            input("(Enter to continue) OR (ctrl+c to exit)")
            driver.get(url)

        FillTest(driver, block).start(
            question=question, answers=answers, submit=block < chunk
        )


def main():
    run(
        driver=get_driver("driver/chromedriver"),
        data=get_data('basedata/attestation.json'),
        url="https://konstruktortestov.ru/add",
    )


if __name__ == "__main__":
    main()
