# IST Lab 03 : OBJECT STORAGE (AMAZON S3)

Authors : Butty Vicky & Mühlemann Julien

Group : L01GrB

Date : 26.03.2024

## TASK 2: USE THE AWS COMMAND-LINE INTERFACE TO MANAGE BUCKETS AND OBJECTS

> 5. What happens if you move an object to a folder that does not exist?

```
The folder will be automaticly created. Since the folder exist only conceptually, the system add the prefix on the file name to simulate the folder.
```


# TASK 3: CREATE A STATIC WEB SITE

> 2. On which URL is your new website reachable?
```
The URL is reachable with the following link:
http://grb-muhlemann-webs.s3-website-us-east-1.amazonaws.com
```

# TASK 4: EXPLORE A PUBLIC BUCKET WITH A LARGE DATASET

> 1. The data location of the Common Crawl datasets is described on the page Get Started. When was the latest crawl?
```
The latest crawl has been created as of february - march 2024
(Common Crawl February/March 2024 Crawl Archive (CC-MAIN-2024-10))
```
> 1.  What is the bucket name?

```
The bucket name is s3://commoncrawl
```

> 1. Under which prefix is the latest crawl stored?

TODO: check that 
```
With the prefix .gz
```

> 3. Navigate to the root folder of the latest crawl. Click on the object index.html. Click the Open button to load it into your browser. 
> What is the URL of this object?

```
https://commoncrawl.s3.us-east-1.amazonaws.com/index.html?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaDGV1LWNlbnRyYWwtMSJGMEQCICAA3bo2d4QuKNhtr9gDF3AHP%2Fe7NaYHO19%2Fn%2FQPhqkVAiB8%2BYXAiox3frCDnhke6vrg0PRsIWdVX7tLdDpy3PxUsCr7AggxEAAaDDg1MTcyNTU4MTg1MSIMS1ZlNxaweD0Wj%2FtjKtgCqGZcab%2BdRElbYocdMMObDIkyxa3Mdv73jXxvnJjlwZkw1lBeQ%2FE2QUR27gUF9gA9SsvDfgc%2FZ7RwdakobJ4dpYmgM6J9kUKtRF76aU%2Fqx8QoUqRVdlIZOGp68JSe9expgwZv3OkMER8nbo1sam5za8JHTbjGuMo7zQ%2BQkDuQJ1%2BCNjR%2BhLY6vlqA26CBy8e7n%2BVyIFUBqHBPISbabYBOEgDtbCGMdRuooOlmM0BWNM3R41jrHnucxh2H%2FBAOtT0KrjuH3uDALPfEoJYH5y3Jehu2ViG6TOO9pIZ0z5J0DQZlsyZ1vGA7Dbxka%2FLGq3yLzPRDGJC9HQonCyQUiDlc8sGBno5se0d5PuyfABUupDq7WWtGd6j%2BeITQDv1n1gBmVWf6rTsFeBLPvGhk7z%2FTUAdWLEAPVcx0ueyfVR8RcGgNm39ywrHPKVfZiVXvdqMyn7oTpZfusFEw3PDvrwY6tALg%2FUdAjaEdY1mLNmRgV5PO0%2BXBSlcs3sun8n408JeRC5ml0zaP198i%2FcxnkbG1jcTG%2BpHS7xL9DcghDSxWqc9AA24FKHP2eq3Ps7VJ3%2B3Mec%2B%2FXrBkfCQ1cyFkaTdkIwV7NVkooedtGaR5pvYwHrhrPpFx%2BXLe1wQ6%2B1GoPnvaC8rKE%2FpnN4EW75jHSyL%2FHxZrdjuLXD%2FYFRInF4JIIV5kns2%2F2w01El9sn1T8kNq%2BGpniNgCyymdXog827DdrNYwk2FCwp0N4fF%2FK2GIBxvQAFUOs9M4ZlPOhxKpUPRedT2gqw7UfIePiQso%2BDcjzoBWKkNJHeJiQxNcWmicAve%2FFBdgEunB6QCxC9STNgl%2BQtdMt36SjZ5B1lqx5I5QBi40GhSOb48sekyhXri8kKkULdNg3sA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240321T192451Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIA4MTWM7YN47RHUM5V%2F20240321%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=3e463dfbb937cc20645aea0c8fe32c9c9130d12661512ddc1a9ccfcdf6231ecf

```


> 4. What are WARC, WAT and WET files (look at the Get Started guide)?

```
The WARC format
This format is the raw data from the crawl, providing a direct mapping to the crawl process.
Not only does the format store the HTTP response from the websites it contacts (WARC-Type: response), it also stores information about how that information was requested (WARC-Type: request) and metadata on the crawl process itself (WARC-Type: metadata).


The WAT Format
The acronym WAT stands for "Web Archive Transformation".
‍WAT files contain important metadata about the records stored in the WARC format. This metadata is computed for each of the three types of records (metadata, request, and response).


The WET Format
The acronym WET stands for "WARC Encapsulated Text".
As many tasks only require textual information, the Common Crawl dataset provides WET files that only contain extracted plaintext.
```


> 4. What is the typical size of a WARC file (ballpark)?

```
 hundreds of terabytes in size.
```


> 4. Why is it not sufficient to just store the WARC, WAT and WET files in the bucket?
> What other type of file is needed?

```
Because they may not provide all the necessary information for retrieval and analysis.
we may need an extra kind of files such as index files to enhance the searchability for proper data mining operations.
```


> 4. What storage classes have the Common Crawl developers chosen to store the data?

``` 
As far as we have seen in the buckets, the devs have choosen to store the data with:
AWS S3 Standard: Default storage for frequent access and high performance in latency.
AWS S3 Intelligent-Tiering: optimises automatically data into acess tiers accordign use of data.
```

# TASK 5: SCENARIO

> How would you do this task? Describe your thought process.

```
1. Understand data
Determine if the sales data contains sensitive information requiring compliance with data protection regulations GDPR, CCPA.

2. Bucket structure
Directory Structure: Design a logical directory structure within the bucket to organize data efficiently. We could create a structure of folders according departments.

3. Data control
We may need to implement validation checks to ensure data integrity before upload to buckets.

4. Automation of Data Upload
We could automate the process of uploading the data to the S3 bucket. The script would include steps for data validation, eventually convertion, and finally, the upload.

5. Data Security and Compliance
Access Control: Use IAM roles and policies to strictly control access to the S3 bucket. Ensure that only authorized departments and users can access or modify the sales data.

6. Data Accessibility
Cross-Account Access: If departments have separate AWS accounts, set up cross-account access to allow secure sharing of the S3 bucket's contents.
Implement lifecycle policies to archive or delete old data that is no longer needed e.g migrate them on AWS Glacier storage class.

7. Monitoring and Optimization
Regularly review the pocess for efficiency and cost optimisation. 
Mmonitoring storage costs, access patterns performances analysis. etc...
```