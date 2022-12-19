from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class SeleniumHooks:
    def __get_chrome_capabilities(self, url, headless):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')

        if headless:
            chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
        driver.get(url.strip())
        driver.maximize_window()
        return driver

    def start_web_driver(self, capabilities):
        """Starts the browser with the desired capabilities.

        :param capabilities: headless
        :return: driver
        """
        try:
            return self.__get_chrome_capabilities(capabilities['url'], capabilities['headless'])
        except Exception as e:
            print(e)
            print("[ERROR] Start web driver process has failed")
            exit()

    def kill_web_driver(self, driver):
        """Kill browser session.

        :param driver: driver
        """
        driver.quit()
