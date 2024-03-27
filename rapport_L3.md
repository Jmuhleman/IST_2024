---
title: IST - Lab 03
subject: OBJECT STORAGE (AMAZON S3)
author: Butty Vicky & Mühlemann Julien
group: L03GrB
date: 26.03.2024
---

<div style="page-break-after: always; break-after: page;"></div>

## TASK 2: USE THE AWS COMMAND-LINE INTERFACE TO MANAGE BUCKETS AND OBJECTS

> 5. Manipulate buckets and objects. Use the documentation [Using high-level (S3) commands with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html) as a reference.
>
> - Create a new bucket.

We can create a new bucket with the command :

```bash
$ aws s3 mb s3://ist-grb-butty-bucket-2
make_bucket: ist-grb-butty-bucket-2
```

We can then check that the bucket was correctly created with the `aws s3 ls` command. 



> - Upload an object.

We decided to upload the .csv generated earlier, which is made with the copy command :

```bash
$ aws s3 cp ./data/lab2.csv s3://ist-grb-butty-bucket-2
upload: data\lab2.csv to s3://ist-grb-butty-bucket-2/lab2.csv
```



> - List the objects in the bucket.

```bash
$ aws s3 ls s3://ist-grb-butty-bucket-2
2024-03-26 17:15:50        335 lab2.csv
```



> - Copy the object.

We decided to copy the file from our first bucket to the second one :

```bash
$ aws s3 cp s3://ist-grb-butty-bucket/lab.csv s3://ist-grb-butty-bucket-2/lab.csv
copy: s3://ist-grb-butty-bucket/lab.csv to s3://ist-grb-butty-bucket-2/lab.csv
```

We check with the previous command that our new object was correctly copied :

```bash
$ aws s3 ls s3://ist-grb-butty-bucket-2
2024-03-26 17:17:07        335 lab.csv
2024-03-26 17:15:50        335 lab2.csv
```



> - Delete the copied object.

```bash
$ aws s3 rm s3://ist-grb-butty-bucket-2/lab.csv
delete: s3://ist-grb-butty-bucket-2/lab.csv
```



> 6. S3 folders behave differently from file system folders. In fact a folder in S3 is a 0-byte object whose name ends with a slash (`/`). Read the introduction on the page [Organizing objects in the Amazon S3 console using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html).
>
> - Create a folder (using the Management Console).
> - Make a copy of the object and move the copy into the folder.
> - What happens if you move an object to a folder that does not exist?

If we move an object to a folder that doesn't exist, the folder will be automatically created. Since the folder exist only conceptually, the system add the prefix on the file name to simulate the folder.



## TASK 3: CREATE A STATIC WEB SITE

> 1. Follow the instructions of the [Tutorial: Configuring a static website on Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html) to create a new bucket for a static web site.
>    - You can use web site content (index.html, CSS stylesheet, error document) of your liking.

As recommended at the end of the tutorial, we deleted the buckets to avoid unwanted costs. Therefore, we made a screenshot to show the base pages that were created for this task:

The index page :

![Lab03_Task3_index](./assets/Lab03_Task3_index.png)

The error page :

![Lab03_Task3_error](./assets/Lab03_Task3_error.png)



> 2. On which URL is your new website reachable?

The Web site was accessible at the URL `http://ist-grb-butty-bucket-2.s3-website-us-east-1.amazonaws.com`, as shown in the screenshots.



## TASK 4: EXPLORE A PUBLIC BUCKET WITH A LARGE DATASET

> 1. The data location of the Common Crawl datasets is described on the page [Get Started](https://commoncrawl.org/the-data/get-started/). When was the latest crawl? What is the bucket name? Under which prefix is the latest crawl stored?

The latest crawl, named `CC-MAIN-2024-10` , has been created on february / march 2024. The latest crawl archive is located in the `commoncrawl` bucket, under the prefix `crawl-data/CC-MAIN-2024-10/`. 



> 2. Log into the AWS S3 Management Console. Replace the browser URL with
>
> ```
>  https://s3.console.aws.amazon.com/s3/buckets/<bucketname>/
> ```
>
> Where you replace `<bucketname>` with the name of the bucket. You should see a bucket with objects and folders.

The URL used here is : ` https://s3.console.aws.amazon.com/s3/buckets/commoncrawl/` 



> 3. Navigate to the root folder of the latest crawl. Click on the object `index.html`. Click the `Open` button to load it into your browser. What is the URL of this object?

The URL of the object is `https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-2024-10/index.html`. When we click on the `open` button, parameters are added at the end of the URL :

```
https://commoncrawl.s3.us-east-1.amazonaws.com/crawl-data/CC-MAIN-2024-10/index.html?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDGV1LWNlbnRyYWwtMSJHMEUCIQCV1SsooOv9wkun0SjtrAnhKJU5EzkKP%2BLOJM7mOSd6zQIgWEWqxka%2BNEGQsiicSS4b6PZOFqoxoXpVGvZnDm1gdYQqhAMIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw4NTE3MjU1ODE4NTEiDDs9Bn1xq8rNxINiKyrYAkQBWHqWjOEsqKTwH36nrIGEsV4OPIy8lj8JS%2F9FKrzeh7b143dOoHTOBqbf%2FJDj%2BMEzP1gILocZRzCcN7Gbnsxgn6EljpRvVzJSakHQQFG9k07iRQ%2B4R6lYqqoVSgFqGHsBmpjqqT7fBhWXkRkfGRgyyPAdxVyXG%2FEgNac2aNVE0cZgmroRp1D2wfnn8K5E6En1RjQnjsXEDbw%2Bd04uU4lIAv6rcxjsZrcaFa17hE62XddxySWD4laF%2Brei0AeeL%2BfbwlQ2A%2FErLDrexCyEq1K3rx3q547Pw6SGVBa54yxYPGvs8AfscEQWz3OA528Lx4SLjYcRyU3emnANb%2BuP14NcBjLbWuKceuVqbIZEHkMUzYtr7Uo5BmSKPNVB0UjCfCLQZirOBb1BlsC1sIcV%2FG8XcJFhHKvl%2F0VlAQi2S36j9heTJr8lqrleG%2FUXaF63eZjm%2F2Gi2Qz6MMnEjLAGOrMC83Z06xHt2JRPZZg2O2le4MHECHd0V3Gp0FZzqKauh2%2FJPastHe5k%2FPiOAVdNct5fRctIGQ08qAdzVwDijiaoCn7%2BybT5KRRwOBrhhmFi08kAHR7bn%2B3N1wiMBebXFyr3nqrrxW0Rd28oAsH%2BehtAlq%2FGW8tMhs30TsPvuldTq8MhOzjfzcTRFmqJCnQJ8Xt48I8BQQHdaemVQ1HVEL6CH0Bkl0ND3rWa%2BgEx9qi9aPpINbaJXuOMTp0j%2FY%2FmgiYzR4A2ndy%2Bq%2BUgvOZLxzDn4fm%2FQxiJm%2F%2Bn7eryj%2Fw5mAfh%2FYapjYr8fZSGHMmhayEYGm4tlkkvw64KloYuYwlMuQytI8%2F%2BYolTXl6T1Df47a9K5IhPlqUK3%2BWLozGSF9WotjdLnbRp%2FC1QQEizH1IclaVQgw%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240326T195313Z&X-Amz-SignedHeaders=host&X-Amz-Expires=299&X-Amz-Credential=ASIA4MTWM7YNYKHKSI6C%2F20240326%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d91793c600fe26ce0d6e91936b5907e078d1e1a963b8f54e62bc864d2a95fdb8
```



> 4.  Explore a bit the objects and folders.
>
> - What are WARC, WAT and WET files (look at the Get Started guide)?

The `Get Started` guide provide the following informations about the files format :

> **The WARC Format**
>
> The WARC format is the raw data from the crawl, providing a direct mapping to the crawl process.
>
> Not only does the format store the HTTP response from the websites it contacts (WARC-Type: response), it also stores information about how that information was requested (WARC-Type: request) and metadata on the crawl process itself (WARC-Type: metadata).

> **The WAT Format**
>
> The acronym WAT stands for "Web Archive Transformation".
>
> ‍‍WAT files contain important metadata about the records stored in the WARC format. This metadata is computed for each of the three types of records (metadata, request, and response).

> **The WET Format**
>
> The acronym WET stands for "WARC Encapsulated Text".
>
> As many tasks only require textual information, the Common Crawl dataset provides WET files that only contain extracted plaintext.

We can summary this as the following :

- The `WARC` files store the raw crawl data.
- The `WAT` files store computed meta data for the data stored in the `WARC` files.
- The `WET` files store plaintext extracted from the `WARC` files.



> - What is the typical size of a WARC file (ballpark)?

The file can be hundreds of terabytes in size, depending on the number and size of the website archived. For example, the latest crawl has a `WARC` file of  90.36 TiB.

 

> - Why is it not sufficient to just store the WARC, WAT and WET files in the bucket? What other type of file is needed?

Because they may not provide all the necessary information for retrieval and analysis.
We may need an additional type of files, such as index files, to improve searchability for proper data mining operations.



> - What storage classes have the Common Crawl developers chosen to store the data?

The Common Crawl developers have chosen to store the data with the following two classes :

- AWS S3 Standard: Default storage for frequent access and high performance in latency.
- AWS S3 Intelligent-Tiering: Optimizes storage costs by automatically moving data to the most cost-effective access tier when access patterns change.



## TASK 5: SCENARIO

> You are a data engineer at Coop responsible for a data product. The product is the global Coop sales data, which is shared with several Coop departments. Your task is to add each week the new sales data of the week to an S3 bucket.
>
> How would you do this task? Describe your thought process. 

1. Understand the data
   Determine if sales data contains sensitive information that requires compliance with GDPR, CCPA, and other data protection regulations.

2. Bucket structure
   Directory structure: Design a logical directory structure within the bucket to efficiently organize data. We could create a structure of folders by department.

3. Data control
   We may need to implement validation checks to ensure data integrity before uploading to buckets.

4. Automate data upload
   We could automate the process of uploading the data to the S3 bucket. The script would include steps for data validation, possibly conversion, and finally upload.

5. Data security
   Use IAM roles and policies to tightly control access to the S3 bucket. Ensure that only authorized departments and users can access or modify sales data.

6. Data accessibility
   If departments have separate AWS accounts, set up cross-account access to securely share the contents of the S3 bucket. Implement lifecycle policies to archive or delete old data that is no longer needed, such as migrating it to AWS Glacier storage class.
   
7. Monitor and Optimize
   Regularly review the process for efficiency and cost optimization. Monitor storage costs, access patterns, performance analysis, etc.
