from helpers import cleantext
from formparse.fdrform.utils import parse_section

def parsec_07(sec):
    data = {}

    data['title'] = sec.cssselect('h3')[0].text
    _p = sec.cssselect('p')[0]
    _r = list(_p)[0]
    data['prompt'] = cleantext(_p.text)
    data['response'] = cleantext(_r.text)
    data['records'] = extract_table(sec)

    return data



################### No (Brian Ellison 2017)

"""
<section class="card mb-2">
        <div class="card-body">
            <h3 class="h4">Part 7. Liabilities

            </h3>
            <p>
                Did you, your spouse, or dependent child have a liability worth more than $10,000 at any time?
                <strong>

                        No

                </strong>
            </p>
        </div>

    </section>
"""


################### YES (Corker 2015)
"""
<section class="card mb-2">
        <div class="card-body">
            <h3 class="h4">Part 7. Liabilities

            </h3>
            <p>
                Did you, your spouse, or dependent child have a liability worth more than $10,000 at any time?
                <strong>

                        Yes

                </strong>
            </p>
        </div>

            <div class="table-responsive">
                <table class="table table-striped">
                    <caption class="sr-only">List of liabilities added to this report</caption>
                    <thead>
                    <tr class="header">
                        <th scope="col"></th>
                        <th scope="col">#</th>
                        <th scope="col">Incurred</th>
                        <th scope="col">Debtor</th>
                        <th scope="col">Type</th>
                        <th scope="col">Points</th>
                        <th scope="col">Rate<br>(Term)</th>
                        <th scope="col">Amount</th>
                        <th scope="col">Creditor</th>
                        <th scope="col">Comments</th>
                    </tr>
                    </thead>
                    <tbody>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                1</td>
                            <td>
                                2015
                            </td>
                            <td>Self</td>
                            <td>Line of Credit
                                </td>
                            <td>
                                -</td>
                            <td>
                                1.95%<br>

                                                        (revolving line)

                            </td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>
                                Raymond James Bank
                                <div class="muted">St. Petersburg, FL</div>
                            </td>
                            <td>
                                Securities Based Lending Account</td>
                        </tr>

                    </tbody>
                </table>
            </div>

    </section>
"""


