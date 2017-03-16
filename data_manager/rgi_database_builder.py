import argparse
import datetime
import json
import os
import shutil
import sys
import tarfile
import urllib2
import zipfile
from import_data import run, _main

parser = argparse.ArgumentParser(description='Create data manager json.')
parser.add_argument('--url', dest='url', action='store', help='Url for CARD data')
parser.add_argument('--out', dest='output', action='store', help='JSON filename')
parser.add_argument('--name', dest='name', action='store', default='CARD_data-'+str(datetime.datetime.now().strftime("%Y-%B-%d-%H:%M:%S")), help='Data table database name')
args = parser.parse_args()

print "[rgi_database_builder] Importing..."

#version = _main(args)
_main(args)

def main(args):
    print "[rgi_database_builder] Building......"

    data_manager_entry = {}
    data_manager_entry['value'] = args.name.lower()
    #data_manager_entry['name'] = str(args.name) + " | CARD data version: " + str(version)
    data_manager_entry['name'] = args.name
    data_manager_entry['path'] = '.'

    data_manager_json = dict(data_tables=dict(rgi_databases=data_manager_entry))

    params = json.loads(open(args.output).read())

    target_directory = params['output_data'][0]['extra_files_path']
    os.mkdir(target_directory)
    output_path = os.path.join(os.getcwd(), 'rgi-database')

    for filename in os.listdir(output_path):
        print "[rgi_database_builder] move file: ", filename, " from ",output_path," to ", target_directory
        shutil.move(os.path.join(output_path, filename), target_directory)
    print "[rgi_database_builder] write file: ", args.output
    file(args.output, 'w').write(json.dumps(data_manager_json))

if __name__ == '__main__':
    main(args)
