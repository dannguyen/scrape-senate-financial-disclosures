from helpers import cleantext
from formparse.fdrform.utils import parse_section

def parsec_05(sec):
    data = {}

    data['title'] = sec.cssselect('h3')[0].text
    _p = sec.cssselect('p')[0]
    _r = list(_p)[0]
    data['prompt'] = cleantext(_p.text)
    data['response'] = cleantext(_r.text)
    data['records'] = extract_table(sec)

    return data




################### NO (Corker 2015)
"""
<section class="card mb-2">
        <div class="card-body">
            <h3 class="h4">Part 5. Gifts

            </h3>
            <p>
                Did you, your spouse, or dependent child receive any reportable gift during the reporting period?
                <strong>

                        No

                </strong>
            </p>
        </div>

    </section>
"""



################### YES (Romney 2018)

"""

"""
