# Top_Indian_movies
data scrape - https://www.imdb.com/india/top-rated-indian-movies/

demo@ - https://www.youtube.com/watch?v=YjKHvAFV3fU&t=121s

I have fectched data of top 200 Indian movies from the above mentioned website.
Collected data of movies include -- movie title, year of release, rating, director, lead actors/actress, rest of the crew, language

For web scraping I have used python's BeautifulSoup module.
data is stored in Data/imdb_scrape.csv.

requirements - 
" 1. python3.6, 
   2. BeautifulSoup, 
   3. django == 1.11
"
# putting data into db
- put_into_db method has been used for putting the fetched data into sqlite database.
- I have already stored the data into DB. So, don't run that function again as that will create redundancy.
- If you still want to run that function, then first clear the database. 
- admin login - (username - timepay,
                 password - timepay2863)
- Execution of this function would take some time.
- I have also stored data in csv file. File is present inside the Data directory.

# For starting the app
python manage.py runserver

Then in the browser, enter the url - 127.0.0.1:8000
