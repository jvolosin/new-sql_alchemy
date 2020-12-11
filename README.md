# new-sql_alchemy
HW for Rutgers Bootcamp


# SQLAlchemy Homework - Surfs Up!

You must make at least 20 commits for this homework.

Good activities to refer to are:

* Day 2 Activities 2 & 9
* Day 3 Activities 3, 9, & 10


### Precipitation Analysis
You must use SQLAlchemy ORM to query the provided sqlite database for this homework.

* Retrieve the average daily temperature for the first available year in the database.
	* There are more than one temperature readings for each date. Be sure to calculate the average over these observations so you have a single temperature for each date.

* Using pandas or matplotlib, create a well-designed line chart with this information.
 
### Station Analysis

* Query the database for a list station, name, and total number of observations over all available dates. Sort this list by total number of observations in descending order.

* Retrieve the precipitation readings for the most active station (i.e., the one with the greatest number of observations) in the year 2016.

* Using pandas or matplotlib, create a well-designed histogram with this information.

- - -

## Step 2 - Climate App

Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

* Use Flask to create your routes.

### Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/temperature`

  * Reproduce the temperature query used in part 1. Convert the results to a list of dictionaries using `date` as the key and `prcp` as the value.
  * Your route must return the JSON representation of the results in this format.

* `/stations`

  * Reproduce the first station analysis query from part 1 (name, station, and observations). Convert the results to a list of dictionaries, where each returned value has its own dictionary.
		*  Each dictionary in the list should be formatted as followed: `{"Station Name": name, "Station": station, "Observations": obs_count}`
  * Your route must return the JSON representation of the results in this format.

* `/precipitation`
  * Reproduce the precipitation query from the Station Analysis section of part 1.  
  * Return a JSON list of precipitation observations from 2016.

* `/prcp/<start>` and `/prcp/<start>/<end>`

  * Create a query that returns the minimum precipitation, the average precipitation, and the max precipitation for a given start or start-end range.
    * Hint: You will need to use a function such as `func.min`, `func.max`, `func.avg`, and `func.count` in your queries.

  * When given the start date only, calculate min, max, and avg for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the min, avg, and max for dates between the start and end date inclusive.
  
  * Return a JSONified dictionary of min, max, and avg temperatures.
	  * Note, the result will be a single dictionary of the format: `{"min_temp": min_temp, "max_temp": max_temp, "avg_temp": avg_temp}`
