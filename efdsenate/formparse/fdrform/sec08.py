from helpers import cleantext
from formparse.fdrform.utils import parse_section

def parsec_08(sec):
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
            <h3 class="h4">Part 8. Positions

            </h3>
            <p>
                Did you hold any outside positions during the reporting period?
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
            <h3 class="h4">Part 8. Positions

            </h3>
            <p>
                Did you hold any outside positions during the reporting period?
                <strong>

                        Yes

                </strong>
            </p>
        </div>

            <div class="table-responsive">
                <table class="table table-striped">
                    <caption class="sr-only">List of outside employment added to this report</caption>
                    <thead>
                    <tr class="header">
                        <th scope="col"></th>
                        <th scope="col">#</th>
                        <th scope="col">Position Dates</th>
                        <th scope="col">Position Held</th>
                        <th scope="col">Entity</th>
                        <th scope="col">Entity Type</th>
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
                                Apr 2005 to
                                present
                            </td>
                            <td>
                                Officer

                            </td>
                            <td>
                                Corker Development Corporation
                                <div class="muted">
                                    Chattanooga, TN
                                </div>
                            </td>
                            <td>
                                Corporation

                            </td>
                            <td></td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                2</td>
                            <td>
                                Dec 1997 to
                                present
                            </td>
                            <td>
                                Director

                            </td>
                            <td>
                                Corker Properties X, LP
                                <div class="muted">
                                    Chattanooga, TN
                                </div>
                            </td>
                            <td>
                                Other
                                (Tennessee Limited Partnership)
                            </td>
                            <td></td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                3</td>
                            <td>
                                Aug 2006 to
                                present
                            </td>
                            <td>
                                Trustee

                            </td>
                            <td>
                                Emily Corker 2006 Trust
                                <div class="muted">
                                    Chattanooga, TN
                                </div>
                            </td>
                            <td>
                                Other
                                (Trust)
                            </td>
                            <td></td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                4</td>
                            <td>
                                Aug 2006 to
                                present
                            </td>
                            <td>
                                Trustee

                            </td>
                            <td>
                                Julia Corker 2006 Trust
                                <div class="muted">
                                    Chattanooga, TN
                                </div>
                            </td>
                            <td>
                                Other
                                (Trust)
                            </td>
                            <td></td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                5</td>
                            <td>
                                Jun 2014 to
                                present
                            </td>
                            <td>
                                Other
                                (Member)
                            </td>
                            <td>
                                NLL, LLC
                                <div class="muted">
                                    Dover, DE
                                </div>
                            </td>
                            <td>
                                Corporation

                            </td>
                            <td></td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                6</td>
                            <td>
                                Jan 2015 to
                                present
                            </td>
                            <td>
                                Other
                                (Member)
                            </td>
                            <td>
                                1150, LLC
                                <div class="muted">
                                    Chattanooga, TN
                                </div>
                            </td>
                            <td>
                                Corporation

                            </td>
                            <td></td>
                        </tr>

                    </tbody>
                </table>
            </div>

    </section>
"""
