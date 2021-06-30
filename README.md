# analytics-backup-python

CLI to get Google Analytics data using Python.

```bash
usage: main.py [-h] -v VIEWID -s STARTDATE -e ENDDATE [-d DIMENSIONS] [-m METRICS] --endpoint ENDPOINT --accessKey ACCESSKEY --secretKey SECRETKEY [--bucket BUCKET]

generate csv report from google analytics

optional arguments:
  -h, --help            show this help message and exit
  -v VIEWID, --viewId VIEWID
                        view id for analytics property
  -s STARTDATE, --startDate STARTDATE
                        start date for analytics range
  -e ENDDATE, --endDate ENDDATE
                        end date for analytics range
  -d DIMENSIONS, --dimensions DIMENSIONS
                        metrics to export for analytics property separated by comma (i.e. ga:date,ga:clientId)
  -m METRICS, --metrics METRICS
                        metrics to export for analytics property separated by comma (i.e. ga:sessions,ga:users)
  --endpoint ENDPOINT   minio endpoint
  --accessKey ACCESSKEY
                        minio access key
  --secretKey SECRETKEY
                        minio secret key
  --bucket BUCKET       minio bucket to use as storage (will be created if it doesn't exist)
```
