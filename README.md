# <img src="src/codevid.ico" width=25px> CODEVID
![Windows](https://github.com/JIceberg/codevid/workflows/Windows/badge.svg)
&nbsp;
![Ubuntu](https://github.com/JIceberg/codevid/workflows/Ubuntu/badge.svg)

A simple web scraper for keeping track of COVID cases in the world.
All data comes from [worldometers](https://www.worldometers.info/coronavirus/).

## Usage

Here are the steps to set up the tracker:
1. Clone the project `git clone https://github.com/JIceberg/codevid.git`

1. Set up your python environment (if needed)

1. Install the requirements for your operating system `pip install -r requirements-<OS>.txt`

1. Run the program and it will send a desktop notification with the current number of cases, and the number of cases yesterday along with the current percent change in number of cases per day compared to 2 days ago to yesterday.

Below is a sample notification

![Notif](.github/images/notif.png)

-----

**DISCLAIMER**

This is my first web scraping project. It is very minimal in scope and not very useful.
The purpose of this project is simply for me to amass more experience with web scraping.