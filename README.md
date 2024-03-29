# Mission To Mars

<img src = "https://user-images.githubusercontent.com/46534353/61434415-bee4f380-a8ea-11e9-9800-dae345d7a627.PNG">

## Website
Beautifully arranged website using Bootstrap and containers. There is button on the top that will Scrape the data for you.
Below is an initial look at the website.
#### Want to see what happens after the data is Scraped...Scroll below....

#### BEFORE
<img src="https://user-images.githubusercontent.com/46534353/61419649-fe441d80-a8b3-11e9-982a-01b0379937ba.png">

#### AFTER
<img src="https://user-images.githubusercontent.com/46534353/61419659-09974900-a8b4-11e9-8f6b-71891c5c304e.png">


### Step 1: Scraping

Scraped the following websites:
1. <a href="https://mars.nasa.gov/news/">NASA Mars News Site</a>
2. <a href="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars">JPL Featured Space Image</a>
3. <a href="https://twitter.com/marswxreport?lang=en">Mars Weather twitter account</a> 
4. <a href="https://space-facts.com/mars/">Mars Facts webpage</a>
5. <a href="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars">USGS Astrogeology site</a>

### Step 2: MongoDB and Flask Application

MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.Use Used Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.
Used Pymongo for CRUD applications for the database. The existing document is overwritten each time the /scrape url is visited and new data is obtained. Used Bootstrap to structure the HTML template.

#### MongoDB setup
<img src="https://user-images.githubusercontent.com/46534353/61419620-e2407c00-a8b3-11e9-9f2e-11da58499f0e.png">
