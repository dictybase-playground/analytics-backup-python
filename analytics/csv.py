import time
import pandas as pd
from typing import List


def get_csv_headers(response):
    """Parses the Analytics Reporting API V4 response and returns a list of column headers.

    Args:
      response: An Analytics Reporting API V4 response.
      https://developers.google.com/analytics/devguides/reporting/core/v4/basics#response_body
    Returns:
      The list of header column strings.
    """
    # get necessary properties from json
    reports = response['reports'][0]
    columnHeaders = reports['columnHeader']['dimensions']
    metricHeaders = reports['columnHeader']['metricHeader']['metricHeaderEntries']
    # use dimensions and metrics both as column headers
    columns = columnHeaders
    for metric in metricHeaders:
        columns.append(metric['name'])
    return columns


def save_response(result: pd.DataFrame, columns: List[str], viewId: str):
    """Saves DataFrame to a CSV file with specified header columns.

    Args:
      result: DataFrame.
      columns: List[str]
      viewId: string
    Returns:
      The filename of the report (string).
    """
    timestr = time.strftime("%Y%m%d")
    filename = timestr + "-" + viewId + ".csv"
    result.to_csv(filename, header=columns)
    return filename
