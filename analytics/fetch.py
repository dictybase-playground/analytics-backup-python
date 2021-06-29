from analytics.params import AnalyticsParams


def get_report(analytics, params: AnalyticsParams):
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
                    'viewId': params.viewId,
                    'dateRanges': [{'startDate': params.startDate, 'endDate': params.endDate}],
                    # https://ga-dev-tools.appspot.com/dimensions-metrics-explorer/
                    # 'metrics': [{'expression': 'ga:sessions'}, {'expression': 'ga:users'}, {'expression': 'ga:pageviews'}, {'expression': 'ga:exits'}],
                    # 'dimensions': [{'name': 'ga:date'}, {'name': 'ga:clientId'}, {'name': 'ga:pagePath'}, {'name': 'ga:previousPagePath'}, {'name': 'ga:country'}]
                    'metrics': [{'expression': 'ga:sessions'}],
                    'dimensions': [{'name': 'ga:pagePath'}],
                    'orderBys': [{"fieldName": "ga:sessions", "sortOrder": "DESCENDING"}],
                }]
        }
    ).execute()
