# Monitor Internet Speeds With Python

1. Use Python and the speedtest-cli to continuslosy monitor internet speeds.

   - Currently set to 60 seconds. Edit the `delay` variable (in seconds) in `monitor.py` to change.)
   - edit time_format to change the time format %H:%M

2. Produce visualization using matplotlib.

## To-Do

- Now we are gathering information and storing it in a csv. You could do all sorts of clever stuff with the filename like name it today’s date using datetime but for now I will keep it as test.

You could also set up a check to see if a certain amount of time has passed and to stop the application after that but I will leave that up to your own creativity.

## Requirements

- matplotlib
- speedtest-cli
