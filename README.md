# Monitor Internet Speeds With Python

1. Use Python and the speedtest-cli to continuously monitor internet speeds.
2. Write to csv
3. Produce visualization using matplotlib.

   - Enter time delay interval in minutes time format returned is `%H:%M`
   - `visualize.py` produces `test-graph.jpg`

## To-Do

- **Test `delay` and add user input**
- Update `test` filenames to produce daily graphs (name it today’s date using `datetime`).
- Set up a check to see if a certain amount of time has passed and to stop the application after that.
- Write up README / How to.

## How to Use

Run `python monitor.py` to collect data. You will be asked to enter an interval...
Run `python vizualize.py` to generate generate a graphical representation.

## Dependancies

- matplotlib
- speedtest-cli
