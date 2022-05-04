# Netflix Scraper

### Prerequisites

1. Selenium
2. Chrome Driver
3. Netflix Credentials [Optional]

### Steps to execute

1. Install Selenium if not installed by using `pip3 install selenium`
2. Download Chrome Driver based on the version of Chrome installed using the following [link](https://chromedriver.chromium.org/downloads). Pick the version according to version that is currently installed i.e. 100, 101 or 102
3. Extract the downloaded zip file in the same directory as the script.

#### To execute Netflix on a specific Title

4. Execute the script by running `python netflix-scraper-no-login.py`

#### To execute Netflix using Credentials

4. **Configure Netflix User Email and Password inside script for variables `login_email` and `login_pass`**
5. Execute the script by running `python netflix-scraper.py`
