# Monitor Internet Speeds With Python

1. Use Python and the speedtest-cli to continuously monitor internet speeds.
2. Write to csv
3. Produce visualization using matplotlib.

   - Enter time delay interval in minutes time format returned is `%H:%M`
   - `visualize.py` produces `test-graph.jpg`

## To-Do

- Update `test` filenames to produce daily graphs (name it today’s date using `datetime`).
- Set up a check to see if a certain amount of time has passed and to stop the application after that.
- Put output in a folder
- Write up README / How to.
- `os.mkdir` dated for csv + visulation

## How to Use

Run `python monitor.py` to collect data.
You will be asked to enter an interval... in minutes
You wil then be asked how long to run the test for
Run `python vizualize.py` to generate generate a graphical representation.

![Picture of Output](#)

You could set a chron job to run daily.

`(heres the code for this)`

## Dependancies

- matplotlib
- speedtest-cli
