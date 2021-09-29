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
    currsor.execute("""CREATE TABLE IF NOT EXISTS USER_DATA ( 
        Food_Name Varchar(100) NOT NULL,
        Calories_Count Varchar(100) NOT NULL,
        Image_Id Integer NOT NULL,
        Timestamp Varchar(100) NOT NULL,
        Food_Preparing_Time Varchar(100) NOT NULL,
        Energyandcrabs Varchar(100) NOT NULL
    )
       """)
createtableuserdata()
