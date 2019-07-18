# 1. import Flask
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars


# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3 Mongo
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.mars_app_db
collection = db.mars_app_db

# 4. Define what to do when a user hits the /index route
@app.route("/")
def index():
    mars = collection.find_one()
    return render_template("index.html", mars=mars)


# 5. Define what to do when a user hits the /scrape route
@app.route("/scrape")
def scrape():
    collection.drop()
    scraped_data = scrape_mars.scrape_all()
    collection.insert_one(scraped_data)
    return redirect('/', code=302)


if __name__ == "__main__":
    app.run(debug=True)
