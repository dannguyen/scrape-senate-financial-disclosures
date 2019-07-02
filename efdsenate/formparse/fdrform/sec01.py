#########################
###  1
#########################
from helpers import cleantext


def parsec_01(sec):
    """
    Part 1. Honoraria Payments or Payments to Charity in Lieu of Honoraria
    """

    d = {}
    p = sec.cssselect('p')[0]
    r = list(p)[0]

    """
    Did any individual or organization pay you or your spouse more than $200 or
    donate any amount to a charity on your behalf, for an article, speech,
    or appearance?
    """
    d['prompt'] = cleantext(p.text)
    d['response'] = cleantext(r.text)
    return d








"""
<section class="card mb-2">
        <div class="card-body">
            <h3 class="h4">
                Part 1. Honoraria Payments or Payments to Charity in Lieu of Honoraria

            </h3>
            <p>
                Did any individual or organization pay you or your spouse more than $200 or donate any amount to a charity on your behalf, for an article, speech, or appearance?
                <strong>

                        No

                </strong>
            </p>
        </div>

    </section>

"""

##########################################################
# Example of Yes (Corker 2015)


##########################################################
# Example of Yes (Romney 2018)

# <section class="card mb-2">
#         <div class="card-body">
#             <h3 class="h4">
#                 Part 1. Honoraria Payments or Payments to Charity in Lieu of Honoraria

#             </h3>
#             <p>
#                 Did any individual or organization pay you or your spouse more than $200 or donate any amount to a charity on your behalf, for an article, speech, or appearance?
#                 <strong>

#                         Yes

#                 </strong>
#             </p>
#         </div>

#             <div class="table-responsive">
#                 <table class="table table-striped">
#                     <caption class="sr-only">List of honoraria added to this report</caption>
#                     <thead>
#                     <tr class="header">
#                         <th scope="col"></th>
#                         <th scope="col">#</th>
#                         <th scope="col">Date</th>
#                         <th scope="col">Activity</th>
#                         <th scope="col">Amount</th>
#                         <th scope="col">Who Paid?</th>
#                         <th scope="col">Who received payment?</th>
#                     </tr>
#                     </thead>
#                     <tbody>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 1</td>
#                             <td>
#                                 02/01/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$99,500.00</td>
#                             <td>
#                                 Deutsche Bank
#                                 <div class="muted">New York, NY</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 2</td>
#                             <td>
#                                 03/02/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$15,000.00</td>
#                             <td>
#                                 American Apparel and Footwear Association
#                                 <div class="muted">Washington, DC</div>
#                             </td>
#                             <td>A Charity</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 3</td>
#                             <td>
#                                 03/02/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$15,000.00</td>
#                             <td>
#                                 New Balance
#                                 <div class="muted">Boston, MA</div>
#                             </td>
#                             <td>A Charity</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 4</td>
#                             <td>
#                                 04/05/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$100,000.00</td>
#                             <td>
#                                 McKinsey &amp; Company
#                                 <div class="muted">New York, NY</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 5</td>
#                             <td>
#                                 04/05/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$100,000.00</td>
#                             <td>
#                                 TD Ameritrade
#                                 <div class="muted">Omaha, NE</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 6</td>
#                             <td>
#                                 04/05/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$98,792.00</td>
#                             <td>
#                                 US Chamber Institute for Legal Reform
#                                 <div class="muted">Washington, DC</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 7</td>
#                             <td>
#                                 06/21/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$20,000.00</td>
#                             <td>
#                                 Biotechnology Innovation Organization
#                                 <div class="muted">Washington, DC</div>
#                             </td>
#                             <td>Spouse</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 8</td>
#                             <td>
#                                 08/18/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$60,000.00</td>
#                             <td>
#                                 Academy Mortgage
#                                 <div class="muted">Draper, UT</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 9</td>
#                             <td>
#                                 08/18/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$40,000.00</td>
#                             <td>
#                                 Goldman Sachs
#                                 <div class="muted">New York, NY</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 10</td>
#                             <td>
#                                 08/18/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$100,000.00</td>
#                             <td>
#                                 National Multifamily Housing Council
#                                 <div class="muted">Washington, DC</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 11</td>
#                             <td>
#                                 08/18/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$100,000.00</td>
#                             <td>
#                                 NBCUniversal Media, LLC
#                                 <div class="muted">New York, NY</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 12</td>
#                             <td>
#                                 08/21/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$40,000.00</td>
#                             <td>
#                                 Goldman Sachs
#                                 <div class="muted">New York, NY</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 13</td>
#                             <td>
#                                 08/21/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$100,000.00</td>
#                             <td>
#                                 Blue Cross Blue Shield
#                                 <div class="muted">Chicago, IL</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 14</td>
#                             <td>
#                                 08/21/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$100,000.00</td>
#                             <td>
#                                 Itau BBA
#                                 <div class="muted">Sao Paulo, Brasil</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 15</td>
#                             <td>
#                                 09/19/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$122,000.00</td>
#                             <td>
#                                 Deutsche Bank
#                                 <div class="muted">London, United Kingdom</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 16</td>
#                             <td>
#                                 10/19/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$84,000.00</td>
#                             <td>
#                                 Stream Realty Partners
#                                 <div class="muted">Houston, TX</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 17</td>
#                             <td>
#                                 11/14/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$97,000.00</td>
#                             <td>
#                                 Robarts Research Institute
#                                 <div class="muted">Ontario, Canada</div>
#                             </td>
#                             <td>A Charity</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 18</td>
#                             <td>
#                                 12/19/2017
#                             </td>
#                             <td>Speech</td>
#                             <td>$100,000.00</td>
#                             <td>
#                                 Centerview Partners
#                                 <div class="muted">New York, NY</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 19</td>
#                             <td>
#                                 01/22/2018
#                             </td>
#                             <td>Speech</td>
#                             <td>$40,260.31</td>
#                             <td>
#                                 Retail Industry Leaders Association
#                                 <div class="muted">Arlington, VA</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                         <tr class="nowrap">
#                             <td>
#                             </td>
#                             <td>
#                                 20</td>
#                             <td>
#                                 02/11/2018
#                             </td>
#                             <td>Speech</td>
#                             <td>$137,082.00</td>
#                             <td>
#                                 NBCUniversal Media, LLC
#                                 <div class="muted">New York, NY</div>
#                             </td>
#                             <td>Self</td>
#                         </tr>

#                     </tbody>
#                 </table>
#             </div>

#     </section>
