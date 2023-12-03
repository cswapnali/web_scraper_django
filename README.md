# web_scraper_django
### Project Description:
This project is a web application that utilizes Django, a Python web framework, to create a platform for scraping and displaying news headlines and summaries based on user input. The application integrates Selenium for web scraping, Django for backend development, and Bootstrap for frontend styling. Users can input a person's name, triggering the application to scrape relevant news details from the past five days using the CNBC website.

### Key Features:
1. **Scraping Functionality:** The application allows users to input a person's name and initiates a web scraping process using Selenium to fetch news headlines and summaries.
2. **Django Integration:** Django is employed to handle user input, manage scraping operations, and render the scraped data to the user interface.
3. **Date Filtering:** The scraped news details are filtered based on their publication date, ensuring only information from the last five days is displayed.
4. **Presentation of Results:** The application presents the scraped headlines, summaries, and publication dates in a structured manner on the results page.

### Technologies Used:
- **Django:** Python web framework for building the backend of the application.
- **Selenium:** Web scraping tool used to extract information from the CNBC website.
- **Bootstrap:** CSS framework for frontend styling and responsive design.

### Installation:
1. Clone the project repository: 'git clone https://github.com/cswapnali/web_scraper_django.git'
2. Install project dependencies using pip: 'pip install -r requirements.txt'
3. Set up the database configuration in 'settings.py'. As the project uses scraping and does not persist data, the default SQLite configuration is sufficient.
4. Apply database migrations: 'python manage.py migrate'
5. Start the development server: 'python manage.py runserver'
6. Access the application in your browser at `http://localhost:8000`.

### How to Use:
1. Input a person's name on the application's home page.
2. Press "Search" to initiate the web scraping process.
3. The application will display relevant news headlines, summaries, and publication dates from the last five days.
4. Results are presented on the results page.

Note: Ensure that the required web drivers for Selenium are correctly configured.

### Screenshots:
Please refer to the following Google Drive link to access a demo video of the application:
https://drive.google.com/file/d/1ljqT9j3GAoSMIgwnprky1QtHL13jSHG7/view?usp=drive_link

### Contact Information:
- LinkedIn: https://www.linkedin.com/in/swapnali-choudhari/
- Portfolio: https://swapnalic14.pythonanywhere.com/
