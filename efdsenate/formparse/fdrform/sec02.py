from helpers import cleantext
from formparse.fdrform.utils import parse_section

def parsec_02(sec):
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
            <h3 class="h4">Part 2. Earned and Non-Investment Income

            </h3>
            <p>
                Did you or your spouse have reportable earned income or non-investment income?
                <strong>

                        No

                </strong>
            </p>
        </div>

    </section>
"""



################### YES (Romney 2018)
"""
<section class="card mb-2">
        <div class="card-body">
            <h3 class="h4">Part 2. Earned and Non-Investment Income

            </h3>
            <p>
                Did you or your spouse have reportable earned income or non-investment income?
                <strong>

                        Yes

                </strong>
            </p>
        </div>

            <div class="table-responsive">
                <table class="table table-striped ">
                    <caption class="sr-only">List of payments added to this report</caption>
                    <thead>
                    <tr class="header">
                        <th scope="col"></th>
                        <th scope="col">#</th>
                        <th scope="col">Who Was Paid</th>
                        <th scope="col">Type</th>
                        <th scope="col">Who Paid</th>
                        <th scope="col">Amount Paid</th>
                    </tr>
                    </thead>
                    <tbody>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                1</td>
                            <td>
                                Self

                            </td>
                            <td>
                                Other
                                <br>
                                    <div class="muted">(Director Fee)</div>

                            </td>
                            <td>
                                Marriott International<br>
                                <div class="muted">Bethesda, MD</div>
                            </td>

                                <td>$131,039.00</td>

                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                2</td>
                            <td>
                                Self

                            </td>
                            <td>
                                Other
                                <br>
                                    <div class="muted">(Director Fee)</div>

                            </td>
                            <td>
                                Solamere Capital<br>
                                <div class="muted">Boston, MA</div>
                            </td>

                                <td>$220,000.00</td>

                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                3</td>
                            <td>
                                Self

                            </td>
                            <td>
                                Retirement


                            </td>
                            <td>
                                Goldman Sachs IRA Account (Retirement Account Distribution)<br>
                                <div class="muted">New York, NY</div>
                            </td>

                                <td>$1,675,642.00</td>

                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                4</td>
                            <td>
                                Spouse

                            </td>
                            <td>
                                Royalties


                            </td>
                            <td>
                                St. Martin's Press (Publisher of "In This Together")<br>
                                <div class="muted">New York, NY</div>
                            </td>

                                <td> &gt; $1,000</td>

                        </tr>

                    </tbody>
                </table>
            </div>

    </section>
    """
