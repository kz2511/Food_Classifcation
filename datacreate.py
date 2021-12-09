import pymysql


def createdatabase():
    connection = pymysql.connect(host="localhost", user="root", password="")
    currsor = connection.cursor()
    currsor.execute("CREATE DATABASE FOOD_PREDICTION")
    print("Creating...")
#createdatabase()

def createtableuserdata():
    connection = pymysql.connect(host="localhost", user="root", password="",database="FOOD_PREDICTION")
    currsor = connection.cursor()
    currsor.execute("CREATE TABLE IF NOT EXISTS predictions (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,prediction VARCHAR(50),veg_or_non_veg VARCHAR(20),calorie_count VARCHAR(10),youtube_predictions TEXT,image_path TEXT)")
createtableuserdata()


# ID AUTO INCREMENT INT
# Prediction VARCHAR
# VegOrNonVeg VARCHAR
# Youtube Predictions TEXT
# Image Link TEXT
