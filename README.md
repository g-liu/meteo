Weatherman
==========

A nice little Python script that lets you see the weather straight from the command line.

Installation
============

1. Download `weather.py`
2. You will need a [Forecast.IO API Key](http://developer.forecast.io). Place this API Key into the file named `API_KEY`. **Nothing else** should be in that file.
3. Install `geopy` and `requests` libraries:

        pip install geopy
        pip install requests


Usage
=====

Run it: `py weather.py`

When the program runs, input your location. The program is fairly flexible about how you enter the location. For example, you could enter "Seattle" or "Seattle, WA" and both will work just fine.


TODO
====

* Bash script to automatically run this
* More options (command line args)
