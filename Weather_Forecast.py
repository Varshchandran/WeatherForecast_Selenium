"""
Author: Varsha Chandran

This Python script uses the Selenium web automation library to scrape the current temperature in Eindhoven from AccuWeather's website.

Requirements:
- Selenium: You can install it using 'pip install selenium'.
- Firefox: You should have Firefox installed on your system.

Usage:
1. Set the 'profile_directory' variable to the location of your Firefox profile directory.
2. Run the script to retrieve the current temperature in Eindhoven.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# Define the Firefox options and profile directory
firefox_options = webdriver.FirefoxOptions()
profile_directory = "C:\\selenium_profile"
firefox_options.add_argument("--profile")
firefox_options.add_argument(profile_directory)

# Initialize the Firefox driver with the specified options
driver = webdriver.Firefox(options=firefox_options)

# Navigate to the AccuWeather website for Eindhoven
driver.get("https://www.accuweather.com/en/nl/eindhoven/249208/hourly-weather-forecast/249208")

try:
    # Find the element containing the current temperature
    temperature_element = driver.find_element(By.CLASS_NAME, 'temp')
    current_temperature = temperature_element.text

    # Print the weather information
    print(f'Current Temperature in Eindhoven is: {current_temperature}')

except Exception as e:
    print(f'Error: {e}')

finally:
    # Close the browser
    driver.quit()
