import sys
import os

setup_script = open(os.path.join(os.path.dirname(__file__), 'setup.py'))
exec(setup_script.read())

import datetime
import config
import extractor


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    start_time = datetime.datetime.now()
    print('Extracting known positive and known negative records starting at {}'.format(start_time))
    
    input_data_files = config.input_data_files
    if len(args) > 0:
        print('Extracting for {}'.format(args[0]))
        input_data_files = [s for s in config.input_data_files if args[0] in s]
        print(input_data_files)
    extractor.extract_records(input_data_files, config.output_dir, config.max_records_to_extract)

    end_time = datetime.datetime.now()
    print('Extraction completed at {}. Total duration: {}.'.format(end_time, end_time - start_time))

if __name__ == "__main__":
    main()