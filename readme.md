# Python Job Scraper

<img src="https://raw.githubusercontent.com/TonyVallad/Scraping/refs/heads/main/Script_screenshot.png" width="850"/>

This script scrapes job listings from a mock job board at [Real Python's Fake Jobs](https://realpython.github.io/fake-jobs/). It identifies job postings related to "Python" and prints key details such as the job title, company name, location, and a link to apply.

## Prerequisites

- Python 3.x
- The following Python libraries are required:
  - `requests`: To send HTTP requests to the website.
  - `beautifulsoup4`: To parse the HTML content of the website.

You can install the necessary libraries using `pip`:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone or download the repository containing the `scraping.py` script.
2. Ensure that you have all the required libraries installed.
3. Run the script from the command line:

```bash
python scraping.py
```

## Output

The script will print the following details for each job listing that includes the word "Python" in the job title:

- Job Title
- Company Name
- Location
- Link to Apply

For example:

```
Senior Python Developer
Company ABC
New York, NY
Apply here: https://realpython.github.io/fake-jobs/job-1

Junior Python Developer
Company XYZ
San Francisco, CA
Apply here: https://realpython.github.io/fake-jobs/job-2
```

## Notes

This project is for educational purposes only. The job board being scraped is a fake job listings page created by Real Python for web scraping tutorials.

## License

This project is open-source and free to use.