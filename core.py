from selenium import webdriver


def get_driver(path: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir=selenium_cache")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_experimental_option("detach", True)
    # chrome_options.add_argument('headless')
    # chrome_options.add_argument("disable-gpu")

    chrome_service = webdriver.ChromeService(executable_path=path)

    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
    driver.set_page_load_timeout(5)
    driver.implicitly_wait(10)

    return driver
