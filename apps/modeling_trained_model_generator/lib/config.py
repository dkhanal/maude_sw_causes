# Copyright (c) 2017 Deepak Khanal
# All Rights Reserved
# dkhanal AT gmail DOT com

import os
import json
import logging

def get_config_file_path(hint_path):
    if hint_path is None:
        hint_path = '../config.json'

    if not os.path.isabs(hint_path):
        file = os.path.join(os.path.dirname(__file__), hint_path)
        logging.info('Config file is {}...'.format(file))
    else:
        file = hint_path
    return file

def load_config():
    logging.info('Loading configuration...')
    with open(get_config_file_path('../config.json')) as config_file:
        config_data = json.load(config_file)

    # Configuration items
    global input_data_file_sets
    global input_dir
    global output_dir
    global models
    global upload_output_to_remote_server
    global remote_server
    global custom_stop_words
    global duplicate_record_check_ignore_pattern
    global verbose

    input_data_file_sets = config_data['input_data_file_sets']
    input_dir = config_data['input_dir']
    output_dir = config_data['output_dir']
    models = config_data['models']
    upload_output_to_remote_server = config_data['upload_output_to_remote_server']
    custom_stop_words = config_data['custom_stop_words']
    
    remote_server = config_data['remote_server']
    duplicate_record_check_ignore_pattern = config_data['duplicate_record_check_ignore_pattern']

    verbose = config_data['verbose']

    logging.info('Configuration loaded.')

load_config()