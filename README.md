# Scraping Senate Financial Disclosures



## Prelim examination

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
