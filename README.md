# Monitor Internet Speeds With Python

1. Use Python and the speedtest-cli to continuously monitor internet speeds.
2. Write to csv
3. Produce visualization using matplotlib.

   - Delay between readings is currently set to 60 seconds. Edit the `delay` variable (in seconds) in `monitor.py` to change.
   - Edit `time_format` to change the time format (currently `%H:%M`)
   - `visualize.py` produces `test-graph.jpg`

## To-Do

- Now we are gathering information and storing it in a csv. You could do all sorts of clever stuff with the filename like name it today’s date using datetime but for now I will keep it as test.

You could also set up a check to see if a certain amount of time has passed and to stop the application after that but I will leave that up to your own creativity.

## Requirements

- matplotlib
- speedtest-cli
