#!/usr/bin/python

import pymysql
import sys, os

cwd = os.path.realpath(sys.argv[0])
directory = cwd.split("populate_db.py")

f = open(directory[0] + "cities_with_salary.txt", "r")
data = f.read()
data = eval(data)
f.close()

# f = open(directory[0] + "world_cities_parsed.txt", "r")
# world_cit = f.read()
# world_cit = eval(world_cit)
# f.close()

# f = open(directory[0] + "countries_data.txt", "r")
# countries_data = f.read()
# countries_data = eval(countries_data)
# f.close()

# f = open(directory[0] + "currency_exchange.txt", "r")
# currency = f.read()
# currency = eval(currency)
# f.close()

# f = open(directory[0] + "simple_ql_index.txt", "r")
# simple_ql = f.read()
# simple_ql = eval(simple_ql)
# f.close()

# f = open(directory[0] + "cities_data copy.txt", "r")
# cities_data = f.read()
# cities_data = eval(cities_data)
# f.close()

# print(len(cities_data))

#------------------------------------------------------------------------CONNECT-----------------------------------------------------------------------

# Open database connection
db = pymysql.connect("localhost","testuser","test123","tfm" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data1 = cursor.fetchone()
print("Database version : %s " % data1)

#-------------------------------------------------------------------------CREATE-----------------------------------------------------------------------

# CITIES WITH SALARIES LIST

# Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS salaries")

# # Create table as per requirement
# sql = """CREATE TABLE salaries (
#         CITY_NAME  CHAR(50) NOT NULL,
#         SALARY  FLOAT
#          )"""

# cursor.execute(sql)

# WORLD CITIES LIST

# Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS world_cities")

# # Create table as per requirement
# sql = """CREATE TABLE world_cities (
#         CITY_NAME  CHAR(50) NOT NULL,
#         COUNTRY_NAME CHAR(50) NOT NULL
#          )"""

# cursor.execute(sql)

# # COUNTRIES DATA LIST

# # Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS countries_data")

# # Create table as per requirement
# sql = """CREATE TABLE countries_data (
#         COUNTRY  CHAR(50) NOT NULL,
#         SALARY  FLOAT,
#         CPI FLOAT,
#         PURCHASING_POWER FLOAT,
#         POLLUTION FLOAT,
#         SAFETY FLOAT,
#         TRAFFIC FLOAT,
#         HEALTH FLOAT
#          )"""

# cursor.execute(sql)

# CURRENCY LIST

# # Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS currencies")

# # Create table as per requirement
# sql = """CREATE TABLE currencies (
#         CURRENCY  CHAR(5),
#         EUR_TO_CURRENCY FLOAT,
#         USD_TO_CURRENCY FLOAT
#         )"""

# cursor.execute(sql)

# # Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS cities_data")

# # Create table as per requirement
# sql = """CREATE TABLE cities_data (
#         CITY_NAME  CHAR(50) NOT NULL,
#         SALARY  FLOAT,
#         INFRAESTRUCTURE FLOAT,
#         ENVIRONMENT FLOAT,
#         POLLUTION FLOAT,
#         SAFETY FLOAT,
#         QLI FLOAT,
#         HEALTH FLOAT,
#         WOMAN FLOAT,
#         RENT FLOAT,
#         LONGITUDE FLOAT,
#         EMPLOYMENT FLOAT,
#         DIVERSITY FLOAT,
#         LATITUDE FLOAT,
#         TRAFFIC FLOAT,
#         PURCHASING FLOAT,
#         CPI FLOAT
#          )"""

# cursor.execute(sql)


#--------------------------------------------------------------------------INSERT-------------------------------------------------------------------------

# # CURRENCY LIST

# for key in currency['exchange_rates']:
#     print(key)
#     currency = key['currency']
#     eur_to_currency = key['one_eur_to_currency']
#     usd_to_currency = key['one_usd_to_currency']
#     # Prepare SQL query to INSERT a record into the database.
#     sql = "INSERT INTO currencies(CURRENCY, \
#         EUR_TO_CURRENCY, USD_TO_CURRENCY) \
#         VALUES ('%s', '%s', '%s')" % \
#         (currency, eur_to_currency, usd_to_currency)
#     try:
#         # Execute the SQL command
#         cursor.execute(sql)
#         # Commit your changes in the database
#         db.commit()
#     except:
#         print("exception")
#         # Rollback in case there is any error
#         db.rollback()

# # WORLD CITIES LIST

# x = 0

# while x < len(world_cit['cities']):
#     all = str(world_cit['cities'][x])
#     all = all.split(', ')
#     city = all[0]
#     country = all[1]
#     # Prepare SQL query to INSERT a record into the database.
#     sql = "INSERT INTO world_cities(CITY_NAME, \
#         COUNTRY_NAME) \
#         VALUES ('%s', '%s')" % \
#         (city, country)
#     try:
#         # Execute the SQL command
#         cursor.execute(sql)
#         # Commit your changes in the database
#         db.commit()
#     except:
#         print("exception")
#         # Rollback in case there is any error
#         db.rollback()
#     x += 1

# # COUNTRIES DATA LIST

# for _k in countries_data:
#     country = _k
#     try: 
#         salary = countries_data[_k]['salary_avg']
#     except:
#         salary = 0
#     try: 
#         purchasing = countries_data[_k]['purchasing_power_incl_rent']
#     except:
#         purchasing = 0
#     try: 
#         pollution = countries_data[_k]['pollution']
#     except:
#         pollution = 0
#     try: 
#         health = countries_data[_k]['health_care']
#     except:
#         health = 0
#     try: 
#         traffic = countries_data[_k]['traffic_time']
#     except:
#         traffic = 0
#     try: 
#         cpi = countries_data[_k]['cpi_and_rent']
#     except:
#         cpi = 0
#     try: 
#         safety = 100 - float(countries_data[_k]['crime'])
#         print(float(countries_data[_k]['crime']))
#         print(safety)
#     except:
#         safety = 0
    
#     sql = "INSERT INTO countries_data(COUNTRY, \
#         SALARY,CPI,PURCHASING_POWER,POLLUTION,SAFETY,TRAFFIC,HEALTH) \
#         VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
#         (country, salary, cpi, purchasing, pollution, safety, traffic, health)
#     try:
#         # Execute the SQL command
#         cursor.execute(sql)
#         # Commit your changes in the database
#         db.commit()
#     except:
#         print("exception")
#         # Rollback in case there is any error
#         db.rollback()


# CITIES WITH SALARY LIST

for key in data:
    salary = data[key]['salary']
    name = data[key]['data']['name']
    qli = data[key]['data']['simple_quality_life_index']
    longitude = data[key]['data']['longitude']
    latitude = data[key]['data']['latitude']
    
    infraestructure = data[key]['data']['infraestucture_index']
    environment = data[key]['data']['environment_index']
    pollution = data[key]['data']['pollution_index']
    safety = data[key]['data']['crime_index']
    health = data[key]['data']['healthcare_index']
    woman = data[key]['data']['woman_protection_index']
    rent = data[key]['data']['rent_and_purchase_power_index']
    employment = data[key]['data']['employment_index']
    diversity = data[key]['data']['cultural_diversity_index']
    traffic = data[key]['data']['traffic_index']
    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO salaries(CITY_NAME, \
        SALARY, QLI, LONGITUDE, LATITUDE, INFRAESTRUCTURE, ENVIRONMENT, POLLUTION, SAFETY, HEALTH, WOMAN, RENT, EMPLOYMENT, DIVERSITY, TRAFFIC) \
        VALUES ('%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s')" % \
        (name, salary, qli, longitude, latitude, infraestructure, environment, pollution, safety, health, woman, rent, employment, diversity, traffic)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        print("exception")
        # Rollback in case there is any error
        db.rollback()

# # CITIES WITHOUT SALARY LIST

# parsed_data = {}

# for i in cities_data:
#     aux = str(i)
#     aux = aux.split(', ')
#     name = ''
#     if len(aux) > 3:
#         name = aux[0] + ', ' + aux[3]
#     elif len(aux) > 2:
#         name = aux[0] + ', ' + aux[2]
#     else:
#         name = aux[0] + ', ' + aux[1]
#     cities_data[i]['name'] = name
#     parsed_data[name] = {}
#     parsed_data[name] = cities_data[i]

# for key in simple_ql:
#     print(simple_ql[key])
#     print(parsed_data[key])
#     k = str(key)
#     k = k.split(', ')
#     if len(k) > 3:
#         country = k[3]
#     elif len(k) > 2:
#         country = k[2]
#     else:
#         country = k[1]
#     print(countries_data[country])
#     simple_quality_life_index = simple_ql[key]['simple_quality_life_index']
#     try:
#         longitude = simple_ql[key]['longitude']
#     except:
#         longitude = 0
#     try:
#         latitude = simple_ql[key]['latitude']
#     except:
#         latitude = 0
#     try:
#         woman_protection_index = simple_ql[key]['woman_protection_index']
#     except:
#         woman_protection_index = 0
#     name = simple_ql[key]['name']
#     try:
#         rent_and_purchase_power_index = simple_ql[key]['rent_and_purchase_power_index']
#     except:
#         rent_and_purchase_power_index = 0
#     try:
#         employment_index = simple_ql[key]['employment_index']
#     except:
#         employment_index = 0
#     try:
#         cultural_diversity_index = simple_ql[key]['cultural_diversity_index']
#     except:
#         cultural_diversity_index = 0
#     salary = 0
#     try: 
#         purchase = parsed_data[key]['purchasing_power_incl_rent']
#     except:
#         purchase = 0
#     try: 
#         infraestucture_index = simple_ql[key]['infraestucture_index']
#     except:
#         infraestucture_index = 0
#     try: 
#         environment_index = simple_ql[key]['environment_index']
#     except:
#         environment_index = 0
#     try: 
#         pollution = simple_ql[key]['pollution_index']
#     except:
#         pollution = 0
#     try: 
#         health = simple_ql[key]['healthcare_index']
#     except:
#         health = 0
#     try: 
#         traffic = simple_ql[key]['traffic_index']
#     except:
#         traffic = 0
#     try: 
#         cpi = parsed_data[key]['cpi_and_rent']
#     except:
#         cpi = 0
#     try: 
#         safety = float(simple_ql[key]['crime_index'])
#     except:
#         safety = 0
#     sql = "INSERT INTO cities_data(CITY_NAME, \
#         SALARY,INFRAESTRUCTURE,ENVIRONMENT,POLLUTION,SAFETY,QLI,HEALTH,WOMAN,RENT,LONGITUDE,EMPLOYMENT,DIVERSITY,LATITUDE,TRAFFIC,PURCHASING,CPI) \
#         VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')" % \
#         (name, salary, infraestucture_index, environment_index, pollution, safety, simple_quality_life_index, health,woman_protection_index ,rent_and_purchase_power_index,longitude,employment_index,cultural_diversity_index,latitude,traffic,purchase,cpi)
#     try:
#         # Execute the SQL command
#         cursor.execute(sql)
#         # Commit your changes in the database
#         db.commit()
#     except:
#         print("exception")
#         # Rollback in case there is any error
#         db.rollback()


#----------------------------------------------------------------------------READ-------------------------------------------------------------------------
# sql = "SELECT * FROM cities_data \
#         INNER JOIN salaries \
#         WHERE cities_data.CITY_NAME = salaries.CITY_NAME \
#         ORDER BY cities_data.simple_quality_life_index"

#         # WHERE QLI > '%d'" % (84)

# mydict = {}
# info = {}

# try:
#     # Execute the SQL command
#     cursor.execute(sql)
#     # Fetch all the rows in a list of lists.
#     results = cursor.fetchall()

#     # print(results)
#     for row in results:
#         info = {}
#         cname = row[0]
#         sal = row[1]
#         qli = row[2]
#         info['name'] = cname
#         info['salary'] = sal
#         info['qli'] = qli
#         mydict[cname] = {}
#         for _k in info:
#             mydict[cname][_k] = info[_k]
#     #     # Now print fetched result
#     #     print "cname=%s,sal=%d,qli=%d" % \
#     #         (cname, sal, qli )
        
# except:
#     print "Error: unable to fecth data"

# print(mydict)

#-------------------------------------------------------------------------CLOSE------------------------------------------------------------------------

# disconnect from server
db.close()