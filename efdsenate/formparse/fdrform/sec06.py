from helpers import cleantext
from formparse.fdrform.utils import parse_section

def parsec_06(sec):
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
            <h3 class="h4">Part 6. Travel

            </h3>
            <p>
                Did you, your spouse, or dependent child receive any <button data-toggle="popover" type="button" aria-haspopup="true" data-html="true" data-title="When is travel reportable? <button type='button' tabindex='0' id='jsPopoverClose' aria-label='close' class='close'><i class='fa fa-times' aria-hidden='true'><span class='sr-only'>Close</span></i></button>" data-template="<div class=&quot;popover popover__fixMedium&quot; role=&quot;tooltip&quot;><div class=&quot;arrow&quot;></div><h3 class=&quot;popover-header&quot;></h3><div class=&quot;popover-body&quot;></div></div>" class="btn btn-link popover--textButton font-weight-bold" data-placement="auto" data-content="<p>If you are reimbursed for more than one trip from the same sponsor, and the trips added together are worth more than $350, then you must report each trip individually, even if the reimbursement for each separate trip does not equal more than $350.</p>">reportable travel</button>?
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
            <h3 class="h4">Part 6. Travel

            </h3>
            <p>
                Did you, your spouse, or dependent child receive any <button data-toggle="popover" type="button" aria-haspopup="true" data-html="true" data-title="When is travel reportable? <button type='button' tabindex='0' id='jsPopoverClose' aria-label='close' class='close'><i class='fa fa-times' aria-hidden='true'><span class='sr-only'>Close</span></i></button>" data-template="<div class=&quot;popover popover__fixMedium&quot; role=&quot;tooltip&quot;><div class=&quot;arrow&quot;></div><h3 class=&quot;popover-header&quot;></h3><div class=&quot;popover-body&quot;></div></div>" class="btn btn-link popover--textButton font-weight-bold" data-placement="auto" data-content="<p>If you are reimbursed for more than one trip from the same sponsor, and the trips added together are worth more than $350, then you must report each trip individually, even if the reimbursement for each separate trip does not equal more than $350.</p>">reportable travel</button>?
                <strong>

                        Yes

                </strong>
            </p>
        </div>

            <div class="table-responsive">
                <table class="table table-striped ">
                    <caption class="sr-only">List of travel added to this report</caption>
                    <thead>
                    <tr class="header">
                        <th scope="col"></th>
                        <th scope="col">#</th>
                        <th scope="col">Date(s)</th>
                        <th scope="col">Traveler(s)</th>
                        <th scope="col">Travel Type</th>
                        <th scope="col">Itinerary</th>
                        <th scope="col">Reimbursed For</th>
                        <th scope="col">Who Paid</th>
                        <th scope="col">Comment</th>
                    </tr>
                    </thead>
                    <tbody>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                1</td>
                            <td>
                                08/10/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>Washington, DC</td>
                            <td>
                                Ground Transportation

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                2</td>
                            <td>
                                08/10/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>New York, NY</td>
                            <td>
                                Ground Transportation

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                3</td>
                            <td>
                                08/10/2015

                                    to
                                    08/12/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>New York, NY</td>
                            <td>
                                Lodging for three nights

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                4</td>
                            <td>
                                08/12/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>New York, NY</td>
                            <td>
                                Ground Transportation

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                5</td>
                            <td>
                                08/14/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>Washington, DC</td>
                            <td>
                                Ground Transportation

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                6</td>
                            <td>
                                08/18/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>San Francisco, CA</td>
                            <td>
                                Lodging for one night

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                7</td>
                            <td>
                                08/18/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>San Francisco, CA</td>
                            <td>
                                Ground Transportation

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                8</td>
                            <td>
                                08/19/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>Los Angeles, CA</td>
                            <td>
                                Ground Transportation

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                9</td>
                            <td>
                                08/19/2015

                                    to
                                    08/21/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>Los Angeles, CA</td>
                            <td>
                                Lodging for three nights

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                10</td>
                            <td>
                                09/24/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>Chicago, IL</td>
                            <td>
                                Ground Transportation

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                11</td>
                            <td>
                                10/12/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>Philadelphia, PA</td>
                            <td>
                                Ground Transportation

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                12</td>
                            <td>
                                10/13/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>Philadelphia, PA</td>
                            <td>
                                Ground Transportation

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                13</td>
                            <td>
                                10/13/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>Boston, MA</td>
                            <td>
                                Ground Transportation

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                14</td>
                            <td>
                                10/15/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>Boston, MA</td>
                            <td>
                                Ground Transportation

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                15</td>
                            <td>
                                10/15/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>Chicago, IL</td>
                            <td>
                                Ground Transportation

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                16</td>
                            <td>
                                10/16/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>Chicago, IL</td>
                            <td>
                                Ground Transportation

                            </td>
                            <td>
                                Simon &amp; Schuster
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                17</td>
                            <td>
                                11/09/2015

                            </td>
                            <td>

                                    Self


                            </td>
                            <td>Outside activity
                                </td>
                            <td>New York, NY</td>
                            <td>
                                Ground Transportation and Lodging

                            </td>
                            <td>
                                CBS
                                <div class="muted">New York, NY</div>
                            </td>
                            <td>Part of Senator's book tour for Plenty Ladylike</td>
                        </tr>

                    </tbody>
                </table>
            </div>

    </section>
"""
