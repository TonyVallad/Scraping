# Python Job Scraper

This script scrapes job listings for Python positions from a sample webpage and prints the job title, company, location, and application link for each listing.

<img src="https://pbs.twimg.com/media/FofpuY3WAAEx78s?format=png&name=small" width="500"/>

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone the repository or download the script.
2. Run the script using Python:

   ```bash
   python job_scraper.py
   ```

3. The script will output the job listings for Python-related positions.

## How It Works

1. **HTTP Request**: The script sends a GET request to the specified URL containing the job listings.
2. **HTML Parsing**: It uses BeautifulSoup to parse the HTML content of the page.
3. **Job Extraction**: The script finds job listings in the HTML structure by searching for specific elements and classes.
4. **Filtering Python Jobs**: It filters the job titles to include only those that contain the word "Python".
5. **Output**: Finally, it prints the title, company name, location, and application link for each Python job.

## Example Output

```
Job Title 1
Company 1
Location 1
Apply here: http://example.com/apply1

Job Title 2
Company 2
Location 2
Apply here: http://example.com/apply2
```

## Contributing

Since this is a just a training project, I do not expect any contributions.