# Notes

## TODOS

- [x] parse the raw state-indexes.json into CSV
- [ ] download every individual form
- [ ] figureout why my all state count is 100 less than the site's default open search


## Problem with successfully posting to the form

Using the defaults of requests.Session will result in getting a 403 response when attempting to post the form:

> Forbidden (403)
  CSRF verification failed. Request aborted.

>  You are seeing this message because this HTTPS site requires a 'Referer header' to be sent by your Web browser, but none was sent. This header is required for security reasons, to ensure that your browser is not being hijacked by third parties.

>  If you have configured your browser to disable 'Referer' headers, please re-enable them, at least for this site, or for HTTPS connections, or for 'same-origin' requests.

>  If you are using the <meta name="referrer" content="no-referrer"> tag or including the 'Referrer-Policy: no-referrer' header, please remove them. The CSRF protection requires the 'Referer' header to do strict referer checking. If you're concerned about privacy, use alternatives like <a rel="noreferrer" ...> for links to third-party sites.
 
    session.headers['Referer'] = 'https://efdsearch.senate.gov/search/home/'


## Example search

```
first_name=&last_name=&filer_type=1&senator_state=IA&filer_type=4&candidate_state=&filer_type=5&submitted_start_date=01%2F01%2F2018&submitted_end_date=12%2F31%2F2018&csrfmiddlewaretoken=SOMETOKEN


data refresh:
draw=2&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=1&order%5B0%5D%5Bdir%5D=asc&order%5B1%5D%5Bcolumn%5D=0&order%5B1%5D%5Bdir%5D=asc&start=0&length=100&search%5Bvalue%5D=&search%5Bregex%5D=false&report_types=%5B%5D&filer_types=%5B1%2C+4%2C+5%5D&submitted_start_date=01%2F01%2F2018+00%3A00%3A00&submitted_end_date=12%2F31%2F2018+23%3A59%3A59&candidate_state=&senator_state=IA&office_id=&first_name=&last_name=
```



