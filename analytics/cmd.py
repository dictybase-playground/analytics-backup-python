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
    return parser.parse_args()
