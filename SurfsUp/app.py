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
    # Query all passengers
    results = session.query(Messenger.date, Messenger.prcp).all()

    session.close()

    # Create a dictionary from the row data and append to a list of precipitation
    precipitation_data = []
    for date, precipitation in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = precipitation
        precipitation_data.append(precipitation_dict)


    return jsonify(all_names)


@app.route("/api/v1.0/stations")
def stations():
    """Return the station data as json"""

    return jsonify(station_data)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return the temperature observation data as json"""

    return jsonify(tobs_data)

@app.route("/api/v1.0/<start>")
def start():
    """Return the <start_data> as json"""

    return jsonify(start_data)

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    """Return the <start_end_data> as json"""

    return jsonify(start_end_data)

if __name__ == "__main__":
    app.run(debug=True)
