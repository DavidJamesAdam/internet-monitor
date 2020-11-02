# Monitor Internet Speeds With Python

- _version: 0.0.2_

Use Python and the speedtest-cli to monitor upload and download speeds over a specified period of time & produce a visualization using matplotlib.

![Picture of Output](./Readme/2020-10-30.jpg)

## How to Use

1. Open your favorite terminal and run `python monitor.py`.
   You will be asked to enter time delay interval in minutes.
2. You will then be asked how long you wish to run the test for. (Again, in minutes).
3. A graphical representation of your internet performance will be produced and stored in `./Output`.

## Dependancies

- matplotlib
- speedtest-cli
- requests

## To-Do

- [ ] Write up README / How to.
- [ ] Stop using hard coded inputs.
- [ ] Better documentation.
- [ ] Package it all? Homebrew / PyPi
  - (https://towardsdatascience.com/build-your-first-open-source-python-project-53471c9942a7)
  - check all dependencies are installed (see requirements.txt)?
- [ ] What If speedtest fails, mark timestamp of failed test?
- [ ] Does it need to cache a csv? maybe just make a dict???
