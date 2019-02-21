from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def run_number_of_tests():
    print("Starting test run")
    driver_list = []
    for i in range(1):
        try:
            chrome = webdriver.Remote(
                command_executor='http://zalenium:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME
            )
            print("Got a chrome driver")
            chrome.set_page_load_timeout(30)
            firefox = webdriver.Remote(
                command_executor='http://zalenium:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.FIREFOX
            )
            print("Got a firefox driver")
            firefox.set_page_load_timeout(30)

            driver_list.extend([chrome, firefox])
        except Exception as e:
            print("Failed acquisition of node" + str(e))
            return False
    print("Sessions created")

    driver_list = [chrome, firefox]
    should_abort = False
    for driver in driver_list:
        try:
            driver.get("http://web")
            print("All good...")
        except Exception as e:
            should_abort = True
            print("Exception caught:" + str(e))
        finally:
            driver.quit()
            should_abort = True
    return should_abort

time.sleep(5)
num_fails_in_a_row = 0
while(num_fails_in_a_row < 6):
    if not run_number_of_tests():
        num_fails_in_a_row += 1
        print("Failed. Retry in 5...")
        time.sleep(5)
    else:
        num_fails_in_a_row = 1
        print("Successful loop.")
    print("Loop completed..")