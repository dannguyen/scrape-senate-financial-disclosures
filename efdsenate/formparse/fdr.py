"""
fdr is short for Financial Disclosure Report
"""

from lxml import etree
from pathlib import Path

from helpers import hparse, cleantext
from formparse.fdrform.sec01 import parsec_01
from formparse.fdrform.sec02 import parsec_02
from formparse.fdrform.sec03 import parsec_03
from formparse.fdrform.sec04a import parsec_04a
from formparse.fdrform.sec04b import parsec_04b
from formparse.fdrform.sec05 import parsec_05
from formparse.fdrform.sec06 import parsec_06
from formparse.fdrform.sec07 import parsec_07
from formparse.fdrform.sec08 import parsec_08
from formparse.fdrform.sec09 import parsec_09
from formparse.fdrform.sec10 import parsec_10


def isnt_required(sec):
    """
<div class="card-body">
            <h3 class="h4">Part 6. Travel

            </h3>
            <p>

                <strong>

                        Not required

                </strong>
            </p>
        </div>
    """

def is_section_amended(sec):
    """
    <h3 class="h4">Part 8. Positions

                    <small>
                        <i class="fa fa-asterisk" title="Amended section"></i> Amended
                    </small>

            </h3>
    """

def extract_sections(html):
    doc = hparse(html)
    return doc.cssselect('#content section.card')


def main():
    d = {}
    SRC_FNAME = Path('archive', 'samples', 'webpages', '2015-annual-report-corker.html')
    html = SRC_FNAME.read_text()
    sections = extract_sections(html)

    d['01'] = parsec_01(sections[0])
    d['02'] = parsec_02(sections[1])
    d['03'] = parsec_03(sections[2])
    d['04a'] = parsec_04a(sections[3])
    d['04b'] = parsec_04b(sections[4])
    d['05'] = parsec_05(sections[5])
    d['06'] = parsec_06(sections[6])
    d['07'] = parsec_07(sections[7])
    d['08'] = parsec_08(sections[8])
    d['09'] = parsec_09(sections[9])
    d['10'] = parsec_10(sections[10])

    return d


if __name__ == '__main__':
    print(main())




























def parsec_03(sec):
    pass







#########################
###  4
#########################


"""
<section class="card mb-2">
        <div class="card-body">
            <h3 class="h4">Part 4a. Periodic Transaction Report Summary

            </h3>
            <p>
                In this section, electronically filed periodic transaction report (PTR) transactions are displayed for you.  Have you filed any paper-based PTRs in this period?
                <strong>

                        No

                </strong>
            </p>
        </div>

            <div class="table-responsive">
                <table class="table table-striped">
                    <caption class="sr-only">List of transactions added to this report</caption>
                    <thead>
                    <tr class="header">
                        <th scope="col"/>
                        <th scope="col">#</th>
                        <th scope="col">Transaction Date</th>
                        <th scope="col">Owner</th>
                        <th scope="col">Ticker</th>
                        <th scope="col">Asset Name</th>
                        <th scope="col">Type</th>
                        <th scope="col">Amount</th>
                        <th scope="col">Comment</th>
                    </tr>
                    </thead>
                    <tbody>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>1</td>
                            <td>
                                07/15/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    MAC


                            </td>
                            <td>

                                    The Macerich Company (NYSE)


                            </td>
                            <td>Purchase</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>2</td>
                            <td>
                                08/12/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    MAC


                            </td>
                            <td>

                                    The Macerich Company (NYSE)


                            </td>
                            <td>Sale (Full)</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>3</td>
                            <td>
                                08/21/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    Poughkeepsie Town NY Build America - CUSIP 738663Y72


                                    <div class="muted">
                                        <em>Rate/Coupon:</em> 3<br/>
                                        <em>Matures:</em> 12/15/19
                                    </div>

                            </td>
                            <td>Sale (Full)</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>4</td>
                            <td>
                                08/21/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    St. Landry Parish LA Sales Tax Rev - CUSIP 791023AK0


                                    <div class="muted">
                                        <em>Rate/Coupon:</em> 3<br/>
                                        <em>Matures:</em> 03/01/2023
                                    </div>

                            </td>
                            <td>Sale (Full)</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>5</td>
                            <td>
                                08/21/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    Oyster Bay NY Pub IMPT Bonds - CUSIP 692160KP8


                                    <div class="muted">
                                        <em>Rate/Coupon:</em> 4<br/>
                                        <em>Matures:</em> 03/01/2028
                                    </div>

                            </td>
                            <td>Sale (Full)</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>6</td>
                            <td>
                                08/21/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    Mississippi Development Horn Lake - CUSIP 60534TVQ5


                                    <div class="muted">
                                        <em>Rate/Coupon:</em> 3.25<br/>
                                        <em>Matures:</em> 10/01/2024
                                    </div>

                            </td>
                            <td>Sale (Full)</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>7</td>
                            <td>
                                08/21/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    Lee County FL School Board - CUSIP 523494MH2


                                    <div class="muted">
                                        <em>Rate/Coupon:</em> 3.75<br/>
                                        <em>Matures:</em> 08/01/2027
                                    </div>

                            </td>
                            <td>Sale (Full)</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>8</td>
                            <td>
                                08/21/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    Georgia State Housing and Financial - CUSIP 373539S30


                                    <div class="muted">
                                        <em>Rate/Coupon:</em> 3.55<br/>
                                        <em>Matures:</em> 12/01/2025
                                    </div>

                            </td>
                            <td>Sale (Full)</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>9</td>
                            <td>
                                08/24/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    CBL


                            </td>
                            <td>

                                    CBL &amp; Associates Properties Inc. (NYSE)


                            </td>
                            <td>Purchase</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>10</td>
                            <td>
                                08/24/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    MAC


                            </td>
                            <td>

                                    The Macerich Company (NYSE)


                            </td>
                            <td>Purchase</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>11</td>
                            <td>
                                08/24/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    MAC


                            </td>
                            <td>

                                    The Macerich Company (NYSE)


                            </td>
                            <td>Purchase</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>12</td>
                            <td>
                                08/24/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    CHK


                            </td>
                            <td>

                                    Chesapeake Energy Corporation (NYSE)


                            </td>
                            <td>Purchase</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>13</td>
                            <td>
                                08/25/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    CHK


                            </td>
                            <td>

                                    Chesapeake Energy Corporation (NYSE)


                            </td>
                            <td>Sale (Full)</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>14</td>
                            <td>
                                09/03/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    MAC


                            </td>
                            <td>

                                    The Macerich Company (NYSE)


                            </td>
                            <td>Sale (Partial)</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>15</td>
                            <td>
                                09/16/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    MAC


                            </td>
                            <td>

                                    The Macerich Company (NYSE)


                            </td>
                            <td>Sale (Full)</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>16</td>
                            <td>
                                10/09/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    CBL &amp; Associates Properties Inc - CBL


                            </td>
                            <td>Sale (Full)</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>17</td>
                            <td>
                                11/12/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    Chesapeake Energy Corporation - CHK


                            </td>
                            <td>Purchase</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>18</td>
                            <td>
                                11/13/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    Macerich Company REIT - MAC


                            </td>
                            <td>Purchase</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>19</td>
                            <td>
                                12/17/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    CHK - Chesapeake Energy Corporation


                            </td>
                            <td>Sale (Full)</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>20</td>
                            <td>
                                12/17/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    MAC - Macerich Company


                            </td>
                            <td>Sale (Full)</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>21</td>
                            <td>
                                12/21/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    Chesapeake Energy Corp - CHK


                            </td>
                            <td>Purchase</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>22</td>
                            <td>
                                12/23/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    Chipotle Mexican Grill - CMG


                            </td>
                            <td>Purchase</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>23</td>
                            <td>
                                12/30/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    Chipotle Mexican Grill - CMG


                            </td>
                            <td>Sale (Full)</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>24</td>
                            <td>
                                12/31/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    Chesapeake Energy Corp - CHK


                            </td>
                            <td>Sale (Full)</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>25</td>
                            <td>
                                12/31/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    Oasis Pete Inc. - OAS


                            </td>
                            <td>Purchase</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>26</td>
                            <td>
                                12/31/2015
                            </td>
                            <td>Self</td>
                            <td>

                                    --


                            </td>
                            <td>

                                    Whiting Pete Corp. - WLL


                            </td>
                            <td>Purchase</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                    </tbody>
                </table>
            </div>

    </section>



"""

def parsec_04(sec):
    pass




#########################
###  5
#########################


"""
<section class="card mb-2">
        <div class="card-body">
            <h3 class="h4">Part 4b. Transactions

            </h3>
            <p>
                Did you, your spouse, or dependent child buy, sell, or exchange an asset that exceeded $1,000?
                <strong>

                        Yes

                </strong>
            </p>
        </div>

            <div class="table-responsive">
                <table class="table table-striped">
                    <caption class="sr-only">List of transactions added to this report</caption>
                    <thead>
                    <tr class="header">
                        <th scope="col"/>
                        <th scope="col">#</th>
                        <th scope="col">Owner</th>
                        <th scope="col">Ticker</th>
                        <th scope="col">Asset Name</th>
                        <th scope="col">Transaction Type</th>
                        <th scope="col">Transaction Date</th>
                        <th scope="col">Amount</th>
                        <th scope="col">Comment</th>
                    </tr>
                    </thead>
                    <tbody>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                1</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=SPY" target="_blank">SPY</a>



                            </td>
                            <td>

                                    SPDR S&amp;P 500 ETF

                            </td>
                            <td>Purchase</td>
                            <td>12/18/2015</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                2</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=QQQ" target="_blank">QQQ</a>



                            </td>
                            <td>

                                    PowerShares QQQ ETF

                            </td>
                            <td>Purchase</td>
                            <td>12/18/2015</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                3</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=DIA" target="_blank">DIA</a>



                            </td>
                            <td>

                                    SPDR Dow Jones Industrial Average ETF

                            </td>
                            <td>Purchase</td>
                            <td>12/18/2015</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                4</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=MASFX" target="_blank">MASFX</a>



                            </td>
                            <td>

                                    Litman Gregory Masters Alt Strats Instl

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                5</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=WMCNX" target="_blank">WMCNX</a>



                            </td>
                            <td>

                                    William Blair Macro Allocation N

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                6</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=DHLSX" target="_blank">DHLSX</a>



                            </td>
                            <td>

                                    Diamond Hill Long-Short I

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                7</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=CLLIX" target="_blank">CLLIX</a>



                            </td>
                            <td>

                                    Collins Alternative Solutions Instl

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                8</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=MLPOX" target="_blank">MLPOX</a>



                            </td>
                            <td>

                                    Oppenheimer SteelPath MLP Alpha Y

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                9</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=ABRYX" target="_blank">ABRYX</a>



                            </td>
                            <td>

                                    Invesco Balanced-Risk Allc Y

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                10</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=AEPFX" target="_blank">AEPFX</a>



                            </td>
                            <td>

                                    American Funds Europacific Growth F2

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                11</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=SCHV" target="_blank">SCHV</a>



                            </td>
                            <td>

                                    Schwab US Large-Cap Value ETF

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                12</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IVW" target="_blank">IVW</a>



                            </td>
                            <td>

                                    iShares S&amp;P 500 Growth

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                13</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJK" target="_blank">IJK</a>



                            </td>
                            <td>

                                    iShares S&amp;P Mid-Cap 400 Growth

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                14</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJJ" target="_blank">IJJ</a>



                            </td>
                            <td>

                                    iShares S&amp;P Mid-Cap 400 Value

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                15</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=EFA" target="_blank">EFA</a>



                            </td>
                            <td>

                                    iShares MSCI EAFE

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                16</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=JCRAX" target="_blank">JCRAX</a>



                            </td>
                            <td>

                                    ALPS|CorCmdty Mgmt CompleteCmdty Strat A

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                17</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=OAKIX" target="_blank">OAKIX</a>



                            </td>
                            <td>

                                    Oakmark International I

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                18</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJJ" target="_blank">IJJ</a>



                            </td>
                            <td>

                                    iShares S&amp;P Mid-Cap 400 Value

                            </td>
                            <td>Purchase</td>
                            <td>10/09/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                19</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJK" target="_blank">IJK</a>



                            </td>
                            <td>

                                    iShares S&amp;P Mid-Cap 400 Growth

                            </td>
                            <td>Purchase</td>
                            <td>10/09/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                20</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=SCHV" target="_blank">SCHV</a>



                            </td>
                            <td>

                                    Schwab US Large-Cap Value ETF

                            </td>
                            <td>Purchase</td>
                            <td>10/09/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                21</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IVW" target="_blank">IVW</a>



                            </td>
                            <td>

                                    iShares S&amp;P 500 Growth

                            </td>
                            <td>Purchase</td>
                            <td>10/09/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                22</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=JCRAX" target="_blank">JCRAX</a>



                            </td>
                            <td>

                                    ALPS|CorCmdty Mgmt CompleteCmdty Strat A

                            </td>
                            <td>Purchase</td>
                            <td>10/09/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                23</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=SCHV" target="_blank">SCHV</a>



                            </td>
                            <td>

                                    Schwab US Large-Cap Value ETF

                            </td>
                            <td>Purchase</td>
                            <td>09/16/2015</td>
                            <td>$15,001 - $50,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                24</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IVW" target="_blank">IVW</a>



                            </td>
                            <td>

                                    iShares S&amp;P 500 Growth

                            </td>
                            <td>Purchase</td>
                            <td>09/16/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                25</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=EFA" target="_blank">EFA</a>



                            </td>
                            <td>

                                    iShares MSCI EAFE

                            </td>
                            <td>Purchase</td>
                            <td>09/16/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                26</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=JCRAX" target="_blank">JCRAX</a>



                            </td>
                            <td>

                                    ALPS|CorCmdty Mgmt CompleteCmdty Strat A

                            </td>
                            <td>Purchase</td>
                            <td>09/16/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                27</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=QAI" target="_blank">QAI</a>



                            </td>
                            <td>

                                    IQ Hedge Multi-Strategy Tracker ETF

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/24/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                28</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJJ" target="_blank">IJJ</a>



                            </td>
                            <td>

                                    iShares S&amp;P Mid-Cap 400 Value

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/24/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                29</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=XLE" target="_blank">XLE</a>



                            </td>
                            <td>

                                    Energy Select Sector SPDR ETF

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/24/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                30</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=SCHV" target="_blank">SCHV</a>



                            </td>
                            <td>

                                    Schwab US Large-Cap Value ETF

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/24/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                31</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IVW" target="_blank">IVW</a>



                            </td>
                            <td>

                                    iShares S&amp;P 500 Growth

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/24/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                32</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=DBC" target="_blank">DBC</a>



                            </td>
                            <td>

                                    PowerShares DB Commodity Tracking ETF

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/24/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                33</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJK" target="_blank">IJK</a>



                            </td>
                            <td>

                                    iShares S&amp;P Mid-Cap 400 Growth

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/24/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                34</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=MLPN" target="_blank">MLPN</a>



                            </td>
                            <td>

                                    Credit Suisse X-Links CushgMLPInfrasETN

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/24/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                35</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=AMLP" target="_blank">AMLP</a>



                            </td>
                            <td>

                                    Alerian MLP ETF

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/24/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                36</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=EFA" target="_blank">EFA</a>



                            </td>
                            <td>

                                    iShares MSCI EAFE

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/24/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                37</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IAU" target="_blank">IAU</a>



                            </td>
                            <td>

                                    iShares Gold Trust

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/24/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                38</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=THOPX" target="_blank">THOPX</a>



                            </td>
                            <td>

                                    Thompson Bond

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/21/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                39</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=OOSYX" target="_blank">OOSYX</a>



                            </td>
                            <td>

                                    Oppenheimer Senior Floating Rate Y

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/21/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                40</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=LALDX" target="_blank">LALDX</a>



                            </td>
                            <td>

                                    Lord Abbett Short Duration Income A

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/21/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                41</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BNDX" target="_blank">BNDX</a>



                            </td>
                            <td>

                                    Vanguard Total Intl Bd Idx ETF

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/21/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                42</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=AQMNX" target="_blank">AQMNX</a>



                            </td>
                            <td>

                                    AQR Managed Futures Strategy N

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/21/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                43</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=VIPSX" target="_blank">VIPSX</a>



                            </td>
                            <td>

                                    Vanguard Inflation-Protected Secs Inv

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/21/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                44</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=OHYFX" target="_blank">OHYFX</a>



                            </td>
                            <td>

                                    JPMorgan High Yield Select

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/21/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                45</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BSIIX" target="_blank">BSIIX</a>



                            </td>
                            <td>

                                    BlackRock Strategic Income Opps Instl

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/21/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                46</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BHYIX" target="_blank">BHYIX</a>



                            </td>
                            <td>

                                    BlackRock High Yield Bond Instl

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/21/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                47</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BICPX" target="_blank">BICPX</a>



                            </td>
                            <td>

                                    BlackRock 20/80 Target Allocation Instl

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/21/2015</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                48</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=MLPN" target="_blank">MLPN</a>



                            </td>
                            <td>

                                    Credit Suisse X-Links CushgMLPInfrasETN

                            </td>
                            <td>Purchase</td>
                            <td>07/31/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                49</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=MLPN" target="_blank">MLPN</a>



                            </td>
                            <td>

                                    Credit Suisse X-Links CushgMLPInfrasETN

                            </td>
                            <td>Purchase</td>
                            <td>07/29/2015</td>
                            <td>$1,001 - $15,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                50</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=DHLSX" target="_blank">DHLSX</a>



                            </td>
                            <td>

                                    Diamond Hill Long-Short I

                            </td>
                            <td>Purchase</td>
                            <td>07/28/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                51</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=AEPFX" target="_blank">AEPFX</a>



                            </td>
                            <td>

                                    American Funds Europacific Growth F2

                            </td>
                            <td>Purchase</td>
                            <td>07/28/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                52</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=EFA" target="_blank">EFA</a>



                            </td>
                            <td>

                                    iShares MSCI EAFE

                            </td>
                            <td>Purchase</td>
                            <td>07/28/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                53</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJK" target="_blank">IJK</a>



                            </td>
                            <td>

                                    iShares S&amp;P Mid-Cap 400 Growth

                            </td>
                            <td>Purchase</td>
                            <td>07/28/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                54</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJJ" target="_blank">IJJ</a>



                            </td>
                            <td>

                                    iShares S&amp;P Mid-Cap 400 Value

                            </td>
                            <td>Purchase</td>
                            <td>07/28/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                55</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=SCHV" target="_blank">SCHV</a>



                            </td>
                            <td>

                                    Schwab US Large-Cap Value ETF

                            </td>
                            <td>Purchase</td>
                            <td>07/28/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                56</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IVW" target="_blank">IVW</a>



                            </td>
                            <td>

                                    iShares S&amp;P 500 Growth

                            </td>
                            <td>Purchase</td>
                            <td>07/28/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                57</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=VIPSX" target="_blank">VIPSX</a>



                            </td>
                            <td>

                                    Vanguard Inflation-Protected Secs Inv

                            </td>
                            <td>Purchase</td>
                            <td>07/28/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                58</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=OAKIX" target="_blank">OAKIX</a>



                            </td>
                            <td>

                                    Oakmark International I

                            </td>
                            <td>Purchase</td>
                            <td>07/28/2015</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                59</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=MASFX" target="_blank">MASFX</a>



                            </td>
                            <td>

                                    Litman Gregory Masters Alt Strats Instl

                            </td>
                            <td>Purchase</td>
                            <td>06/08/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                60</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BREFX" target="_blank">BREFX</a>



                            </td>
                            <td>

                                    Baron Real Estate Retail

                            </td>
                            <td>Sale (Full)</td>
                            <td>06/08/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                61</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=HIEMX" target="_blank">HIEMX</a>



                            </td>
                            <td>

                                    Virtus Emerging Markets Opportunities I

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                62</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=PMCPX" target="_blank">PMCPX</a>



                            </td>
                            <td>

                                    Principal MidCap P

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                63</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=NEFFX" target="_blank">NEFFX</a>



                            </td>
                            <td>

                                    American Funds New Economy F2

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                64</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=AEPFX" target="_blank">AEPFX</a>



                            </td>
                            <td>

                                    American Funds Europacific Growth F2

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                65</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=HWAIX" target="_blank">HWAIX</a>



                            </td>
                            <td>

                                    Hotchkis &amp; Wiley Value Opps Instl

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                66</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=SCHF" target="_blank">SCHF</a>



                            </td>
                            <td>

                                    Schwab International Equity ETF

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                67</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=SCHV" target="_blank">SCHV</a>



                            </td>
                            <td>

                                    Schwab US Large-Cap Value ETF

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                68</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=DXJ" target="_blank">DXJ</a>



                            </td>
                            <td>

                                    WisdomTree Japan Hedged Equity ETF

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                69</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=EFA" target="_blank">EFA</a>



                            </td>
                            <td>

                                    iShares MSCI EAFE

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                70</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IVW" target="_blank">IVW</a>



                            </td>
                            <td>

                                    iShares S&amp;P 500 Growth

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                71</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJS" target="_blank">IJS</a>



                            </td>
                            <td>

                                    iShares S&amp;P Small-Cap 600 Value

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                72</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJJ" target="_blank">IJJ</a>



                            </td>
                            <td>

                                    iShares S&amp;P Mid-Cap 400 Value

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                73</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJK" target="_blank">IJK</a>



                            </td>
                            <td>

                                    iShares S&amp;P Mid-Cap 400 Growth

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                74</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IWO" target="_blank">IWO</a>



                            </td>
                            <td>

                                    iShares Russell 2000 Growth

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                75</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=EEM" target="_blank">EEM</a>



                            </td>
                            <td>

                                    iShares MSCI Emerging Markets

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                76</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=HDPSX" target="_blank">HDPSX</a>



                            </td>
                            <td>

                                    Hodges Small Cap Retail

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                77</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=TIQIX" target="_blank">TIQIX</a>



                            </td>
                            <td>

                                    Touchstone Sustainability &amp; Imp Eq Y

                            </td>
                            <td>Sale (Full)</td>
                            <td>03/12/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                78</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IVW" target="_blank">IVW</a>



                            </td>
                            <td>

                                    iShares S&amp;P 500 Growth

                            </td>
                            <td>Purchase</td>
                            <td>03/12/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                79</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=ABRYX" target="_blank">ABRYX</a>



                            </td>
                            <td>

                                    Invesco Balanced-Risk Allc Y

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                80</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BICPX" target="_blank">BICPX</a>



                            </td>
                            <td>

                                    BlackRock 20/80 Target Allocation Instl

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                81</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=LALDX" target="_blank">LALDX</a>



                            </td>
                            <td>

                                    Lord Abbett Short Duration Income A

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                82</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=AEPFX" target="_blank">AEPFX</a>



                            </td>
                            <td>

                                    American Funds Europacific Growth F2

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                83</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=DHLSX" target="_blank">DHLSX</a>



                            </td>
                            <td>

                                    Diamond Hill Long-Short I

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                84</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=WMCNX" target="_blank">WMCNX</a>



                            </td>
                            <td>

                                    William Blair Macro Allocation N

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                85</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=CLLIX" target="_blank">CLLIX</a>



                            </td>
                            <td>

                                    Collins Alternative Solutions Instl

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                86</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=MLPOX" target="_blank">MLPOX</a>



                            </td>
                            <td>

                                    Oppenheimer SteelPath MLP Alpha Y

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                87</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=QAI" target="_blank">QAI</a>



                            </td>
                            <td>

                                    IQ Hedge Multi-Strategy Tracker ETF

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                88</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=AMLP" target="_blank">AMLP</a>



                            </td>
                            <td>

                                    Alerian MLP ETF

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                89</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=DBC" target="_blank">DBC</a>



                            </td>
                            <td>

                                    PowerShares DB Commodity Tracking ETF

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                90</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=SCHF" target="_blank">SCHF</a>



                            </td>
                            <td>

                                    Schwab International Equity ETF

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                91</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=EFA" target="_blank">EFA</a>



                            </td>
                            <td>

                                    iShares MSCI EAFE

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                92</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJS" target="_blank">IJS</a>



                            </td>
                            <td>

                                    iShares S&amp;P Small-Cap 600 Value

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$15,001 - $50,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                93</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IWO" target="_blank">IWO</a>



                            </td>
                            <td>

                                    iShares Russell 2000 Growth

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$15,001 - $50,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                94</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJJ" target="_blank">IJJ</a>



                            </td>
                            <td>

                                    iShares S&amp;P Mid-Cap 400 Value

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                95</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJK" target="_blank">IJK</a>



                            </td>
                            <td>

                                    iShares S&amp;P Mid-Cap 400 Growth

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                96</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=AQMNX" target="_blank">AQMNX</a>



                            </td>
                            <td>

                                    AQR Managed Futures Strategy N

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                97</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=JCRAX" target="_blank">JCRAX</a>



                            </td>
                            <td>

                                    ALPS|CorCmdty Mgmt CompleteCmdty Strat A

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                98</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=MLPOX" target="_blank">MLPOX</a>



                            </td>
                            <td>

                                    Oppenheimer SteelPath MLP Alpha Y

                            </td>
                            <td>Purchase</td>
                            <td>01/28/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                99</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=OOSYX" target="_blank">OOSYX</a>



                            </td>
                            <td>

                                    Oppenheimer Senior Floating Rate Y

                            </td>
                            <td>Purchase</td>
                            <td>01/28/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                100</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=LALDX" target="_blank">LALDX</a>



                            </td>
                            <td>

                                    Lord Abbett Short Duration Income A

                            </td>
                            <td>Purchase</td>
                            <td>01/28/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                101</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=THOPX" target="_blank">THOPX</a>



                            </td>
                            <td>

                                    Thompson Bond

                            </td>
                            <td>Purchase</td>
                            <td>01/28/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                102</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=AMLP" target="_blank">AMLP</a>



                            </td>
                            <td>

                                    Alerian MLP ETF

                            </td>
                            <td>Purchase</td>
                            <td>01/28/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                103</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BNDX" target="_blank">BNDX</a>



                            </td>
                            <td>

                                    Vanguard Total Intl Bd Idx ETF

                            </td>
                            <td>Purchase</td>
                            <td>01/28/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                104</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BSIIX" target="_blank">BSIIX</a>



                            </td>
                            <td>

                                    BlackRock Strategic Income Opps Instl

                            </td>
                            <td>Purchase</td>
                            <td>01/28/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                105</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=ABRYX" target="_blank">ABRYX</a>



                            </td>
                            <td>

                                    Invesco Balanced-Risk Allc Y

                            </td>
                            <td>Purchase</td>
                            <td>01/26/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                106</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BICPX" target="_blank">BICPX</a>



                            </td>
                            <td>

                                    BlackRock 20/80 Target Allocation Instl

                            </td>
                            <td>Purchase</td>
                            <td>01/26/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                107</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=AEPFX" target="_blank">AEPFX</a>



                            </td>
                            <td>

                                    American Funds Europacific Growth F2

                            </td>
                            <td>Purchase</td>
                            <td>01/26/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                108</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=NEFFX" target="_blank">NEFFX</a>



                            </td>
                            <td>

                                    American Funds New Economy F2

                            </td>
                            <td>Purchase</td>
                            <td>01/26/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                109</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=WMCNX" target="_blank">WMCNX</a>



                            </td>
                            <td>

                                    William Blair Macro Allocation N

                            </td>
                            <td>Purchase</td>
                            <td>01/26/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                110</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=CLLIX" target="_blank">CLLIX</a>



                            </td>
                            <td>

                                    Collins Alternative Solutions Instl

                            </td>
                            <td>Purchase</td>
                            <td>01/26/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                111</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=QAI" target="_blank">QAI</a>



                            </td>
                            <td>

                                    IQ Hedge Multi-Strategy Tracker ETF

                            </td>
                            <td>Purchase</td>
                            <td>01/26/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                112</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=DBC" target="_blank">DBC</a>



                            </td>
                            <td>

                                    PowerShares DB Commodity Tracking ETF

                            </td>
                            <td>Purchase</td>
                            <td>01/26/2015</td>
                            <td>$15,001 - $50,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                113</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=EFA" target="_blank">EFA</a>



                            </td>
                            <td>

                                    iShares MSCI EAFE

                            </td>
                            <td>Purchase</td>
                            <td>01/26/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                114</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJJ" target="_blank">IJJ</a>



                            </td>
                            <td>

                                    iShares S&amp;P Mid-Cap 400 Value

                            </td>
                            <td>Purchase</td>
                            <td>01/26/2015</td>
                            <td>$1,001 - $15,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                115</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=IJK" target="_blank">IJK</a>



                            </td>
                            <td>

                                    iShares S&amp;P Mid-Cap 400 Growth

                            </td>
                            <td>Purchase</td>
                            <td>01/26/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                116</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=SCHV" target="_blank">SCHV</a>



                            </td>
                            <td>

                                    Schwab US Large-Cap Value ETF

                            </td>
                            <td>Purchase</td>
                            <td>01/26/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                117</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BHYIX" target="_blank">BHYIX</a>



                            </td>
                            <td>

                                    BlackRock High Yield Bond Instl

                            </td>
                            <td>Purchase</td>
                            <td>01/26/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                118</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=DHLSX" target="_blank">DHLSX</a>



                            </td>
                            <td>

                                    Diamond Hill Long-Short I

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                119</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=MLPOX" target="_blank">MLPOX</a>



                            </td>
                            <td>

                                    Oppenheimer SteelPath MLP Alpha Y

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                120</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=NEFFX" target="_blank">NEFFX</a>



                            </td>
                            <td>

                                    American Funds New Economy F2

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                121</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=AEPFX" target="_blank">AEPFX</a>



                            </td>
                            <td>

                                    American Funds Europacific Growth F2

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                122</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=EFA" target="_blank">EFA</a>



                            </td>
                            <td>

                                    iShares MSCI EAFE

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                123</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=OAKIX" target="_blank">OAKIX</a>



                            </td>
                            <td>

                                    Oakmark International I

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                124</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=CDOZX" target="_blank">CDOZX</a>



                            </td>
                            <td>

                                    Columbia Dividend Opportunity Z

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                125</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BREFX" target="_blank">BREFX</a>



                            </td>
                            <td>

                                    Baron Real Estate Retail

                            </td>
                            <td>Sale (Full)</td>
                            <td>10/14/2015</td>
                            <td>$15,001 - $50,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                126</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=AMLP" target="_blank">AMLP</a>



                            </td>
                            <td>

                                    Alerian MLP ETF

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/24/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                127</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=MLPN" target="_blank">MLPN</a>



                            </td>
                            <td>

                                    Credit Suisse X-Links CushgMLPInfrasETN

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/24/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                128</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=TGBAX" target="_blank">TGBAX</a>



                            </td>
                            <td>

                                    Templeton Global Bond Adv

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/21/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                129</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=OOSYX" target="_blank">OOSYX</a>



                            </td>
                            <td>

                                    Oppenheimer Senior Floating Rate Y

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/21/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                130</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BHYIX" target="_blank">BHYIX</a>



                            </td>
                            <td>

                                    BlackRock High Yield Bond Instl

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/21/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                131</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BSIIX" target="_blank">BSIIX</a>



                            </td>
                            <td>

                                    BlackRock Strategic Income Opps Instl

                            </td>
                            <td>Sale (Full)</td>
                            <td>08/21/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                132</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BHYIX" target="_blank">BHYIX</a>



                            </td>
                            <td>

                                    BlackRock High Yield Bond Instl

                            </td>
                            <td>Sale (Partial)</td>
                            <td>08/20/2015</td>
                            <td>$15,001 - $50,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                133</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=TIQIX" target="_blank">TIQIX</a>



                            </td>
                            <td>

                                    Touchstone Sustainability &amp; Imp Eq Y

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                134</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=NEFFX" target="_blank">NEFFX</a>



                            </td>
                            <td>

                                    American Funds New Economy F2

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                135</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=HIEMX" target="_blank">HIEMX</a>



                            </td>
                            <td>

                                    Virtus Emerging Markets Opportunities I

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                136</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=CDOZX" target="_blank">CDOZX</a>



                            </td>
                            <td>

                                    Columbia Dividend Opportunity Z

                            </td>
                            <td>Sale (Full)</td>
                            <td>04/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                137</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=DHLSX" target="_blank">DHLSX</a>



                            </td>
                            <td>

                                    Diamond Hill Long-Short I

                            </td>
                            <td>Purchase</td>
                            <td>09/10/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                138</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=NEFFX" target="_blank">NEFFX</a>



                            </td>
                            <td>

                                    American Funds New Economy F2

                            </td>
                            <td>Purchase</td>
                            <td>09/10/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                139</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=AEPFX" target="_blank">AEPFX</a>



                            </td>
                            <td>

                                    American Funds Europacific Growth F2

                            </td>
                            <td>Purchase</td>
                            <td>09/10/2015</td>
                            <td>$15,001 - $50,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                140</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=EFA" target="_blank">EFA</a>



                            </td>
                            <td>

                                    iShares MSCI EAFE

                            </td>
                            <td>Purchase</td>
                            <td>09/10/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                141</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=CDOZX" target="_blank">CDOZX</a>



                            </td>
                            <td>

                                    Columbia Dividend Opportunity Z

                            </td>
                            <td>Purchase</td>
                            <td>09/10/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                142</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=OAKIX" target="_blank">OAKIX</a>



                            </td>
                            <td>

                                    Oakmark International I

                            </td>
                            <td>Purchase</td>
                            <td>09/10/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                143</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=MLPN" target="_blank">MLPN</a>



                            </td>
                            <td>

                                    Credit Suisse X-Links CushgMLPInfrasETN

                            </td>
                            <td>Purchase</td>
                            <td>07/30/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                144</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=AMLP" target="_blank">AMLP</a>



                            </td>
                            <td>

                                    Alerian MLP ETF

                            </td>
                            <td>Purchase</td>
                            <td>07/28/2015</td>
                            <td>$250,001 - $500,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                145</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=TGBAX" target="_blank">TGBAX</a>



                            </td>
                            <td>

                                    Templeton Global Bond Adv

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                146</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=OOSYX" target="_blank">OOSYX</a>



                            </td>
                            <td>

                                    Oppenheimer Senior Floating Rate Y

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                147</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=HIEMX" target="_blank">HIEMX</a>



                            </td>
                            <td>

                                    Virtus Emerging Markets Opportunities I

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                148</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=TIQIX" target="_blank">TIQIX</a>



                            </td>
                            <td>

                                    Touchstone Sustainability &amp; Imp Eq Y

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                149</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=NEFFX" target="_blank">NEFFX</a>



                            </td>
                            <td>

                                    American Funds New Economy F2

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                150</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BREFX" target="_blank">BREFX</a>



                            </td>
                            <td>

                                    Baron Real Estate Retail

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$50,001 - $100,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                151</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BSIIX" target="_blank">BSIIX</a>



                            </td>
                            <td>

                                    BlackRock Strategic Income Opps Instl

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                152</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=BHYIX" target="_blank">BHYIX</a>



                            </td>
                            <td>

                                    BlackRock High Yield Bond Instl

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                153</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=CDOZX" target="_blank">CDOZX</a>



                            </td>
                            <td>

                                    Columbia Dividend Opportunity Z

                            </td>
                            <td>Purchase</td>
                            <td>03/02/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                154</td>
                            <td>Self</td>
                            <td>

                                    <a href="https://finance.yahoo.com/q?s=MLPOX" target="_blank">MLPOX</a>



                            </td>
                            <td>

                                    Oppenheimer SteelPath MLP Alpha Y

                            </td>
                            <td>Purchase</td>
                            <td>07/28/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                155</td>
                            <td>Self</td>
                            <td>

                                    --



                            </td>
                            <td>

                                    Chestnut Development Partners II, LP

                            </td>
                            <td>Purchase</td>
                            <td>08/31/2015</td>
                            <td>$100,001 - $250,000</td>
                            <td>
                                --</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                156</td>
                            <td>Self</td>
                            <td>

                                    --



                            </td>
                            <td>

                                    Commercial Property: 1150 Hixson Pike, Chattanooga, TN 37405

                            </td>
                            <td>Purchase</td>
                            <td>01/07/2015</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>
                                This property was purchased and is owned by 1150,LLC which The Third Floor Grantor Trust is a member</td>
                        </tr>

                        <tr class="nowrap">
                            <td>
                            </td>
                            <td>
                                157</td>
                            <td>Self</td>
                            <td>

                                    --



                            </td>
                            <td>

                                    Covenant Apartment Fund VIII, LP

                            </td>
                            <td>Purchase</td>
                            <td>02/27/2015</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>
                                --</td>
                        </tr>

                    </tbody>
                </table>
            </div>

    </section>



"""

def parsec_05(sec):
    pass




#########################
###  6
#########################


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

def parsec_06(sec):
    pass






#########################
###  7
#########################


"""
<section class="card mb-2">
        <div class="card-body">
            <h3 class="h4">Part 6. Travel

            </h3>
            <p>
                Did you, your spouse, or dependent child receive any <button data-toggle="popover" type="button" aria-haspopup="true" data-html="true" data-title="When is travel reportable? &lt;button type='button' tabindex='0' id='jsPopoverClose' aria-label='close' class='close'&gt;&lt;i class='fa fa-times' aria-hidden='true'&gt;&lt;span class='sr-only'&gt;Close&lt;/span&gt;&lt;/i&gt;&lt;/button&gt;" data-template="&lt;div class=&quot;popover popover__fixMedium&quot; role=&quot;tooltip&quot;&gt;&lt;div class=&quot;arrow&quot;&gt;&lt;/div&gt;&lt;h3 class=&quot;popover-header&quot;&gt;&lt;/h3&gt;&lt;div class=&quot;popover-body&quot;&gt;&lt;/div&gt;&lt;/div&gt;" class="btn btn-link popover--textButton font-weight-bold" data-placement="auto" data-content="&lt;p&gt;If you are reimbursed for more than one trip from the same sponsor, and the trips added together are worth more than $350, then you must report each trip individually, even if the reimbursement for each separate trip does not equal more than $350.&lt;/p&gt;">reportable travel</button>?
                <strong>

                        No

                </strong>
            </p>
        </div>

    </section>



"""
def parsec_07(sec):
    pass





#########################
###  8
#########################


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
                        <th scope="col"/>
                        <th scope="col">#</th>
                        <th scope="col">Incurred</th>
                        <th scope="col">Debtor</th>
                        <th scope="col">Type</th>
                        <th scope="col">Points</th>
                        <th scope="col">Rate<br/>(Term)</th>
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
                                1.95%<br/>

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

def parsec_08(sec):
    pass




#########################
###  9
#########################


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
                        <th scope="col"/>
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
                            <td/>
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
                            <td/>
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
                            <td/>
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
                            <td/>
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
                            <td/>
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
                            <td/>
                        </tr>

                    </tbody>
                </table>
            </div>

    </section>



"""
def parsec_09(sec):
    pass





#########################
###  10
#########################


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
def parsec_10(sec):
    pass





#########################
###  11
#########################


"""
<section class="card mb-2">
        <div class="card-body">
            <h3 class="h4">Part 10. Compensation

            </h3>
            <p>
                <strong>If this is your first report, or you are a candidate</strong> did you receive compensation of more than $5,000 from a single source in the <strong>two</strong> prior years?
                <strong>

                        This is not my first report.

                </strong>
            </p>
        </div>

    </section>



"""

def parsec_11(sec):
    pass




#########################
###  12
#########################


"""
<section class="card mb-2">
        <div class="card-body">
            <h3 class="h4">
                Attachments &amp; Comments

            </h3>


                <h4 class="h5">Attachments</h4>
                <div class="table-responsive">
                    <table class="table table-striped">
                        <caption class="sr-only">List of supporting documents for this report.</caption>
                        <thead>
                        <tr class="header">
                            <th scope="col">Document Title</th>
                            <th scope="col">Date/Time Added</th>
                        </tr>
                        </thead>
                        <tbody>

                            <tr class="nowrap">
                                <td>
                                    <a href="https://electronic-financial-disclosure.s3.amazonaws.com/production/Corker-Robert-355/2015/a197a94a-27c2-45ec-aae8-177cc71b6d93/8e699c61-f46c-456c-9ded-1c6974f4653b.pdf?Expires=1561156310&amp;AWSAccessKeyId=AKIAIL7OIS64Y5R67EXA&amp;Signature=QFHR7WhYPIZstEy03QQ8hWxtsTA%3D" target="_blank">Corker 2015 Disclosure Cover Letter.pdf</a>
                                </td>
                                <td>08/05/2016 @ 8:53 AM</td>
                            </tr>

                            <tr class="nowrap">
                                <td>
                                    <a href="https://electronic-financial-disclosure.s3.amazonaws.com/production/Corker-Robert-355/2015/a197a94a-27c2-45ec-aae8-177cc71b6d93/bfa23001-b1db-481c-8e2b-853abbf91b25.pdf?Expires=1561156310&amp;AWSAccessKeyId=AKIAIL7OIS64Y5R67EXA&amp;Signature=CUOyU9DecuyrhaSOD8oUrg%2BeQtA%3D" target="_blank">Corker 2015 Ethics EIF Letters.pdf</a>
                                </td>
                                <td>08/04/2016 @ 8:17 AM</td>
                            </tr>

                        </tbody>
                    </table>
                </div>



                <br/>
                <em class="text-muted">No comments added.</em>

        </div>
    </section>
"""
def parsec_12(sec):
    pass



