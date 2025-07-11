import os
import time
from datetime import datetime
from requirements import *
from profile_update import profile_update
from job_search import job_search
import pytz
from dotenv import load_dotenv


def login():
    # Get current IST time inside the function
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist)
    current_hour = current_time.hour
    current_minute = current_time.minute
    allowed_times = [(9, 30), (14, 30), (17, 30)]

    # Load credentials
    load_dotenv()
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    try:
        print("Navigating to Naukri login...")
        driver.get("https://www.naukri.com/")
        login_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_btn.click()
        time.sleep(2)

        print("Entering credentials...")
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder,'Email ID')]"))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))).click()
        print(" Logged in successfully.")
        time.sleep(5)

        print(" Navigating to profile page...")
        driver.get("https://www.naukri.com/mnjuser/profile")
        time.sleep(5)
        profile_update()
        print(f" Current IST time: {current_time.strftime('%H:%M')}")
        # Run profile update only at specific times
        if (current_hour, current_minute) in allowed_times:
            profile_update()
        else:
            print(" Not within profile update time window. Skipping...")

        job_search()

    except Exception as e:
        print(f" XXXXXXXXXXXXXXXXXXXXX login Error: {e}")


# Run login
login()
