from helpers import cleantext, hparse, slugify


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

def table_records_default_parser(sec):
    records = []
    table = sec.find('*/table')
    if table is not None:
        headers = [slugify(e.text) for e in table.cssselect('.header')[0]]
        # [None, 'Asset', 'Asset Type', 'Owner', 'Value', 'Income Type', 'Income']
        headers[0] = 'id'
        for r in table.cssselect('tr')[1:]:
            records.append({ headers[i]: cleantext(r[i].text_content()) for i in range(len(r)) })
    return records


def parse_section_header(sec):
    h = {}
    h['title'] = cleantext(sec.cssselect('h3')[0].text)
    _p = sec.cssselect('p')[0]
    _r = list(_p)[0]
    h['prompt'] = cleantext(_p.text)
    h['response'] = cleantext(_r.text)
    return h

def parse_section(sec, table_parser=table_records_default_parser):
    data = parse_section_header(sec)
    data['records'] = table_parser(sec)
    return data
