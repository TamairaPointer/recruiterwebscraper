# We need to import some libraries to help us with web scraping
import requests                # This helps us to download the webpage
from bs4 import BeautifulSoup  # This helps us to extract data from the webpage
import time                    # This helps us to add delays so we're not overloading the website
import pandas as pd            # This helps us to organize the scraped data into a table

# This is information about ourselves that we send to the website to be polite
headers = {
    "User-Agent": "Friendly Job Scraper", # Pretend like a friendly web browser
    "From": "your_email_here@example.com" # Let them know how to contact you
}

# This is the web address where the job postings are
url = 'https://example.com/job-postings' # Make sure you replace this with the actual web address

# Go to the web address and get the webpage
response = requests.get(url, headers=headers)

# Look at the webpage and figure out how it's organized
soup = BeautifulSoup(response.text, 'html.parser')

# Let's store our job postings here
job_postings = []

# Find all job postings on the page (this will depend on how the website is built)
for job in soup.find_all('div', {'class': 'job-posting'}): # Look for the section with job postings
    # From each job posting, get the job title, company name, and location
    title = job.find('h2').text # Usually, the job title is big and bold
    company = job.find('span', {'class': 'company'}).text # Maybe the company name is next to it
    location = job.find('span', {'class': 'location'}).text # Location could be next to the company
    
    # Add this job posting to our list
    job_postings.append({'title': title, 'company': company, 'location': location})
    
    # Wait for 5 seconds before getting the next job, so we don't overwhelm the website
    time.sleep(5)

# Now, let's put this data into a table
df = pd.DataFrame(job_postings)

# And save it into a file so we can look at it later
df.to_csv('job_postings.csv', index=False)
