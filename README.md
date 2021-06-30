# analytics-backup-python

CLI to get Google Analytics data using Python.

```bash
usage: main.py [-h] -v VIEWID -s STARTDATE -e ENDDATE [-o OUTPUTFILE] [-d DIMENSIONS] [-m METRICS]

generate csv report from google analytics

optional arguments:
  -h, --help            show this help message and exit
  -v VIEWID, --viewId VIEWID
                        view id for analytics property
  -s STARTDATE, --startDate STARTDATE
                        start date for analytics range
  -e ENDDATE, --endDate ENDDATE
                        end date for analytics range
  -o OUTPUTFILE, --outputFile OUTPUTFILE
                        csv filename to use for output data
  -d DIMENSIONS, --dimensions DIMENSIONS
                        metrics to export for analytics property separated by comma (i.e. ga:date,ga:clientId)
  -m METRICS, --metrics METRICS
                        metrics to export for analytics property separated by comma (i.e. ga:sessions,ga:users)
```
