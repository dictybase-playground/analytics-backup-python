import pandas as pd


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

            for _, dimension in zip(dimensionHeaders, dimensions):
                dimensionList.append(dimension)

            for _, values in enumerate(dateRangeValues):
                for _, value in zip(metricHeaders, values.get('values')):
                    valueList.append(value)

        data = pd.DataFrame()
        data["Sessions"] = valueList
        data["pagePath"] = dimensionList
        data = data[["pagePath", "Sessions"]]

        data.to_csv("parameter_pages.csv")
