from analytics.params import AnalyticsParams


def get_report(analytics, params: AnalyticsParams, pageToken=None):
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
                    'pageToken': pageToken,
                    'dateRanges': [{'startDate': params.startDate, 'endDate': params.endDate}],
                    # https://ga-dev-tools.appspot.com/dimensions-metrics-explorer/
                    'metrics': [{'expression': 'ga:sessions'}, {'expression': 'ga:users'}, {'expression': 'ga:pageviews'}, {'expression': 'ga:exits'}],
                    'dimensions': [{'name': 'ga:date'}, {'name': 'ga:clientId'}, {'name': 'ga:pagePath'}, {'name': 'ga:previousPagePath'}, {'name': 'ga:country'}],
                }]
        }
    ).execute()
