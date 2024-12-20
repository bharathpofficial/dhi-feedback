import random
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (update paths as needed)
driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')

def get_form(form_link):
    driver.get(form_link)

def click_all_options():
    # This is gonna select "excellent" as default.
    for i in range(12):
        option_xpath = f'//*[@id="Overall Student Feedback_{i}_0"]'
        try:
            # Wait for the option to be present and scroll it into view
            option_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_xpath)))
            driver.execute_script("arguments[0].scrollIntoView(true);", option_element)

            # Wait for the element to be clickable and then click it
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
            driver.execute_script("arguments[0].click();", option_element)
            # Optional: wait a bit before clicking the next one if needed
            #time.sleep()
        except Exception as e:
            print(f"Error clicking option {i}: {e}")
    print("Completed clicking all options.")

def comment_now():
    # List of possible comments
    comments = ["super", "good", "best"]
    
    # Select a random comment from the list
    selected_comment = random.choice(comments)
    
    # Locate the comment box using XPath
    comment_box_xpath = '//*[@id="feedbackComment"]'
    comment_box = driver.find_element(By.XPATH, comment_box_xpath)
    
    # Clear the comment box if necessary (optional)
    comment_box.clear()
    
    # Send the selected comment to the comment box
    comment_box.send_keys(selected_comment)
    print(f"Comment sent: {selected_comment}")

def submit_now():
    submit_button_xpath = '/html/body/div[2]/app-root/div/app-student/div/section/app-feedback/app-feedback-detail/div[11]/div[2]/button[1]'
    
    try:
        # Wait for the submit button to be visible
        submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, submit_button_xpath)))
        
        # Scroll the submit button into view
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        
        # Optionally, hide or adjust overlapping elements
        driver.execute_script("""
            var footer = document.querySelector('.footer-alignment-css');
            if (footer) {
                footer.style.display = 'none';
            }
        """)
        
        # Wait for the submit button to be clickable
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
        
        # Click the submit button using JavaScript to bypass blocking issues
        driver.execute_script("arguments[0].click();", submit_button)
        
        print("Form submitted.")
    except Exception as e:
        print(f"Error submitting form: {e}")

def main():
    # URL to navigate to for login
    base_url = 'https://regroup.dhi-edu.com/regroup_mite'
    get_form(base_url)
    input("Please log in and navigate to the form. Press Enter when ready...")
    # Replace with the actual URL of the form
    while True:
        # Prompt for the form link
        form_link = input("Enter the form link (or type 'exit' to quit): ").strip()
        if form_link.lower() == 'exit':
            print("Exiting the program.")
            break
            
        get_form(form_link)
        click_all_options()
        comment_now()
        submit_now()

        # Close the WebDriver
    driver.quit()

# Execute the main function
if __name__ == "__main__":
    main()

