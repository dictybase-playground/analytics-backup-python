import cfg
import pandas as pd
from analytics.cmd import parse_cmdline
from analytics.service import initialize_analyticsreporting
from analytics.fetch import get_report
from analytics.parse import parse_response
from analytics.csv import get_csv_headers
from analytics.csv import save_response
from analytics.params import AnalyticsParams
from upload.params import MinioParams
from upload.client import upload_report


def main():
    args = parse_cmdline()
    params = AnalyticsParams(
        viewId=args.viewId,
        startDate=args.startDate,
        endDate=args.endDate,
        dimensions=args.dimensions,
        metrics=args.metrics
    )

    cfg.logger.info("fetching google analytics data...")
    analytics = initialize_analyticsreporting()
    response = get_report(analytics, params)
    data = parse_response(response)
    headers = get_csv_headers(response)
    pageToken = response['reports'][0].get('nextPageToken')

    while pageToken != None:
        print(
            f"fetching next batch of results starting with page token {pageToken}")
        analytics = initialize_analyticsreporting()
        response = get_report(analytics, params, str(int(pageToken)))
        pageToken = response['reports'][0].get('nextPageToken')
        newData = parse_response(response)
        data = pd.concat([data, newData], ignore_index=True)

    cfg.logger.info(f"finished retrieving {len(data.index)} results")
    csv = save_response(data, headers, params.viewId)
    cfg.logger.info(f"successfully saved report to {csv}")

    # upload result to minio
    minioParams = MinioParams(
        endpoint=args.endpoint,
        accessKey=args.accessKey,
        secretKey=args.secretKey,
        bucket=args.bucket,
        filename=csv
    )
    upload_report(minioParams)


if __name__ == '__main__':
    main()
