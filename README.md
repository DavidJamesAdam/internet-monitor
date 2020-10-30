# Monitor Internet Speeds With Python

1. Use Python and the speedtest-cli to continuously monitor upload and download speeds.
2. Write to csv
3. Produce visualization using matplotlib.

   - Enter time delay interval in minutes time format returned is `%H:%M`
   - `visualize.py` produces `test-graph.jpg`

## To-Do

- `os.mkdir` dated for csv + visulation (cache)
- Comment code
- Write up README / How to.
- Create crontab scheduler "a crontab`scheduler (called`#`) is also provided.
- Add license

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
