import os
import pyautogui
from requirements import *

def profile_update():
    # Scroll to "Update resume" button and click it
    resume_path = os.path.abspath("K:\datascience\Job_application_bot\Chandrashekar_Resume.docx")
    update_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Update resume']")))
    update_button.click()
    print("----------------  Update resume' button clicked.       ----------------")
    time.sleep(2)

    # Wait a second for the native dialog to open
    time.sleep(2)

    # Use PyAutoGUI to interact with file picker
    if os.path.exists(resume_path):
        pyautogui.write(resume_path)
        pyautogui.press('enter')
        print(" Resume uploaded via native dialog...................................")
    else:
        print(" Resume file not found on disk.......................................")

    # Confirm upload
    try:
        updated_on = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'updateOn')]"))
        )
        print(f" Upload confirmed. Last updated: {updated_on.text}")
    except:
        print(" Could not verify resume upload timestamp.")


    # DELETING AND UPDATING KEY SKILLS

    try:
        print(" Opening 'Key Skills' edit mode...")

        # Step 1: Click the 'edit' icon beside Key Skills section
        edit_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='lazyKeySkills']//span[contains(@class, 'edit') and contains(@class, 'icon')]")))
        edit_icon.click()
        time.sleep(2)




        print(" Locating the 'Python' chip...")

        # Step 2: Locate the 'Python' skill chip div
        python_chip = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='waves-effect chip' and @data-id='Python_python' and @title='Python']"
            ))
        )

        # Step 3: 
        remove_btn = python_chip.find_element(By.XPATH, ".//a[@class='material-icons close']")
        remove_btn.click()
        print(" 'Python' skill removed successfully.")

        time.sleep(2)

    # except Exception as e:
    #     print(f" Error removing 'Python': {e}")
    #     driver.save_screenshot("remove_python_error.png")
 




 
    # try:
        # 1. Focus the skill input and type "Python"
        skill_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "keySkillSugg"))
        )
        skill_input.clear()
        skill_input.send_keys("Python")
        print(" Typed 'Python' into input.")
        time.sleep(1.5)  # Allow suggestions to load

        # 2. Directly click the suggestion with data-id="7681"
        suggestion = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@class='sugTouple' and @data-id='7681']"))
        )

        # Move mouse to element and click (simulating real behavior)
        actions = ActionChains(driver)
        actions.move_to_element(suggestion).pause(0.5).click().perform()

        print(" Selected suggestion with data-id='7681' (Python)")

        # 3. Optional: Save the skills if required
        try:
            save_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save')]"))
            )
            save_button.click()
            print("Skills saved.")
        except:
            print("Save button not found or not needed.")

    except Exception as e:
        print(f"Failed to add Python skill: {e}")
        # driver.save_screenshot("add_python_error.png")

