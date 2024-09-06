### Basic Goal and Requirements for the Web Scraping and Data Entry Capstone Project

#### **Basic Goal**
The goal of this project is to demonstrate your ability to apply web scraping techniques using BeautifulSoup and Selenium to extract data from a website and automate data entry into a Google Form. You will scrape listing details from a Zillow-Clone website, clean and organize the data, and then use Selenium to submit this data to a Google Form, which will be converted into a Google Sheet for final data presentation.

#### **Project Requirements**

1. **Set Up Google Form:**
   - **Create a Form:** Go to [Google Forms](https://docs.google.com/forms/) and create a new form.
   - **Add Questions:** Include 3 questions in the form, all of which should be of the "short-answer" type.
   - **Copy Form Link:** After setting up the form, click "Send" and copy the link address for use in your program.

2. **Scrape Data from Zillow-Clone Website:**
   - **Visit Website:** Navigate to [Zillow-Clone](https://appbrewery.github.io/Zillow-Clone/) to understand the website structure.
   - **Use BeautifulSoup/Requests:** Implement a BeautifulSoup and Requests-based script to:
     - **Extract Listing Links:** Gather all listing URLs.
     - **Extract Prices:** Capture the price information from each listing and clean the data to remove extraneous characters, leaving just the dollar amount in the format "$1,234".
     - **Extract Addresses:** Obtain and clean the addresses, ensuring no newlines, pipe symbols (`|`), or unnecessary whitespace.

3. **Automate Data Entry with Selenium:**
   - **Fill Google Form:** Use Selenium to programmatically fill in the Google Form for each listing. Input the listing’s price, address, and link into the appropriate fields.
   - **Submit Form:** Ensure that a new form entry is created for each listing.
   - **Create Google Sheet:** After all data entries are complete, click on the "Sheet" icon in the Google Form responses to generate a Google Sheet with all the data.

#### **Summary of Deliverables**
- **Google Form Setup:** A functional Google Form with three short-answer questions.
- **Scraped Data:** Cleaned and organized lists of links, prices, and addresses from the Zillow-Clone website.
- **Automated Form Submission:** A Selenium script that successfully submits all scraped data to the Google Form.
- **Google Sheet:** A Google Sheet populated with the scraped data from the Zillow-Clone website.

This project will test your ability to integrate various skills, including web scraping, data cleaning, and automation, to achieve a complete workflow from data extraction to presentation.