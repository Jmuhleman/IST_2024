<div id='_export_cover' style="height:50vh">
  <div id='_export_title' style="margin-top: 50%;text-align: center;font-size: 1.5rem;">IST - Lab 06</div>
  <div id='_export_subject' style="text-align: center;font-size: 2rem;">'LAB 6: DATA CATALOG AND PARQUET FILES</div>
  <br><br><br><br>
  <div id='_export_author' style="text-align: center;font-size: 1rem;">L06GrJ : Butty Vicky & Mühlemann Julien</div>
  <div id='_export_date' style="text-align: center;font-size: 1rem;">02.05.2024</div>
</div>
<script>
    var $cover = document.querySelector("#_export_cover");
    var title = document.querySelector("meta[name='title']").getAttribute("content");
    var subject = document.querySelector("meta[name='subject']").getAttribute("content");
    var author= document.querySelector("meta[name='author']").getAttribute("content");
    var group = document.querySelector("meta[name='group']").getAttribute("content");
    var date = document.querySelector("meta[name='date']").getAttribute("content");

<div style="page-break-after: always; break-after: page;"></div>


## TASK 1: EXPLORE NEW YORK CITY TAXI TRIP DATA

>Navigate to the TLC Trip Record Data website. The taxi commission publishes data on four types of cabs. Which are they?

1. Yellow taxis: 

2. Green taxis:

3. FHV: for hire vehicles

4. HVFHS: high volume for hire service



>Find the PDF file with the data dictionary for the yellow cab data on web site. Does it contain the data types?
It seems to contain only the descriptions and for some attributes the explanation of the categories.

>The yellow cab data is available in what types of files?
It is only available in PARQUET format.
It seems that some backups are available in csv format according to the bucket.

>Find the copy of the data product in the Registry of Open Data on AWS. What is the bucket name? In which region is the bucket? Open the bucket in the S3 console.

arn:aws:s3:::nyc-tlc is the name of the bucket
region:US East (N. Virginia) us-east-1

>In this lab we are going to use the yellow cab trip data. In which folder are the CSV files for yellow cabs?
>Does this folder only contain yellow cab data?
>In which folder are the Parquet files for yellow cabs? 
>Does this folder only contain yellow cab data?

The csv files for yellow cabs are in the s3::nyc-tlc/opendata_repo/opendata_webconvert/yellow.
Yes they seem to be sorted by vehicle type.
The PARQUET files for yellow cabs are located in the trip_data folder.
no it contains mixed up files from all the vehicle types.


>Is Amazon's copy up-to-date compared to the original data product?