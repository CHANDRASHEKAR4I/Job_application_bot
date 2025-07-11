
from bs4 import BeautifulSoup
import csv

from requirements import *



#job_search
def job_search():
    try:
        applied =0
        failed = 0
        applied_list={ 'passed':[],'failed':[] } 


        joblink=[]                           #Initialized list to store links
        maxcount=3                          #Max daily apply quota for Naukri
        keywords=['powerbi developer','BUSINESS ANALYST' ,'DATA ANALYST', "POWERBI"]  #Add you list of role you want to apply
        # location = 'hyderabad'               #Add your location
        time.sleep(3)
        for k in keywords:
            for i in range(3):
                # url = "https://www.naukri.com/"+k.replace(' ','-')+"-jobs-in-"+location+"-"+str(i+1)
                # url = "https://www.naukri.com/"+k.replace(' ','-')+"-jobs-"+str(i+1)+"-EXP"
                # url =   "https://www.naukri.com/"+k.replace(' ','-')+"-jobs" +"&experience="+str(i+1)+"&nignbevent_src=jobsearchDeskGNB"
                url = "https://www.naukri.com/"+k.replace(' ','-')+"-jobs" +"&experience="+str(i+1)+"&nignbevent_src=jobsearchDeskGNB"

                driver.get(url)
                print(url)
                time.sleep(13)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                job_elems = soup.find_all('div', class_='srp-jobtuple-wrapper')
                for job_elem  in job_elems:
                    joblink.append( job_elem.find('a', class_='title').get('href'))
        # print(joblink)



        for i in joblink:
            time.sleep(3)
            driver.get(i)   
            if applied <=maxcount:
                try: 
                    wait = WebDriverWait(driver, 10)
                    apply_button = wait.until(EC.element_to_be_clickable((By.ID, "apply-button")))
                    # Click the button
                    time.sleep(3)
                    apply_button.click()
                    time.sleep(2)
                    
                    applied +=1
                    applied_list['passed'].append(i)
                    print('Applied for ',i, " Count", applied)

                except Exception as e: 
                    failed+=1
                    applied_list['failed'].append(i)
                    print(e, "Failed " ,failed)
            else:
                print("reached your limit")
                driver.close()
                break


        print('Completed applying closing browser saving in applied jobs csv')
        try:driver.close()
        except:pass
        csv_file = "naukriapplied.csv"
        try:
            with open(csv_file, 'w', newline='')  as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['passed', 'failed'])
                writer.writeheader()
                # Get the maximum number of rows needed
                max_len = max(len(applied_list['passed']), len(applied_list['failed']))
                for i in range(max_len):
                    row = {
                        'passed': applied_list['passed'][i] if i < len(applied_list['passed']) else '',
                        'failed': applied_list['failed'][i] if i < len(applied_list['failed']) else ''
                    } 
                    writer.writerow(row)
        except IOError:
            print("I/O error")



    except Exception as job_error:
        print(f" Job search failed: {job_error}")
        driver.save_screenshot("job_search_error.png")








