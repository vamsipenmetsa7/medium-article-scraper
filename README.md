# [Medium Header Scraper: Automate Table of Contents Creation for Your Articles in Seconds](https://vamsipenmetsa.medium.com/medium-header-scraper-automate-table-of-contents-creation-for-your-articles-in-seconds-f6bb66b25d56)
## Medium article header scraper App

This project is a Flask application that allows users to scrape headers from Medium articles. Users can input a Medium article URL, and the application will return the titles and links of the headers in a well-indented format.

<img width="995" alt="image" src="https://github.com/user-attachments/assets/6eca5ac5-b98a-4ec3-ac10-483cd31154ef" />


## Project Structure

```
medium-header-scraper-app
├── app
│   ├── static
│   │   └── styles.css        # CSS styles for the application
│   ├── templates
│   │   └── index.html        # HTML template for the main page
│   ├── __init__.py           # Initializes the Flask application
│   ├── routes.py             # Defines the routes for the application
│   └── scraper.py            # Contains the scraping logic
├── venv                       # Virtual environment for the project
├── requirements.txt           # Lists required Python libraries
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd medium-flask-app
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install the required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```bash
   flask run
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter the Medium article URL in the provided input field and submit the form.

4. The application will display the headers and links extracted from the article.

## Dependencies

This project requires the following Python libraries:

- Flask
- requests
- beautifulsoup4
- tabulate

Make sure to install these dependencies using the `requirements.txt` file.
