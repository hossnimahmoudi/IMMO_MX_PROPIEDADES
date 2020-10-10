## How to launch a spider
 - Create a virtualEnv Python3 
 - Install NEUKOLLN
 - launch prop1_luminati.py ,  prop2_luminati.py and  prop3_luminati.py
 - Merge the 3 CSV files
 - Drop all duplicated rows based on field ID_CLIENT

<hr>

## Follow this steps

- Launch each spider in different Screen 
``` 
scrapy crawl name_of_spider_1 -o name_file_csv_1.csv
scrapy crawl name_of_spider_2 -o name_file_csv_2.csv
scrapy crawl name_of_spider_3 -o name_file_csv_3.csv
```

- Merge all the CSV files 
```
cat name_file_csv_1.csv name_file_csv_2.csv name_file_csv_3.csv > merge_files.csv
```

- Drop duplicate
```
sort -u -k3,3 -t";" merge_files.csv > merge_file_without_dup.csv
```