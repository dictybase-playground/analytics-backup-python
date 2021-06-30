from analytics.params import AnalyticsParams


def get_report(analytics, params: AnalyticsParams, pageToken=None):
    """Queries the Analytics Reporting API V4.

    Args:
      analytics: An authorized Analytics Reporting API V4 service object.
      params: DataClass
      pageToken: str
    Returns:
      The Analytics Reporting API V4 response.
    """
    # convert dimensions and metrics strings into necessary objects
    splitDimensions = params.dimensions.split(",")
    dimensions = list(map((lambda x: {'name': x}), splitDimensions))
    splitMetrics = params.metrics.split(",")
    metrics = list(map((lambda x: {'expression': x}), splitMetrics))

    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': params.viewId,
                    'pageToken': pageToken,
                    'dateRanges': [{'startDate': params.startDate, 'endDate': params.endDate}],
                    # https://ga-dev-tools.appspot.com/dimensions-metrics-explorer/
                    'metrics': metrics,
                    'dimensions': dimensions,
                }]
        }
    ).execute()
