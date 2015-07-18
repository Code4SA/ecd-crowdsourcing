import csv
import re
field_names = 'id,source_url,status,category,fax,name,postal_address,phone,reg_no,physical_address,legal_form,reg_date,contact_name,email,reg_status_cell,reg_no_cell,category1,category3,category2'.split(',')

def gen_re():
    places = [el.strip() for el in open('zululand_places.txt')]
    piped = "|".join(places)
    return re.compile(piped)
    

def parse_address(x):
    if re_place.search(x):
        return x
    return None

re_place = gen_re()
reader = csv.DictReader(open('ecd_npo.csv'))
with open('output_npo.csv', 'w') as fp:
    writer = csv.DictWriter(fp, field_names)
    for datum in reader:
        address = datum['physical_address']
        result = parse_address(address)
        if result:
            writer.writerow(datum)
