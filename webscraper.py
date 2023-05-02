# Tutorial Followed on the website 'https://realpython.com/beautiful-soup-web-scraper-python/'

import requests  # run 'command python -m pip install requests'  in terminal
# run command 'python -m pip install beautifulsoup4' in terminal
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"  # the website you want to scrape
page = requests.get(URL)  # use the import to get all page content


# this grabs all page content the is to be parsed
soup = BeautifulSoup(page.content, "html.parser")


# you can pick which html element you want to scrape using its id
results = soup.find(id="ResultsContainer")
# once you have the id you can pick certain class you want displayed in your scrape
job_elements = results.find_all("div", class_="card-content")

# to filter through multiple points on the website we can use iteration
# in the iterations you can find more classes for certain html elements
# when printing results you can also strip off all of html

# for job_element in job_elements:
# title_element = job_element.find("h2", class_="title")
# company_element = job_element.find("h3", class_="company")
# location_element = job_element.find("p", class_="location")
# print(title_element.text.strip())
# print(company_element.text.strip())
# print(location_element.text.strip())


# what if you only wanted specific jobs for python only
# you can use a another varible and pass an argument for specific h2 elements

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower())  # use 'https://realpython.com/python-lambda/' to learn how to use lamda functions

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
# Afterword you can iterate again to find all jobs with that title.
# with this you can also find links and change the content that appears inside the for loop.
for job_element in python_job_elements:
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
