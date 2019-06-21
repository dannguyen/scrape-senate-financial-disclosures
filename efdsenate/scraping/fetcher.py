# from datetime import date
import json
from lxml.html import fromstring as hparse
from pathlib import Path
import requests
from urllib.parse import urljoin

from constants import DEFAULT_SEARCHDATA_PARAMS, DEFAULT_SEARCHDATA_HEADERS, DEFAULT_USER_AGENT

URL_HOMEPAGE = 'https://efdsearch.senate.gov/search/home/'
URL_SEARCH = 'https://efdsearch.senate.gov/search/'
URL_DATASEARCH = 'https://efdsearch.senate.gov/search/report/data/'


def _agree_to_form(session):
    res_g = session.get(URL_HOMEPAGE)
    formvals = {'prohibition_agreement': 1,
                'csrfmiddlewaretoken': _extract_csrftoken(res_g.text)}
    session.headers['Referer'] = 'https://efdsearch.senate.gov/search/home/'
    p = session.post(URL_HOMEPAGE, formvals)
    return session, p

def _extract_csrftoken(html):
    doc = hparse(html)
    return doc.xpath("//input[@name='csrfmiddlewaretoken']/@value")[0]

def init_scraper():
    s = requests.Session()
    s.headers['User-Agent'] = DEFAULT_USER_AGENT
    s, search_resp = _agree_to_form(s)
    s.headers['Referer'] = URL_SEARCH
    s.headers['DNT'] = '1'
    s.headers['Host'] = 'efdsearch.senate.gov'
    s.headers['Origin'] = 'https://efdsearch.senate.gov'
    s.headers['Upgrade-Insecure-Requests'] = '1'
    s.headers['Pragma'] = 'no-cache'
    s.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'

    return s, search_resp


def scrape_by_state(state):
    records = []
    responses = []

    s, _rx = init_scraper()
    qheaders = DEFAULT_SEARCHDATA_HEADERS.copy()
    qheaders['Cookie'] = _rx.request.headers['Cookie']
    qheaders['X-CSRFToken'] = s.cookies.get('csrftoken')

    qparams = DEFAULT_SEARCHDATA_PARAMS.copy()
    qparams['senator_state'] = qparams['candidate_state'] = state

    rbody = None
    while len(responses) == 0 or len(records) < rbody['recordsTotal']:
        resp = s.post(URL_DATASEARCH, data=qparams, headers=qheaders)
        responses.append(resp)

        rbody = resp.json()
        records.extend(rbody['data'])

        i = int(qparams['start'][0])
        qparams['start'] = [str(i+100)]
#        print(i, len(records), 'out of:', rbody['recordsTotal'])


    return s, responses, records






"""
from urllib.parse import parse_qs

from efdsenate.scraper import _extract_csrftoken, _agree_to_form
from efdsenate.scraper import *
s, r = scrape_by_state('IA')

sx, rx = init_scraper()


"""
