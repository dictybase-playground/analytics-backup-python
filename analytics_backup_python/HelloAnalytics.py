from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'key.json'
VIEW_ID = ''


def initialize_analyticsreporting():
    """Initializes an Analytics Reporting API V4 service object.

    Returns:
      An authorized Analytics Reporting API V4 service object.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        KEY_FILE_LOCATION, SCOPES)

    # Build the service object.
    analytics = build('analyticsreporting', 'v4', credentials=credentials)

    return analytics


def get_report(analytics):
    """Queries the Analytics Reporting API V4.

    Args:
      analytics: An authorized Analytics Reporting API V4 service object.
    Returns:
      The Analytics Reporting API V4 response.
    """
    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': VIEW_ID,
                    'dateRanges': [{'startDate': 'today', 'endDate': 'today'}],
                    # https://ga-dev-tools.appspot.com/dimensions-metrics-explorer/
                    # 'metrics': [{'expression': 'ga:sessions'}, {'expression': 'ga:users'}, {'expression': 'ga:pageviews'}, {'expression': 'ga:exits'}],
                    # 'dimensions': [{'name': 'ga:date'}, {'name': 'ga:clientId'}, {'name': 'ga:pagePath'}, {'name': 'ga:previousPagePath'}, {'name': 'ga:country'}]
                    'metrics': [{'expression': 'ga:sessions'}],
                    'dimensions': [{'name': 'ga:pagePath'}],
                    'orderBys': [{"fieldName": "ga:sessions", "sortOrder": "DESCENDING"}],
                }]
        }
    ).execute()


def save_response(response):
    """Parses and saves the Analytics Reporting API V4 response to a CSV file.

    Args:
      response: An Analytics Reporting API V4 response.
    """
    dimensionList = []
    valueList = []
    for report in response.get('reports', []):

        columnHeader = report.get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get(
            'metricHeader', {}).get('metricHeaderEntries', [])

        for row in report.get('data', {}).get('rows', []):
            dimensions = row.get('dimensions', [])
            dateRangeValues = row.get('metrics', [])

            for header, dimension in zip(dimensionHeaders, dimensions):
                dimensionList.append(dimension)

            for i, values in enumerate(dateRangeValues):
                for metricHeader, value in zip(metricHeaders, values.get('values')):
                    valueList.append(value)

        data = pd.DataFrame()
        data["Sessions"] = valueList
        data["pagePath"] = dimensionList
        data = data[["pagePath", "Sessions"]]

        data.to_csv("parameter_pages.csv")


def main():
    analytics = initialize_analyticsreporting()
    response = get_report(analytics)
    save_response(response)


if __name__ == '__main__':
    main()
