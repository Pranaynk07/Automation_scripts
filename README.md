# This is a repository for automation of python scripts

**Automated Daily News Scraper** 

This project automates the collection of daily headlines from Google News using Selenium and saves them in a structured .csv file.
The program is built in Python and compiled into a standalone .exe file using PyInstaller, allowing it to run on Windows without requiring a separate Python environment.

**How It Works?**

Launches a headless (invisible) Chrome browser using Selenium.
Scrapes the latest news headlines, publishers, and article links from Google News.
Stores the data in a CSV file.
Can be scheduled to run automatically every day at 09:00 AM using Windows Task Scheduler.

**Technologies:** 

- Python  
- Selenium  
- Pandas  
- PyInstaller

*Note:*<br>
The chromedriver version must be same as that of the chrome browser.<br>
The chromedriver.exe must be in the same folder as that of the standalone .exe file that we coverted from the python file using PyInstaller.