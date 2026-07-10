from flask import Flask, render_template

# Creating the web application instance
app = Flask(__name__)

# Telling the web application this is the home page and what to do when someone visits it 
@app.route("/")
def home():
  about = {
    "bio": "I'm a data science and machine learning student building end-to-end projects — from scraping raw data to deploying models people can actually use.",
    "focus": [
      "Regression & classification modeling",
      "Model deployment (Flask, Streamlit)",
      "Data pipelines & feature engineering"
    ]
  }
  return render_template("index.html", about=about)

# Running the web application
if __name__ == "__main__":
  app.run(debug = True) # Run the web application in debug mode