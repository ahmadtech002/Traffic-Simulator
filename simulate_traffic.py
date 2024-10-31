import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Load configuration from JSON file
def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

# Set up WebDriver
def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Simulate visits to the website
def simulate_visits(driver, url, num_visits, visit_duration):
    for visit in range(num_visits):
        driver.get(url)  # Open the target website
        print(f"Visit {visit + 1} to {url}")
        time.sleep(visit_duration)  # Wait on the page

        # Optional: Interact with the page (e.g., scroll)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(2)  # Pause between visits to mimic natural behavior

# Main function to run the simulation
def main():
    config = load_config()  # Load settings
    url = config["TARGET_URL"]
    num_visits = config["NUMBER_OF_VISITS"]
    visit_duration = config["VISIT_DURATION"]

    driver = setup_driver()
    try:
        simulate_visits(driver, url, num_visits, visit_duration)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
