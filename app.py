import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.station
Measurement = Base.classes.measurement

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/temperature<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/pcrp/<start><br/>"
        f"/api/v1.0/pcrp/<start>/<end><br/>"
    )


@app.route("/api/v1.0/temperature")
def station():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Reproduce the temperature query used in part 1. 
    # Convert the results to a list of dictionaries using `date` as the key and `prcp` as the value.
    
    first_yr_avg_temp = session.query(func.avg(Measurement.tobs), Measurement.date),\
        filter(func.strftime("%Y", Measurement.date) == "2010").\
        group_by(Measurement.date).all()

    session.close()

    avg_temp = []
    for result in first_yr_avg_temp:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["tobs"] = tobs
        avg_temp.append(temp_dict)
       
    return jsonify(avg_temp)


@app.route("/api/v1.0/stations")
def passengers():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    
    # Reproduce the first station analysis query from part 1 (name, station, and observations). Convert the results to a list of dictionaries, where each returned value has its own dictionary.
    #Each dictionary in the list should be formatted as followed: `{"Station Name": name, "Station": station, "Observations": obs_count}`
    #Note - I was unable to get names, I kept getting an error saying it wasn't in measurement even though I was querying stations. I understand this will lower my grade

    query_list = session.query(Station.station, func.count(Measurement.station)).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).all()
    
    station_analysis = []
    for result in query_list
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Observations"] = obs_count
        station_analysis.append(station_dict)
       
    return jsonify(station_analysis)

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_passengers = []
    for name, age, sex in results:
        passenger_dict = {}
        passenger_dict["name"] = name
        passenger_dict["age"] = age
        passenger_dict["sex"] = sex
        all_passengers.append(passenger_dict)

    return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)
