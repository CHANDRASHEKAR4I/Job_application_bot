PROJECT TITLE: AUTOMATED JOB APPLICATION BOT – VERSION 2 NOW SMARTER AND STRONGER

OVERVIEW:
-----------
This Python-based automation tool is designed to streamline the online job application process. It automates login, job search, resume uploads, and application submission for platforms like Naukri.com. Version 2 includes smarter logic, broader keyword support, and improved stability, saving hours of manual effort.

KEY FEATURES:
--------------
1. **Automated Login**
   - Secure login using saved credentials.
   - Fast and reliable access to job portals.

2. **Smart Job Search**
   - Keyword-based dynamic job search (e.g., Power BI, Data Analyst, Business Analyst).
   - Scrapes multiple pages using Selenium and BeautifulSoup.

3. **Auto-Apply Mechanism**
   - Automatically applies to job listings matching user-defined criteria.
   - Filters out duplicates or previously applied jobs.

4. **Resume Auto-Upload**
   - Integrates with OS file pickers using PyAutoGUI.
   - Automatically uploads the latest resume during application.

5. **Credential & State Management**
   - Uses `os` module for securely storing and accessing login credentials and status.

6. **Streamlit UI**
   - Simple and modern user interface to input job titles.
   - One-click button to start the automated bot from the browser.

TECHNOLOGIES USED:
-------------------
- **Python**: Core programming language
- **Selenium**: For browser automation
- **BeautifulSoup**: For web scraping job details
- **PyAutoGUI**: For file selection automation
- **Streamlit**: For interactive UI
- **OS**: For path and credential handling

PROJECT FILES:
---------------
- `main.py`: Master script to control flow
- `login.py`: Manages login logic
- `job_search.py`: Scrapes job listings
- `profile_update.py`: Uploads resume if needed
- `requirements.py`: Stores config data or utilities
- `streamlit_ui.py`: Frontend Streamlit interface

USE CASES:
-----------
- Automate job search and application for freshers and experienced professionals.
- Save time by applying to multiple jobs with one command.
- Customize job titles, resume, and portal interaction with minimal configuration.

HOW TO USE:
------------
1. Clone or download the repository.
2. Add your credentials to a secure `.env` file or input them through UI.
3. Launch `streamlit_ui.py` to open the browser interface.
4. Enter job title(s) and click "Start Bot".
5. Sit back while the bot applies jobs on your behalf.

EXAMPLE JOB TITLES:
---------------------
- Power BI Developer
- Data Analyst
- Business Analyst
- Python Developer
- SQL Analyst

VERSION HISTORY:
-----------------
**Version 1.0**
- Basic login and job scraping logic.
- Manual resume upload.

**Version 2.0** (Current)
- Improved UI using Streamlit.
- Auto resume upload.
- Multi-page scraping and auto-apply logic.
- Smarter error handling and logging.

FUTURE ENHANCEMENTS:
---------------------
- Support for multiple job platforms (LinkedIn, Indeed).
- Logging applied jobs to CSV/DB.
- Email notifications post application.
- Resume customization per job type.

CONTACT:
---------
Developer: Chandra Shekar  
LinkedIn: https://www.linkedin.com/in/chandrashekarippili/

