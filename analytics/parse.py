import pandas as pd


def parse_response(response):
    """Parses and converts the Analytics Reporting API V4 response to a DataFrame.

    Args:
      response: An Analytics Reporting API V4 response.
      https://developers.google.com/analytics/devguides/reporting/core/v4/basics#response_body

    Returns:
        A converted DataFrame.
    """
    # get necessary properties from json
    reports = response['reports'][0]
    # normalize the json response into flat table split into dimensions and metrics
    data = pd.json_normalize(reports['data']['rows'])
    data_dimensions = pd.DataFrame(data['dimensions'].tolist())
    data_metrics = pd.DataFrame(data['metrics'].tolist())
    # use lambda to only get values list
    data_metrics = data_metrics.applymap(lambda x: x['values'])
    data_metrics = pd.DataFrame(data_metrics[0].tolist())
    result = pd.concat([data_dimensions, data_metrics],
                       axis=1, ignore_index=True)
    return result
