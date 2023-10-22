import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_linkedin_job(url):
    # Send an HTTP GET request to the LinkedIn job URL
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract job title
        job_title = soup.find('h1', class_='topcard__title').get_text(strip=True)

        job_description = soup.find('div', class_='show-more-less-html__markup').get_text()
        
        # Extract company LinkedIn page URL
        company_url = soup.find('a', class_='topcard__org-name-link')['href']
        
        # Create a DataFrame to store the data
        job_data = pd.DataFrame({
            'URL': [url],
            'Job Title': [job_title],
            'Job Description': [job_description],
            'Company LinkedIn Page': [company_url]
        })

        # Save the data to an Excel file
        job_data.to_excel('linkedin_jobs.xlsx', index=False)
        print("Data saved to 'linkedin_jobs.xlsx'")
    else:
        print("Error: Unable to fetch the LinkedIn job page.")

# Example usage
linkedin_url = "https://www.linkedin.com/jobs/view/3740963276/"
scrape_linkedin_job(linkedin_url)
