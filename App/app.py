from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape"
mongo = PyMongo(app)




@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("Mars_.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful!"


if __name__ == "__main__":
    app.run()
