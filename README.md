# analytics-backup-python

[![License](https://img.shields.io/badge/License-BSD%202--Clause-blue.svg)](LICENSE)  
![GitHub tag](https://img.shields.io/github/v/tag/dictybase-playground/analytics-backup-python)  
[![Maintainability](https://badgen.net/codeclimate/maintainability/dictybase-playground/analytics-backup-python)](https://codeclimate.com/github/dictybase-playground/analytics-backup-python)  
![Last commit](https://badgen.net/github/last-commit/dictybase-playground/analytics-backup-python/develop)  
[![Funding](https://badgen.net/badge/Funding/Rex%20L%20Chisholm,dictyBase,DCR/yellow?list=|)](https://reporter.nih.gov/project-details/10024726)

CLI to get Google Analytics data using Python.

```bash
usage: main.py [-h] -v VIEWIDS -s STARTDATE -e ENDDATE [-d DIMENSIONS] [-m METRICS] --endpoint ENDPOINT --accessKey ACCESSKEY --secretKey SECRETKEY [--bucket BUCKET]

generate csv report from google analytics

optional arguments:
  -h, --help            show this help message and exit
  -v VIEWIDS, --viewIds VIEWIDS
                        list of view ids for analytics property separated by comma (i.e. 123456,888888)
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
