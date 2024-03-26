# IST Lab 03 : OBJECT STORAGE (AMAZON S3)

Authors : Butty Vicky & Mühlemann Julien

Group : L01GrB

Date : 26.03.2024

## TASK 2: USE THE AWS COMMAND-LINE INTERFACE TO MANAGE BUCKETS AND OBJECTS




http://grb-muhlemann-webs.s3-website-us-east-1.amazonaws.com


Common Crawl February/March 2024 Crawl Archive (CC-MAIN-2024-10)

s3://commoncrawl

warc.paths.gz

https://commoncrawl.s3.us-east-1.amazonaws.com/index.html?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaDGV1LWNlbnRyYWwtMSJGMEQCICAA3bo2d4QuKNhtr9gDF3AHP%2Fe7NaYHO19%2Fn%2FQPhqkVAiB8%2BYXAiox3frCDnhke6vrg0PRsIWdVX7tLdDpy3PxUsCr7AggxEAAaDDg1MTcyNTU4MTg1MSIMS1ZlNxaweD0Wj%2FtjKtgCqGZcab%2BdRElbYocdMMObDIkyxa3Mdv73jXxvnJjlwZkw1lBeQ%2FE2QUR27gUF9gA9SsvDfgc%2FZ7RwdakobJ4dpYmgM6J9kUKtRF76aU%2Fqx8QoUqRVdlIZOGp68JSe9expgwZv3OkMER8nbo1sam5za8JHTbjGuMo7zQ%2BQkDuQJ1%2BCNjR%2BhLY6vlqA26CBy8e7n%2BVyIFUBqHBPISbabYBOEgDtbCGMdRuooOlmM0BWNM3R41jrHnucxh2H%2FBAOtT0KrjuH3uDALPfEoJYH5y3Jehu2ViG6TOO9pIZ0z5J0DQZlsyZ1vGA7Dbxka%2FLGq3yLzPRDGJC9HQonCyQUiDlc8sGBno5se0d5PuyfABUupDq7WWtGd6j%2BeITQDv1n1gBmVWf6rTsFeBLPvGhk7z%2FTUAdWLEAPVcx0ueyfVR8RcGgNm39ywrHPKVfZiVXvdqMyn7oTpZfusFEw3PDvrwY6tALg%2FUdAjaEdY1mLNmRgV5PO0%2BXBSlcs3sun8n408JeRC5ml0zaP198i%2FcxnkbG1jcTG%2BpHS7xL9DcghDSxWqc9AA24FKHP2eq3Ps7VJ3%2B3Mec%2B%2FXrBkfCQ1cyFkaTdkIwV7NVkooedtGaR5pvYwHrhrPpFx%2BXLe1wQ6%2B1GoPnvaC8rKE%2FpnN4EW75jHSyL%2FHxZrdjuLXD%2FYFRInF4JIIV5kns2%2F2w01El9sn1T8kNq%2BGpniNgCyymdXog827DdrNYwk2FCwp0N4fF%2FK2GIBxvQAFUOs9M4ZlPOhxKpUPRedT2gqw7UfIePiQso%2BDcjzoBWKkNJHeJiQxNcWmicAve%2FFBdgEunB6QCxC9STNgl%2BQtdMt36SjZ5B1lqx5I5QBi40GhSOb48sekyhXri8kKkULdNg3sA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240321T192451Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIA4MTWM7YN47RHUM5V%2F20240321%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=3e463dfbb937cc20645aea0c8fe32c9c9130d12661512ddc1a9ccfcdf6231ecf







The WARC Format

The WARC format is the raw data from the crawl, providing a direct mapping to the crawl process.

Not only does the format store the HTTP response from the websites it contacts (WARC-Type: response), it also stores information about how that information was requested (WARC-Type: request) and metadata on the crawl process itself (WARC-Type: metadata).

For the HTTP responses themselves, the raw response is stored. This not only includes the response itself, (what you would get if you downloaded the file) but also the HTTP header information, which can be used to glean a number of interesting insights.

In the example below, we can see the crawler contacted https://en.wikipedia.org/wiki/Saturn and received HTML in response.

We can also see the page sets caching details, and attempts to set a cookie (shortened for display here).










The WAT Format

The acronym WAT stands for "Web Archive Transformation".

‍WAT files contain important metadata about the records stored in the WARC format. This metadata is computed for each of the three types of records (metadata, request, and response).

If the information crawled is HTML, the computed metadata includes the HTTP headers returned and the links (including the type of link) listed on the page. This information is stored as JSON.

To keep the file sizes as small as possible, the JSON is stored with all unnecessary whitespace stripped, resulting in a relatively unreadable format for humans. If you want to inspect the file yourself, you can use one of the many formatting tools available, such as JSONFormatter.io.
‍
The HTTP response metadata is most likely to be of interest to Common Crawl users. The skeleton of the JSON format is outlined below:











The WET Format

The acronym WET stands for "WARC Encapsulated Text".

As many tasks only require textual information, the Common Crawl dataset provides WET files that only contain extracted plaintext.

The way in which this textual data is stored in the WET format is quite simple: the WARC metadata contains various details, including the URL and the length of the plaintext data, with the plaintext data following immediately afterwards.













 hundreds of terabytes in size.











1. Index Files:
The most significant type of file that you would need in addition to WARC, WAT, and WET files is an index file. Index files are crucial for efficiently searching and retrieving content from the archive. They map keywords, URLs, or other metadata to the locations within WARC files where the actual content is stored. Without an index, finding specific content within large WARC files would be like looking for a needle in a haystack, requiring potentially exhaustive searches through potentially terabytes or more of data.

2. Metadata Files:
While WAT files do contain some metadata, comprehensive metadata files that go beyond what WAT files offer might be necessary for detailed archive management and accessibility. These might include information about the archiving process itself, copyright and licensing information, and more detailed descriptions of the content.

3. Database or Catalogue:
For large-scale web archives, a database or a catalog that organizes all files and their metadata is essential. This system allows for complex queries, tracking of archive integrity, and management of the archive’s structure, ensuring that users can find and access archived content efficiently.

4. Preservation Metadata:
This includes information necessary for the long-term preservation of digital files, such as file format information, checksums for integrity verification, and details about the creation and modification of the files. This type of metadata is critical for ensuring that digital content remains accessible and usable over time, despite changes in technology.

















 Here’s a brief overview of the storage classes used by Common Crawl for its web archives:

Amazon S3 Standard:
Primary Use: This is used for the storage of newly crawled data. The S3 Standard storage class offers high durability, availability, and performance object storage. It's ideal for frequently accessed data and is used by Common Crawl for storing recent crawls because this data is accessed and downloaded by users more frequently.
Amazon S3 Glacier and Deep Archive:
Cost-effective Storage: For older crawls, which are accessed less frequently, Common Crawl may transition the data to Amazon S3 Glacier or even the S3 Glacier Deep Archive storage class. These classes are designed for long-term archiving and backup. They are much more cost-effective for storing large amounts of data that is rarely accessed. The trade-off is that retrieving data from these storage classes takes longer, ranging from minutes to hours, and there might be additional costs for data retrieval.























1. Understand the Data
Format and Size: Understand the format (CSV, JSON, Parquet, etc.) and approximate size of the weekly sales data. This influences the upload method and the structure of the storage.
Sensitivity and Compliance: Determine if the sales data contains sensitive information requiring compliance with data protection regulations (e.g., GDPR, CCPA).
2. Bucket Structure and Naming Convention
S3 Bucket Setup: If not already set up, create an S3 bucket with a clear naming convention that reflects its purpose, for example, coop-global-sales-data.
Directory Structure: Design a logical directory structure within the bucket to organize data efficiently. This could be based on date (year/month/week), region, or department. For instance, 2024/03/W13/.
3. Data Preparation
Pre-upload Processing: Depending on the data format, consider compressing the data or converting it to a more efficient format like Parquet for analytics. This reduces storage costs and improves data query performance.
Data Validation: Implement validation checks to ensure data integrity and correctness before upload.
4. Automation of Data Upload
Automation Tools: Utilize AWS services like AWS Data Pipeline, AWS Lambda, or AWS Glue for automating the data upload process. These tools can be scheduled to run at specific times, such as the end of every week.
Scripting the Upload: Write scripts (e.g., using Python and Boto3 SDK) to automate the process of uploading the new sales data to the S3 bucket. The script would include steps for data validation, compression/conversion, and finally, the upload.
5. Data Security and Compliance
Encryption: Enable encryption at rest (using S3 server-side encryption) and in transit (using SSL/TLS) to protect sensitive data.
Access Control: Use IAM roles and policies to strictly control access to the S3 bucket. Ensure that only authorized departments and users can access or modify the sales data.
Audit and Monitoring: Enable logging and monitoring using AWS CloudTrail and Amazon CloudWatch to track access and changes to the S3 bucket.
6. Data Accessibility and Sharing
Presigned URLs: For sharing specific data files with external parties without granting them broad access to the S3 bucket, consider using presigned URLs.
Cross-Account Access: If departments have separate AWS accounts, set up cross-account access to allow secure sharing of the S3 bucket's contents.
Data Lifecycle Management: Implement lifecycle policies to archive or delete old data that is no longer needed, reducing storage costs.
7. Documentation and Training
Provide documentation on the data structure, access policies, and the process for retrieving or querying the data. Offer training sessions for departments on how to access and use the sales data effectively.
8. Monitoring and Optimization
Regularly review the process for efficiency and cost-effectiveness. This includes monitoring storage costs, access patterns, and exploring AWS offerings for optimizations.