
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

firefox_options = webdriver.FirefoxOptions()
profile_directory = ("C:\\selenium_profile")
firefox_options.add_argument("--profile")
firefox_options.add_argument(profile_directory)
#location = "Eindhoven, North Brabanth, NL"
driver = webdriver.Firefox(options=firefox_options)

driver.get("https://www.accuweather.com/en/nl/eindhoven/249208/hourly-weather-forecast/249208")

try:

    # Find the element containing the current temperature
    temperature_element = driver.find_element(By.CLASS_NAME, 'temp')
    current_temperature = temperature_element.text

    # Print the weather information
    print(f'Current Temperature in Eindhoven is : {current_temperature}')

except Exception as e:
    print(f'Error: {e}')

finally:
    # Close the browser
    driver.quit()









