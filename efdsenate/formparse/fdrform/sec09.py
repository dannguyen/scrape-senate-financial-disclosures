from helpers import cleantext
from formparse.fdrform.utils import parse_section

def parsec_09(sec):
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
            <h3 class="h4">Part 9. Agreements

            </h3>
            <p>
                Did you have any reportable agreement or arrangement with an outside entity?
                <strong>

                        No

                </strong>
            </p>
        </div>

    </section>
"""



################### YES (McCaskill 2015)

"""
<section class="card mb-2">
        <div class="card-body">
            <h3 class="h4">Part 9. Agreements

            </h3>
            <p>
                Did you have any reportable agreement or arrangement with an outside entity?
                <strong>

                        Yes

                </strong>
            </p>
        </div>

            <div class="table-responsive">
                <table class="table table-striped ">
                    <caption class="sr-only">List of agreements or arrangements added to this report</caption>
                    <thead>
                    <tr class="header">
                        <th scope="col"></th>
                        <th scope="col">#</th>
                        <th scope="col">Date</th>
                        <th scope="col">Parties Involved</th>
                        <th scope="col">Type</th>
                        <th scope="col">Status and Terms</th>
                    </tr>
                    </thead>
                    <tbody>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                1</td>
                            <td>
                                May 2013
                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Royalty Agreement

                            </td>
                            <td>Agreement to receive book advance and royalty payments based on usual and customary terms for publication of book Plenty Ladylike.</td>
                        </tr>

                    </tbody>
                </table>
            </div>

    </section>
"""
