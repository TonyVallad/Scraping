import requests  # Import the requests library to make HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML

# URL of the webpage containing job listings
URL = "https://realpython.github.io/fake-jobs/"
# Send a GET request to the specified URL
page = requests.get(URL)

# Parse the content of the page with BeautifulSoup using the HTML parser
soup = BeautifulSoup(page.content, "html.parser")

# Find the container that holds the job results by its ID
results = soup.find(id="ResultsContainer")

# Find all job elements within the results container
job_elements = results.find_all("div", class_="card-content")

# Find all job titles that contain the word "python" (case-insensitive)
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

# Extract the parent elements of the Python job titles to get complete job cards
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# Iterate through each Python job element to extract details
for job_element in python_job_elements:
    # Find and extract the job title
    title_element = job_element.find("h2", class_="title")
    # Find and extract the company name
    company_element = job_element.find("h3", class_="company")
    # Find and extract the job location
    location_element = job_element.find("p", class_="location")

    # Print the job title, company name, and location, stripping any extra whitespace
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())

    # Find all anchor tags in the job element to get the application link
    links = job_element.find_all("a")
    # Get the second link (which typically contains the application URL)
    link_url = job_element.find_all("a")[1]["href"]
    
    # Print the application link
    print(f"Apply here: {link_url}\n")
    print()  # Print an empty line for better readability between job listings
