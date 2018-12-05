import pyodbc
connection_string = redacted

conn = pyodbc.connect(connection_string,autocommit=True) # autocommit = True, since it is the SQL Server way
curs = conn.cursor()
curs.execute(
    '''
create table WillsTable (
	RID int identity(1,1) primary key clustered -- Added Column
	,GuaranteeNumber varchar(500)
	,TransactionReportID bigint
	,AmountUSD money
	,CurrencyName varchar(100)
	,EndDate datetime2
	,BusinessSector varchar(100)
	,CityTown varchar(100)
	,StateProvinceRegionName varchar(100)
	,StateProvinceRegionCode varchar(100)
	,CountryName varchar(100)
	,RegionName varchar(100)
	,Latitude varchar(100)
	,Longitude varchar(100)
	,IsWomanOwned varchar(100)
	,IsFirstTimeBorrower varchar(100)
	,BusinessSize varchar(100)
     )

    '''
    )

import csv
insert_query = 'insert into WillsTable (GuaranteeNumber, TransactionReportID, AmountUSD, CurrencyName, EndDate, BusinessSector, CityTown, StateProvinceRegionName, StateProvinceRegionCode, CountryName, RegionName, Latitude, Longitude, IsWomanOwned, IsFirstTimeBorrower, BusinessSize) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
with open(r'C:\Desktop\Final Project\Final Project Data.csv', 'r',encoding='utf8') as loan_data:
    loans = csv.reader(loan_data)
    curs.executemany(insert_query, loans)

#    3) Describe the schema you will use in your database. If it is a relational database (e.g.SQL Server), share your table schema, if it is a document store (e.g.MongoDB) then share a sample JSON file that represents the data you intend to store.(10 pts)
#Here is the table that McKelly created for me.

create table WillsDatabase.dbo.WillsTable (
	RID int identity(1,1) primary key clustered -- Added Column
	,GuaranteeNumber varchar(500)
	,TransactionReportID bigint
	,AmountUSD money
	,CurrencyName varchar(100)
	,EndDate datetime2
	,BusinessSector varchar(100)
	,CityTown varchar(100)
	,StateProvinceRegionName varchar(100)
	,StateProvinceRegionCode varchar(100)
	,CountryName varchar(100)
	,RegionName varchar(100)
	,Latitude varchar(100)
	,Longitude varchar(100)
	,IsWomanOwned varchar(100)
	,IsFirstTimeBorrower varchar(100)
	,BusinessSize varchar(100)
     )


import json
import rethinkdb as r
from flask import Flask, request

app = Flask(__name__)

#Route
@app.route('/', methods=['GET'])
def hello():
    return 'Will Bagley MIS 5400 Project'

#get item
@app.route('/data', methods=['GET'])
def contact():
        return '<b>My data source for this project comes from ' \
               'a United States Government website. ' \
               'The Government provides loans around the world ' \
               'through the USAID program.  This is a program ' \
               'to exercise the Governments soft influence around the world. ' \
               'This data source shows the loan amount, the currency, ' \
               'the location, and many additional metrics of the loans. ' \
               'I have detailed the amount and location of these loans in ' \
               'the following pages. </b>'