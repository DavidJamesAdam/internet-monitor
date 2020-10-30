# Monitor Internet Speeds With Python

- _version: 0.0.2_

Use Python and the speedtest-cli to continuously monitor upload and download speeds & produce a visualization using matplotlib.

![Picture of Output](./Readme/2020-10-30.jpg)

## To-Do

- `os.mkdir` dated for cache + visualization
- Comment & refactor code
- Write up README / How to.
- Add license

## How to Use

1. Open your favorite terminal and run `python monitor.py`.
   You will be asked to enter time delay interval in minutes. (Time format returned is `%H:%M`).
2. You will then be asked how long you wish to run the test for. (Again, in minutes).
3. A graphical representation of your internet performance will be produced and stored in `#`.

## Dependancies

- matplotlib
- speedtest-cli
