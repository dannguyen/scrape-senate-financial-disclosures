"""
fdr is short for Financial Disclosure Report
"""

from lxml import etree
from pathlib import Path

from efdsenate.helpers import hparse, cleantext


if __name__ == '__main__':

    SRC_FNAME = Path('archive', 'samples', 'webpages', '2015-annual-report-corker.html')

    html = SRC_FNAME.read_text()
    doc = hparse(html)

    ### extract sections
    sections = doc.cssselect('#content section.card')


    for i, s in enumerate(sections):
        print('\n\n\n\n')
        print('#########################')
        print('### ', i+1)
        print('#########################\n\n')

        b = etree.tostring(s, pretty_print=True)
        print('"""')
        print(b.decode('utf8'))
        print('"""')























#########################
###  1
#########################


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

def parse_section_01(sec):
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


#########################
###  2
#########################


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
def parse_section_02(sec):
    pass





#########################
###  3
#########################


"""
<section class="card mb-2">
        <div class="card-body">
            <h3 class="h4">Part 3. Assets

            </h3>
            <p>
                Did you, your spouse, or dependent child own any asset worth more than $1000, have a deposit account with a balance over $5,000, or receive income of more than $200 from an asset?
                <strong>

                        Yes

                </strong>
            </p>
        </div>

            <div class="table-responsive">
                <table id="grid_items" class="table dataTable">
                    <caption class="sr-only">List of assets added to this report</caption>
                    <thead>
                    <tr class="header">
                        <th scope="col"/>
                        <th scope="col">Asset</th>
                        <th scope="col">Asset Type</th>
                        <th scope="col">Owner</th>
                        <th scope="col">Value</th>
                        <th scope="col">Income Type</th>
                        <th scope="col">Income</th>
                    </tr>
                    </thead>
                    <tbody>

                        <tr class="nowrap">
                            <td>1</td>
                            <td class="span4"><strong class="marginit-right">Corker Development Corporation</strong><div class="addUnderlyingAssets noWrap"/><div class="muted"><em>Company:</em> Corker Development Corporation (Chattanooga, TN)&#160;<em>Description:</em>&#160;Partnership interest in Limited Partnerships&#160;</div></td>
                            <td>Business Entity<div class="muted">General Partnership</div></td>
                            <td>Self</td>
                            <td>$500,001 - $1,000,000</td>
                            <td/>
                            <td/>
                        </tr>

                        <tr class="nowrap">
                            <td>1.1</td>
                            <td class="span4"><strong>Raymond James - Wealth Preservation Advisors</strong><div class="muted noWrap">(Chattanooga, TN)</div><div class="muted"><div class="muted"><em>Type: </em>Brokerage Sweep Account, </div></div></td>
                            <td>Bank Deposit</td>
                            <td>Self</td>
                            <td>$1,001 - $15,000</td>
                            <td>Interest, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>2</td>
                            <td class="span4"><strong class="marginit-right">Corker Properties X, L.P.</strong><div class="addUnderlyingAssets noWrap"/><div class="muted"><em>Company:</em> Corker Properties X, L.P. (Chattanooga, TN)&#160;<em>Description:</em>&#160;Rental Real Estate&#160;</div></td>
                            <td>Business Entity<div class="muted">Limited Partnership (LP)</div></td>
                            <td>Self</td>
                            <td/>
                            <td/>
                            <td/>
                        </tr>

                        <tr class="nowrap">
                            <td>2.1</td>
                            <td class="span4"><strong class="marginit-right">The Volunteer Buidling</strong><div class="muted"><em>Description:</em> 832 Georgia Avenue (Chattanooga, TN)&#160;<em>Filer comment:  </em>This property's value includes the commercial building, side lots, parking garage, and rear parking lot.</div></td>
                            <td>Real Estate<div class="muted">Commercial</div></td>
                            <td>Self</td>
                            <td>$5,000,001 - $25,000,000</td>
                            <td>Rent/Royalties, </td>
                            <td>$1,000,001 - $5,000,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>2.2</td>
                            <td class="span4"><strong>Raymond James - Wealth Preservation Advisors</strong><div class="muted noWrap">(Chattanooga, TN)</div><div class="muted"><div class="muted"><em>Type: </em>Checking, </div></div></td>
                            <td>Bank Deposit</td>
                            <td>Self</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>Interest, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>2.3</td>
                            <td class="span4"><strong class="marginit-right">Goodhew, LLC</strong><div class="muted"><em>Description</em>: Business Entity - Apparel Manufacture (socks)&#160;(Chattanooga, TN)&#160;</div></td>
                            <td>Other Securities</td>
                            <td>Self</td>
                            <td>$100,001 - $250,000</td>
                            <td>Other, (Business Income (K-1))</td>
                            <td>$50,001 - $100,000<br/>Other $51,725.00</td>
                        </tr>

                        <tr class="nowrap">
                            <td>2.4</td>
                            <td class="span4"><strong class="marginit-right">Sweetgreen - Preferred Stock</strong><div class="muted"><em>Description</em>: Sweetgreen - Fast Casual Restaurant Franchise&#160;(Washington, D.C.)&#160;</div></td>
                            <td>Other Securities</td>
                            <td>Self</td>
                            <td>$50,001 - $100,000</td>
                            <td>Dividends, Capital Gains, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>3</td>
                            <td class="span4"><strong class="marginit-right">Cumberland Trust and Investment Company</strong><div class="muted"><em>Description</em>: Trust Services&#160;(Nashville, TN)&#160;</div></td>
                            <td>Other Securities</td>
                            <td>Self</td>
                            <td>$15,001 - $50,000</td>
                            <td>Dividends, </td>
                            <td>$2,501 - $5,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>4</td>
                            <td class="span4"><strong class="marginit-right">Land</strong><div class="muted"><em>Description:</em> Dorothy Burchfield Butler Family Limited Partnership (Sevieville, TN)&#160;</div></td>
                            <td>Real Estate<div class="muted">Unimproved Land</div></td>
                            <td>Spouse</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>Rent/Royalties, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>5</td>
                            <td class="span4"><strong class="marginit-right">Land</strong><div class="muted"><em>Description:</em> Dorothy Burchfield Butler Management Company (Sevierville, TN)&#160;</div></td>
                            <td>Real Estate<div class="muted">Unimproved Land</div></td>
                            <td>Spouse</td>
                            <td>$1,001 - $15,000</td>
                            <td>Rent/Royalties, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>6</td>
                            <td class="span4"><strong class="marginit-right">Dorothy Burchfield Butler Estate</strong><div class="addUnderlyingAssets noWrap"/><div class="muted"><em>Description</em>: Estate of Dorothy Burchfield&#160;(Chattanooga, TN)&#160;</div></td>
                            <td>Other Securities</td>
                            <td>Spouse</td>
                            <td/>
                            <td/>
                            <td/>
                        </tr>

                        <tr class="nowrap">
                            <td>6.1</td>
                            <td class="span4"><strong>Tennessee State Bank</strong><div class="muted noWrap">(Sevierville, TN)</div><div class="muted"><div class="muted"><em>Type: </em>Checking, </div></div></td>
                            <td>Bank Deposit</td>
                            <td>Spouse</td>
                            <td>$100,001 - $250,000</td>
                            <td>Interest, </td>
                            <td>$201 - $1,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>7</td>
                            <td class="span4"><strong class="marginit-right">Whole Life Insurance</strong><div class="muted"><em>Provider:</em> Northwestern Mutual&#160;</div></td>
                            <td>Life Insurance<div class="muted">Whole</div></td>
                            <td>Self</td>
                            <td>$50,001 - $100,000</td>
                            <td>Dividends, </td>
                            <td>$2,501 - $5,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>8</td>
                            <td class="span4"><strong class="marginit-right">City of Chattanooga, TN Pension Plan</strong><div class="muted"/></td>
                            <td>Retirement Plans<div class="muted">Defined Benefit Pension Plan</div></td>
                            <td>Self</td>
                            <td>$100,001 - $250,000</td>
                            <td>Dividends, </td>
                            <td>$15,001 - $50,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9</td>
                            <td class="span4"><strong class="marginit-right">Raymond James - Wealth Preservation Adviosrs</strong><div class="addUnderlyingAssets noWrap"/><div class="muted"/></td>
                            <td>Brokerage/Managed Account</td>
                            <td>Self</td>
                            <td/>
                            <td/>
                            <td/>
                        </tr>

                        <tr class="nowrap">
                            <td>9.1</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=OHYFX" target="_blank">OHYFX</a> - JPMorgan High Yield Select (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$5,001 - $15,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.2</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=OOSYX" target="_blank">OOSYX</a> - Oppenheimer Senior Floating Rate Y (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$2,501 - $5,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.3</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=THOPX" target="_blank">THOPX</a> - Thompson Bond (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$5,001 - $15,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.4</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=IWO" target="_blank">IWO</a> - iShares Russell 2000 Growth (NYSEArca)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Exchange Traded Fund/Note</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$201 - $1,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.5</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=IJJ" target="_blank">IJJ</a> - iShares S&amp;P Mid-Cap 400 Value (NYSEArca)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Exchange Traded Fund/Note</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$1,001 - $2,500</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.6</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=IJS" target="_blank">IJS</a> - iShares S&amp;P Small-Cap 600 Value (NYSEArca)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Exchange Traded Fund/Note</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$201 - $1,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.7</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=SCHV" target="_blank">SCHV</a> - Schwab US Large-Cap Value ETF (NYSEArca)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Exchange Traded Fund/Note</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$2,501 - $5,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.8</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=XLE" target="_blank">XLE</a> - Energy Select Sector SPDR ETF (NYSEArca)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Exchange Traded Fund/Note</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$1,001 - $2,500</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.9</td>
                            <td class="span4"><strong class="marginit-right">Georgia State Housing and Financial Revenue - Cusip 373539S30</strong><div class="muted"><em>Rate/Coupon:</em> 3.55 <br/> <em>Matures:</em> 12/01/2025</div><div class="muted"/></td>
                            <td>Government Securities<div class="muted">Municipal Security</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Interest, </td>
                            <td>$201 - $1,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.10</td>
                            <td class="span4"><strong class="marginit-right">Lee County Florida School Board - Cusip 523494MH2</strong><div class="muted"><em>Rate/Coupon:</em> 3.75 <br/> <em>Matures:</em> 08/01/2027</div><div class="muted"/></td>
                            <td>Government Securities<div class="muted">Municipal Security</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Interest, </td>
                            <td>$1,001 - $2,500</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.11</td>
                            <td class="span4"><strong class="marginit-right">Mississippi Development Bond - Cusip 60534TVQ5</strong><div class="muted"><em>Rate/Coupon:</em> 3.25 <br/> <em>Matures:</em> 10/01/2024</div><div class="muted"/></td>
                            <td>Government Securities<div class="muted">Municipal Security</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Interest, </td>
                            <td>$201 - $1,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.12</td>
                            <td class="span4"><strong class="marginit-right">Oyster Bay New York Public Impact - Cusip 692160KP8</strong><div class="muted"><em>Rate/Coupon:</em> 4 <br/> <em>Matures:</em> 03/01/2028</div><div class="muted"/></td>
                            <td>Government Securities<div class="muted">Municipal Security</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Interest, </td>
                            <td>$1,001 - $2,500</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.13</td>
                            <td class="span4"><strong class="marginit-right">Poughkeepsie Town New York Library Purpose - Cusip 738663Y72</strong><div class="muted"><em>Rate/Coupon:</em> 3 <br/> <em>Matures:</em> 12/15/19</div><div class="muted"/></td>
                            <td>Government Securities<div class="muted">Municipal Security</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Interest, </td>
                            <td>$201 - $1,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.14</td>
                            <td class="span4"><strong class="marginit-right">St. Landry Parish Louisiana Revenue Bonds - Cusip 791023AK0</strong><div class="muted"><em>Rate/Coupon:</em> 3 <br/> <em>Matures:</em> 03/01/2023</div><div class="muted"/></td>
                            <td>Government Securities<div class="muted">Municipal Security</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Interest, </td>
                            <td>$201 - $1,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.15</td>
                            <td class="span4"><strong class="marginit-right">CBL - CBL &amp; Associates Properties </strong><div class="muted"/></td>
                            <td>Corporate Securities<div class="muted">Stock</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$5,001 - $15,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.16</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=MASFX" target="_blank">MASFX</a> - Litman Gregory Masters Alt Strats Instl</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$2,501 - $5,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.17</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=IVW" target="_blank">IVW</a> - iShares S&amp;P 500 Growth</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Exchange Traded Fund/Note</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$1,001 - $2,500</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.18</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=LALDX" target="_blank">LALDX</a> - Lord Abbett Short Duration Income A</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$5,001 - $15,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.19</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=BSIIX" target="_blank">BSIIX</a> - BlackRock Strategic Income Opps Instl</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$2,501 - $5,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.20</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=BHYIX" target="_blank">BHYIX</a> - BlackRock High Yield Bond Instl</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$2,501 - $5,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.21</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=AMLP" target="_blank">AMLP</a> - Alerian MLP ETF</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Exchange Traded Fund/Note</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$5,001 - $15,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.22</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=MLPOX" target="_blank">MLPOX</a> - Oppenheimer SteelPath MLP Alpha Y</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$5,001 - $15,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.23</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=BNDX" target="_blank">BNDX</a> - Vanguard Total Intl Bd Idx ETF</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Exchange Traded Fund/Note</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$1,001 - $2,500</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.24</td>
                            <td class="span4"><strong>Raymond James - Wealth Preservation Advisors</strong><div class="muted noWrap">(Chattanooga, TN)</div><div class="muted"><div class="muted"><em>Type: </em>Brokerage Sweep Account, </div></div></td>
                            <td>Bank Deposit</td>
                            <td>Self</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>Interest, </td>
                            <td>$1,001 - $2,500</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.25</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=WLL" target="_blank">WLL</a> - Whiting Petroleum Corp.</strong><div class="muted"/></td>
                            <td>Corporate Securities<div class="muted">Stock</div></td>
                            <td>Self</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>None, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.26</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=OAS" target="_blank">OAS</a> - Oasis Petroleum Inc.</strong><div class="muted"/></td>
                            <td>Corporate Securities<div class="muted">Stock</div></td>
                            <td>Self</td>
                            <td>$500,001 - $1,000,000</td>
                            <td>None, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.27</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=QQQ" target="_blank">QQQ</a> - PowerShares QQQ ETF</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Exchange Traded Fund/Note</div></td>
                            <td>Self</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>Dividends, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.28</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=SPY" target="_blank">SPY</a> - SPDR S&amp;P 500 ETF</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Exchange Traded Fund/Note</div></td>
                            <td>Self</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>Dividends, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.29</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=DIA" target="_blank">DIA</a> - SPDR Dow Jones Industrial Average ETF</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Exchange Traded Fund/Note</div></td>
                            <td>Self</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>Dividends, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>9.30</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=IJK" target="_blank">IJK</a> - iShares S&amp;P Mid-Cap 400 Growth</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Exchange Traded Fund/Note</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$201 - $1,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>10</td>
                            <td class="span4"><strong class="marginit-right">Raymond James - Wealth Preservation Advisors</strong><div class="addUnderlyingAssets noWrap"/><div class="muted"/></td>
                            <td>Retirement Plans<div class="muted">IRA</div></td>
                            <td>Spouse</td>
                            <td/>
                            <td/>
                            <td/>
                        </tr>

                        <tr class="nowrap">
                            <td>10.1</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=ABRYX" target="_blank">ABRYX</a> - Invesco Balanced-Risk Allc Y (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Spouse</td>
                            <td>$1,001 - $15,000</td>
                            <td>Dividends, Capital Gains, </td>
                            <td>$201 - $1,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>10.2</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=BREFX" target="_blank">BREFX</a> - Baron Real Estate Retail (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Spouse</td>
                            <td>$1,001 - $15,000</td>
                            <td>Dividends, Capital Gains, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>10.3</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=CDOZX" target="_blank">CDOZX</a> - Columbia Dividend Opportunity Z (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Spouse</td>
                            <td>$1,001 - $15,000</td>
                            <td>Dividends, Capital Gains, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>10.4</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=OAKIX" target="_blank">OAKIX</a> - Oakmark International I (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Spouse</td>
                            <td>$1,001 - $15,000</td>
                            <td>Dividends, Capital Gains, </td>
                            <td>$201 - $1,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>10.5</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=HWIAX" target="_blank">HWIAX</a> - Hotchkis &amp; Wiley Capital Income A (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Spouse</td>
                            <td>$1,001 - $15,000</td>
                            <td>Dividends, Capital Gains, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>10.6</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=WHIAX" target="_blank">WHIAX</a> - Ivy High Income A (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Spouse</td>
                            <td>$1,001 - $15,000</td>
                            <td>Dividends, </td>
                            <td>$201 - $1,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>10.7</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=NEFFX" target="_blank">NEFFX</a> - American Funds New Economy F2 (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Spouse</td>
                            <td>$1,001 - $15,000</td>
                            <td>Dividends, Capital Gains, </td>
                            <td>$201 - $1,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>10.8</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=OOSYX" target="_blank">OOSYX</a> - Oppenheimer Senior Floating Rate Y (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Spouse</td>
                            <td>$1,001 - $15,000</td>
                            <td>Dividends, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>10.9</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=PMCPX" target="_blank">PMCPX</a> - Principal MidCap P (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Spouse</td>
                            <td>$1,001 - $15,000</td>
                            <td>Dividends, Capital Gains, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>10.10</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=HDPSX" target="_blank">HDPSX</a> - Hodges Small Cap Retail (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Spouse</td>
                            <td>$1,001 - $15,000</td>
                            <td>Capital Gains, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>10.11</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=PNRZX" target="_blank">PNRZX</a> - Prudential Jennison Natural Resources Z (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Spouse</td>
                            <td>$1,001 - $15,000</td>
                            <td>None, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>10.12</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=THOPX" target="_blank">THOPX</a> - Thompson Bond (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Spouse</td>
                            <td>$1,001 - $15,000</td>
                            <td>Dividends, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>10.13</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=QAI" target="_blank">QAI</a> - IQ Hedge Multi-Strategy Tracker ETF (NYSEArca)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Exchange Traded Fund/Note</div></td>
                            <td>Spouse</td>
                            <td>$1,001 - $15,000</td>
                            <td>Dividends, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>10.14</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=AQMNX" target="_blank">AQMNX</a> - AQR Managed Futures Strategy N (NASDAQ)</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Spouse</td>
                            <td>$1,001 - $15,000</td>
                            <td>Dividends, Capital Gains, </td>
                            <td>$201 - $1,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>10.15</td>
                            <td class="span4"><strong>Raymond James - Wealth Preservation Advisors</strong><div class="muted noWrap">(Chattanooga, TN)</div><div class="muted"><div class="muted"><em>Type: </em>Brokerage Sweep Account, </div></div></td>
                            <td>Bank Deposit</td>
                            <td>Spouse</td>
                            <td>None (or less than $1,001)</td>
                            <td>Interest, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>11</td>
                            <td class="span4"><strong class="marginit-right">Pensco IRA</strong><div class="addUnderlyingAssets noWrap"/><div class="muted"/></td>
                            <td>Retirement Plans<div class="muted">IRA</div></td>
                            <td>Self</td>
                            <td/>
                            <td/>
                            <td/>
                        </tr>

                        <tr class="nowrap">
                            <td>11.1</td>
                            <td class="span4"><strong>Pensco</strong><div class="muted noWrap">(Denver, CO)</div><div class="muted"><div class="muted"><em>Type: </em>Brokerage Sweep Account, </div></div></td>
                            <td>Bank Deposit</td>
                            <td>Self</td>
                            <td>$1,001 - $15,000</td>
                            <td>Interest, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>11.2</td>
                            <td class="span4"><strong class="marginit-right">Covenant Apartment Fund VIII, LP</strong><div class="muted"><em>Company:</em> Covenant Apartment Fund VIII, LP (Nashville, TN)&#160;<em>Description:</em>&#160;Commerical Real Estate/Apartment Development&#160;</div></td>
                            <td>Business Entity<div class="muted">Limited Partnership (LP)</div></td>
                            <td>Self</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>Excepted Investment Fund, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>12</td>
                            <td class="span4"><strong class="marginit-right">Minnesota Life - Variable Adjustable Life Insurance</strong><div class="addUnderlyingAssets noWrap"/><div class="muted"/></td>
                            <td>Life Insurance<div class="muted">Variable</div></td>
                            <td>Self</td>
                            <td/>
                            <td/>
                            <td/>
                        </tr>

                        <tr class="nowrap">
                            <td>12.1</td>
                            <td class="span4"><strong class="marginit-right">Ivy Growth Subaccount</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>$100,001 - $250,000</td>
                            <td>None, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>12.2</td>
                            <td class="span4"><strong class="marginit-right">SFT Advantage Index 500 - Subaccount</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>$50,001 - $100,000</td>
                            <td>None, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>12.3</td>
                            <td class="span4"><strong class="marginit-right">Ivy VIP International Core - Subaccount</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>$15,001 - $50,000</td>
                            <td>None, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>12.4</td>
                            <td class="span4"><strong class="marginit-right">SFT Ivy Small Growth</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>$15,001 - $50,000</td>
                            <td>None, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>12.5</td>
                            <td class="span4"><strong class="marginit-right">Ivy VIP Value</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>$50,001 - $100,000</td>
                            <td>None, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>13</td>
                            <td class="span4"><strong class="marginit-right">NLL Holdings, LLC</strong><div class="muted"><em>Company:</em> NLL, LLC (Dover, DE)&#160;<em>Description:</em>&#160;Commercial real estate projects&#160;</div></td>
                            <td>Business Entity<div class="muted">Limited Liability Company (LLC)</div></td>
                            <td>Self</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>Interest, </td>
                            <td>$100,001 - $1,000,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>14</td>
                            <td class="span4"><strong class="marginit-right">Third Floor Grantor Trust</strong><div class="addUnderlyingAssets noWrap"/><div class="muted"/></td>
                            <td>Trust<div class="muted">General Trust</div></td>
                            <td>Self</td>
                            <td/>
                            <td/>
                            <td/>
                        </tr>

                        <tr class="nowrap">
                            <td>14.1</td>
                            <td class="span4"><strong class="marginit-right">McGowin Park, LLC</strong><div class="addUnderlyingAssets noWrap"/><div class="muted"><em>Company:</em> McGowin Park, LLC (Chattanooga, TN)&#160;<em>Description:</em>&#160;Commercial Real Estate Project&#160;<em>Filer comment:  </em>Third Floor Grantor Trust is a 13.73% member of McGowin Park, LLC</div></td>
                            <td>Business Entity<div class="muted">Limited Liability Company (LLC)</div></td>
                            <td>Self</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td/>
                            <td/>
                        </tr>

                        <tr class="nowrap">
                            <td>14.1.1</td>
                            <td class="span4"><strong class="marginit-right">McGowin Park Shopping Center</strong><div class="muted"><em>Description:</em> Interstate 65 &amp; Highway 90 (Mobile, AL)&#160;</div></td>
                            <td>Real Estate<div class="muted">Commercial</div></td>
                            <td>Self</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>Rent/Royalties, </td>
                            <td>$100,001 - $1,000,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>14.2</td>
                            <td class="span4"><strong class="marginit-right">1150, LLC</strong><div class="addUnderlyingAssets noWrap"/><div class="muted"><em>Company:</em> 1150, LLC (Chattanooga, TN)&#160;<em>Description:</em>&#160;Commercial Real Estate&#160;</div></td>
                            <td>Business Entity<div class="muted">Limited Liability Company (LLC)</div></td>
                            <td>Self</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td/>
                            <td/>
                        </tr>

                        <tr class="nowrap">
                            <td>14.2.1</td>
                            <td class="span4"><strong class="marginit-right">1150 Hixson Pike, Chattanooga, TN 37402</strong><div class="muted"><em>Description:</em> Commercial Real Estate (Chattanooga, TN)&#160;</div></td>
                            <td>Real Estate<div class="muted">Commercial</div></td>
                            <td>Self</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>Rent/Royalties, </td>
                            <td>$100,001 - $1,000,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>14.2.2</td>
                            <td class="span4"><strong>CapitalMark Bank (now Pinnacle Bank)</strong><div class="muted noWrap">(Chattanooga, TN)</div><div class="muted"><div class="muted"><em>Type: </em>Checking, </div></div></td>
                            <td>Bank Deposit</td>
                            <td>Self</td>
                            <td>$50,001 - $100,000</td>
                            <td>Interest, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>14.3</td>
                            <td class="span4"><strong class="marginit-right">McGowin Park Incentive Manager, LLC</strong><div class="addUnderlyingAssets noWrap"/><div class="muted"><em>Company:</em> McGowin Park Incentive Manager, LLC (Chattanooga, TN)&#160;<em>Description:</em>&#160;Entity formed to become a member of McGowin Park Incentive, LLC&#160;<em>Filer comment:  </em>Third Floor Grantor Trust is a 13.73% member in McGowin Park Incentive Manager, LLC</div></td>
                            <td>Business Entity<div class="muted">Limited Liability Company (LLC)</div></td>
                            <td>Self</td>
                            <td/>
                            <td/>
                            <td/>
                        </tr>

                        <tr class="nowrap">
                            <td>14.3.1</td>
                            <td class="span4"><strong class="marginit-right">McGowin Park Incentive, LLC</strong><div class="addUnderlyingAssets noWrap"/><div class="muted"><em>Company:</em> McGowin Park Incentive, LLC (Chattanooga, TN)&#160;<em>Description:</em>&#160;Entity to hold specific assets that were transferred out of McGowin Park, LLC&#160;<em>Filer comment:  </em>McGowin Park Incentive Manager, LLC is a 92% owner in McGowin Park Incentive, LLC</div></td>
                            <td>Business Entity<div class="muted">Limited Liability Company (LLC)</div></td>
                            <td>Self</td>
                            <td/>
                            <td/>
                            <td/>
                        </tr>

                        <tr class="nowrap">
                            <td>14.3.1.1</td>
                            <td class="span4"><strong class="marginit-right">City of Mobile Limited Obligation Project Revenue Warrant</strong><div class="muted"><em>Description</em>: Project Revenue Warrant&#160;(Mobile, AL)&#160;</div></td>
                            <td>Other Securities</td>
                            <td>Self</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>Other, (Project Sales Tax Revenue)</td>
                            <td><br/>Other $40,349.31</td>
                        </tr>

                        <tr class="nowrap">
                            <td>14.3.1.2</td>
                            <td class="span4"><strong class="marginit-right">Mobile County Limited Obligation Project Revenue Warrant</strong><div class="muted"><em>Description</em>: Project Revenue Warrant&#160;(Mobile, AL)&#160;</div></td>
                            <td>Other Securities</td>
                            <td>Self</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>Other, (Project Sales Tax Revenue)</td>
                            <td><br/>Other $40,349.31</td>
                        </tr>

                        <tr class="nowrap">
                            <td>15</td>
                            <td class="span4"><strong class="marginit-right">Raymond James - Wealth Preservation Advisors Traditional IRA</strong><div class="addUnderlyingAssets noWrap"/><div class="muted"/></td>
                            <td>Retirement Plans<div class="muted">IRA</div></td>
                            <td>Self</td>
                            <td/>
                            <td/>
                            <td/>
                        </tr>

                        <tr class="nowrap">
                            <td>15.1</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=BREFX" target="_blank">BREFX</a> - Baron Real Estate Retail</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, Capital Gains, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>15.2</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=CDOZX" target="_blank">CDOZX</a> - Columbia Dividend Opportunity Z</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$2,501 - $5,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>15.3</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=OOSYX" target="_blank">OOSYX</a> - Oppenheimer Senior Floating Rate Y</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$2,501 - $5,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>15.4</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=BSIIX" target="_blank">BSIIX</a> - BlackRock Strategic Income Opps Instl</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$1,001 - $2,500</td>
                        </tr>

                        <tr class="nowrap">
                            <td>15.5</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=BHYIX" target="_blank">BHYIX</a> - BlackRock High Yield Bond Instl</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$2,501 - $5,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>15.6</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=AMLP" target="_blank">AMLP</a> - Alerian MLP ETF</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Exchange Traded Fund/Note</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$2,501 - $5,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>15.7</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=TGBAX" target="_blank">TGBAX</a> - Templeton Global Bond Adv</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$1,001 - $2,500</td>
                        </tr>

                        <tr class="nowrap">
                            <td>15.8</td>
                            <td class="span4"><strong class="marginit-right"><a href="http://finance.yahoo.com/q?s=MLPOX" target="_blank">MLPOX</a> - Oppenheimer SteelPath MLP Alpha Y</strong><div class="muted"/></td>
                            <td>Mutual Funds<div class="muted">Mutual Fund</div></td>
                            <td>Self</td>
                            <td>None (or less than $1,001)</td>
                            <td>Dividends, </td>
                            <td>$2,501 - $5,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>15.9</td>
                            <td class="span4"><strong>Raymond James - Wealth Preservation Advisors</strong><div class="muted noWrap">(Chattanooga, TN)</div><div class="muted"><div class="muted"><em>Type: </em>Brokerage Sweep Account, </div></div></td>
                            <td>Bank Deposit</td>
                            <td>Self</td>
                            <td>$1,000,001 - $5,000,000</td>
                            <td>Interest, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>16</td>
                            <td class="span4"><strong>Raymond James - Wealth Preservation Advisors</strong><div class="muted noWrap">(Chattanooga, TN)</div><div class="muted"><div class="muted"><em>Type: </em>Checking, </div></div></td>
                            <td>Bank Deposit</td>
                            <td>Self</td>
                            <td>$250,001 - $500,000</td>
                            <td>Interest, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                        <tr class="nowrap">
                            <td>17</td>
                            <td class="span4"><strong>Raymond James - Wealth Preservation Advisors</strong><div class="muted noWrap">(Chattanooga, TN)</div><div class="muted"><div class="muted"><em>Type: </em>Brokerage Sweep Account, </div></div></td>
                            <td>Bank Deposit</td>
                            <td>Self</td>
                            <td>$5,000,001 - $25,000,000</td>
                            <td>Interest, </td>
                            <td>$1,001 - $2,500</td>
                        </tr>

                        <tr class="nowrap">
                            <td>18</td>
                            <td class="span4"><strong class="marginit-right">Chestnut Development Partners II, LP</strong><div class="muted"><em>Company:</em> Chestnut Development Partners (Chattanooga, TN)&#160;<em>Description:</em>&#160;Commercial Real Estate Partnership&#160;</div></td>
                            <td>Business Entity<div class="muted">Limited Partnership (LP)</div></td>
                            <td>Self</td>
                            <td>$100,001 - $250,000</td>
                            <td>Excepted Investment Fund, </td>
                            <td>$201 - $1,000</td>
                        </tr>

                        <tr class="nowrap">
                            <td>19</td>
                            <td class="span4"><strong>Sun Trust Bank</strong><div class="muted noWrap">(Chattanooga, TN)</div><div class="muted"><div class="muted"><em>Type: </em>Checking, </div></div></td>
                            <td>Bank Deposit</td>
                            <td>Joint</td>
                            <td>$50,001 - $100,000</td>
                            <td>Interest, </td>
                            <td>None (or less than $201)</td>
                        </tr>

                    </tbody>
                </table>
            </div>

    </section>



"""

def parse_section_03(sec):
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

def parse_section_04(sec):
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

def parse_section_05(sec):
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

def parse_section_06(sec):
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
def parse_section_07(sec):
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

def parse_section_08(sec):
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
def parse_section_09(sec):
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
def parse_section_10(sec):
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

def parse_section_11(sec):
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
def parse_section_12(sec):
    pass



