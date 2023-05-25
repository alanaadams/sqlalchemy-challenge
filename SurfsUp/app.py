# Import the dependencies.
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"This is the Hawaii Precipitation API homepage. <br/>"
        f"Available routes: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start> <br/>"
        f"/api/v1.0/<start>/<end> <br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a  dictionary of all precipitation data"""
    # Starting from the most recent data point in the database. 
    most_recent_date = dt.date(2017, 8, 23)

    # Calculate the date one year from the last date in data set.
    query_date = most_recent_date - dt.timedelta(days=365)


    # Perform a query to retrieve the date and precipitation scores in the last year
    results = session.query(Messenger.date, Messenger.prcp).\
        filter(Measurement.date >= query_date).\
        filter(Measurement.date <= most_recent_date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of precipitation
    precipitation_data = []
    for date, precipitation in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = precipitation
        precipitation_data.append(precipitation_dict)

    return jsonify(precipitation_data)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return the station data as json"""
    # Perform a query to retrieve the stations in the data
    stations = session.query(Station.station).all()
    
    session.close()

    # Create a dictionary from the station data
    station_data = []
    for station in stations:
        station_dict = {}
        station_dict["station"] = station
        station_data.append(station_dict)

    return jsonify(station_data)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return the temperature observation data as json"""
    # Using the most active station id
    # Query the last 12 months of temperature observation data for this station
    most_active_station = "USC00519281"
    active_tobs_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= query_date).\
        filter(Measurement.date <= most_recent_date).\
        filter(Measurement.station == most_active_station).all()
    
    session.close()

    # Create a dictionary from the row data and append to a list of temperature data
    temperature_data = []
    for date, temperature in results:
        temperature_dict = {}
        temperature_dict["date"] = date
        temperature_dict["tobs"] = temperature
        temperature_data.append(temperature_dict)
    return jsonify(temperature_data)

@app.route("/api/v1.0/<start>")
def start():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return the <start_date> as json"""

    session.close()

    return jsonify(start_data)

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    """Return the <start_end_data> as json"""

    return jsonify(start_end_data)

if __name__ == "__main__":
    app.run(debug=True)
