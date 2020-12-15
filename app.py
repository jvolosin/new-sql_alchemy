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
def temperature():
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
def stations():
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


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    
    # Reproduce the precipitation query from the Station Analysis section of part 1. 

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

 #/prcp/<start>` and `/prcp/<start>/<end>`

  #Create a query that returns the minimum precipitation, the average precipitation, and the max precipitation for a given start or start-end range.
    #Hint: You will need to use a function such as `func.min`, `func.max`, `func.avg`, and `func.count` in your queries.

  #When given the start date only, calculate min, max, and avg for all dates greater than and equal to the start date.

  #When given the start and the end date, calculate the min, avg, and max for dates between the start and end date inclusive.
  
  #Return a JSONified dictionary of min, max, and avg temperatures.
	#Note, the result will be a single dictionary of the format: `{"min_temp": min_temp, "max_temp": max_temp, "avg_temp": avg_temp}`

@app.route("/api/v1.0/pcrp/<start")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    start_date = session.query(Station.station, func.count(Measurement.station)).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).all()
    
    start_precip_data = []
    for result in start_date
        start_dict = {}
        start_dict["min_temp"] = min_temp
        start_dict["max_temp"] = max_temp
        start_dict["avg_temp"] = avg_temp
        station_analysis.append(start_dict)
       
    return jsonify(start_precip_data)

    session.close()



@app.route("/api/v1.0/pcrp/<start>/<end")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    start_end_date = session.query(Station.station, func.count(Measurement.station)).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).all()
    
    start_end_precip_data = []
    for result in start_end_date
        start_end_dict = {}
        start_end_dict["min_temp"] = min_temp
        start_end_dict["max_temp"] = max_temp
        start_end_dict["avg_temp"] = avg_temp
        station_analysis.append(start_end_dict)
       
    return jsonify(start_end_precip_data)

    session.close()

if __name__ == '__main__':
    app.run(debug=True)
