# Import the dependencies.



#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
from flask import Flask
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
    """Return the precipitation data as json"""

    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    """Return the station data as json"""

    return jsonify(station_data)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return the tobs data as json"""

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
