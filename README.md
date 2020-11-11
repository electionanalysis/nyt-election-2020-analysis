# NYT 2020 election timeseries data plotter

This repo scrapes a timeseries of NYT election data for all federal races, granular at the state level. It's important
to note that the timeseries is maintained by the NYT.

The output also includes a snapshot of county-level results, correct at the time the data was scraped. 

A script is included which plots the NYT 2020 election data from any state, with time on the X axis and ratio of D/R votes on the Y axis. Based on https://threadreaderapp.com/thread/1325592112428163072.html

## County-level timeseries
A separate repo is [](available here) which scraped the NYT API on a regular basis, albeit only for the presidential race.
This allows reconstruction of the POTUS NYT vote-count data at the county-level.

## Down-ballot timeseries
There is no known source of county-level down-ballot timeseries, but it is possible to partially reconstruct 
using the state-level house race timeseries. This is because each congressional district corresponds to a limited number
of counties (in larger cities one CD obtains data from a subset of a single county).

## Congressional District <-> County mapping
Daily Kos helpfully [tabulated the mapping](https://www.dailykos.com/stories/2019/7/30/1848730/-How-do-counties-House-districts-and-legislative-districts-all-overlap-These-new-tools-show-you), 
as of 2019, and it is [available as a google doc](https://docs.google.com/spreadsheets/d/18adZpIghSQQTZLrUNzEdn78ng7mnk2l4-h6IYPsv34I/edit?ts=5ca11736#gid=1533064169).

A copy of this mapping data is stored as a CSV in the metadata folder of this repo.

## All races data
Added a quick script that returns the timeseries data for all races tracked by the NYT.



## Quickstart

Prerequisites: Python 3

```
pip3 install pandas requests matplotlib
python3 nyt_ts.py
python3 plot.py michigan
python3 plot.py new-hampshire
```
