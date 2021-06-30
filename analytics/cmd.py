import argparse


def parse_cmdline():
    """Command-line interface.

    Returns:
        An object with parsed attributes.
    """
    parser = argparse.ArgumentParser(
        description='generate csv report from google analytics')
    parser.add_argument(
        "-v", "--viewId", help="view id for analytics property", required=True
    )
    parser.add_argument(
        "-s", "--startDate", help="start date for analytics range", required=True)
    parser.add_argument(
        "-e", "--endDate", help="end date for analytics range", required=True)
    parser.add_argument(
        "-o", "--outputFile", help="csv filename to use for output data", default="analytics.csv")
    parser.add_argument(
        "-d", "--dimensions", help="metrics to export for analytics property separated by comma (i.e. ga:date,ga:clientId)", default="ga:date,ga:clientId,ga:pagePath,ga:previousPagePath,ga:country"
    )
    parser.add_argument(
        "-m", "--metrics", help="metrics to export for analytics property separated by comma (i.e. ga:sessions,ga:users)", default="ga:sessions,ga:users,ga:pageviews,ga:exits"
    )
    parser.add_argument(
        "--endpoint", help="minio endpoint", required=True)
    parser.add_argument(
        "--accessKey", help="minio access key", required=True)
    parser.add_argument(
        "--secretKey", help="minio secret key", required=True)
    parser.add_argument(
        "--bucket", help="minio bucket to use as storage (will be created if it doesn't exist)", default="google-analytics")
    return parser.parse_args()
