import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    # TODO: Implement function
    # Constants to Adjust the train, val and test data sets
    P_TRAIN = 0.8 
    P_VAL   = 0.1 
    P_TEST = (1 - P_TRAIN, P_VAL)

    # Get all the files in the source directory 
    files = glob.glob(os.path.join(source,"*.tfrecord"))
    random.shuffle(files)

    n_total = len(files)
    n_train = int(P_TRAIN * n_total)
    n_val   = int(P_VAL * n_total)
    n_test  = n_total - n_train - n_val 

    split = {
        "train" : files[:n_train],
        "val"   : files[n_train:n_train + n_val],
        "test"  : files[n_train + n_val:]    
    }

    for split_name, split_files in splits.items():
        split_dir = os.path.join(destination, split_name)
        os.makedirs(split_dir, exist_ok=True)
        for f in split_files:
            dest_file = os.path.join(split_dir, os.path.basename(f))




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)