from helpers import cleantext

def parsec_10(sec):
    data = {}

    data['title'] = sec.cssselect('h3')[0].text
    _p = sec.cssselect('p')[0]
    _r = list(_p)[0]
    data['prompt'] = cleantext(_p.text)
    data['response'] = cleantext(_r.text)
    data['records'] = extract_table(sec)

    return data


################### NO (Sanders 2013)
"""
<section class="card mb-2">
        <div class="card-body">
            <h3 class="h4">Part 10. Compensation

            </h3>
            <p>
                <strong>If this is your first report, or you are a candidate</strong> did you receive compensation of more than $5,000 from a single source in the <strong>two</strong> prior years?
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
