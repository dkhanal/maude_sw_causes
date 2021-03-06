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
    global files_to_classify
    global trained_models_dir
    global output_dir
    global target_file_max_num_records_to_classify
    global models
    global positive_probability_threshold
    global overall_classification_method
    global min_models_needed_for_overall_pos_classification
    global min_required_record_length
    global upload_output_to_remote_server
    global upload_positive_files_only
    global positive_signals_for_false_negative_check
    global remote_server
    global verbose

    files_to_classify = config_data['files_to_classify']
    output_dir = config_data['output_dir']
    trained_models_dir = config_data['trained_models_dir']
    models = config_data['models']
    target_file_max_num_records_to_classify = config_data['target_file_max_num_records_to_classify']
    positive_probability_threshold = config_data['positive_probability_threshold']
    overall_classification_method = config_data['overall_classification_method']
    min_models_needed_for_overall_pos_classification = config_data['min_models_needed_for_overall_pos_classification']
    min_required_record_length = config_data['min_required_record_length']

    upload_output_to_remote_server = config_data['upload_output_to_remote_server']
    upload_positive_files_only = config_data['upload_positive_files_only']

    positive_signals_for_false_negative_check = config_data['positive_signals_for_false_negative_check']

    remote_server = config_data['remote_server']
    verbose = config_data['verbose']

    logging.info('Configuration loaded.')

load_config()

