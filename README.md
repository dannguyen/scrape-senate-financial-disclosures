# Scraping Senate Financial Disclosures

## Random update notes to myself

- 2020-02-27: I have no idea where I left off, other than remembering I should re-run scrapes once in awhile since older reports/senators may be removed from the Senate site from time to time. Last scrape was 2019-11-21




## Prelim examination

Parse the extracted JSON data:

```
$ python efdsenate parse_raw
```

> Note (2020-02-28): I have no idea what the above command refers to. Ignore it please.

How many paper records have been submitted, by year?

```sh
$ ack 'view/paper' -A1 data/state-indexes/*.json \
    | ack '"\d{2}/\d{2}/(\d{4})"' --output '$1' \
    | sort | uniq -c
```

```
 251 2012
 455 2013
 155 2014
  72 2015
  57 2016
  54 2017
  77 2018
  31 2019
```

Analyze the doc titles

```
cat data/parsed/state-indexes.csv \
    | csvgrep -c doc_url -r '/ptr' \
    | csvcut -c doc_title

 cat data/parsed/state-indexes.csv \
    | csvcut -c doc_url | ack -o '(?<=view/)\w+' | sort | uniq -c
```

```
# paper in 2019
cat data/parsed/state-indexes.csv \
    | csvgrep -c doc_url -r 'view/paper' \
    | csvgrep -c date -r '201[9]' \
    | csvgrep -c doc_type -r 'Annual' \
    | csvgrep -c doc_type -i -r 'Amendment' \
    | csvgrep -c filer_type -r '^Senator' \
    |   csvcut -c state,last_name,first_name,date,doc_type


cat data/parsed/state-indexes.csv \
    | csvgrep -c doc_url -r 'view/annual' \
    | csvgrep -c date -r '201[9]' \
    | csvgrep -c doc_type -r 'Annual' \
    | csvgrep -c doc_type -i -r 'Amendment' \
    | csvgrep -c filer_type -r '^Senator' \
    |   csvcut -c state,last_name,first_name,date,doc_type

```



```
 cat data/parsed/state-indexes.csv | csvgrep -c doc_type -r 'Periodic|Financial' | csvgrep -c doc_filetype -m 'paper' | csvcut -c last_name,first_name,date | ack '(.+?),(\d{4})' --output '$2  $1' | sort | uniq -c

```
