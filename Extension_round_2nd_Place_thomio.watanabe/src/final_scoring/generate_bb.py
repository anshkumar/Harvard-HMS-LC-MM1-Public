#!/usr/bin/env python
from hms_lung_tumor import HMSLungTumor
import argparse

# Import arguments
parser = argparse.ArgumentParser()
parser.add_argument('--root_path', type=str, required=True)
parser.add_argument('--output_file', type=str, required=True)
args = parser.parse_args()

root_path = args.root_path
file_name = args.output_file


if __name__ == "__main__":
    gt = HMSLungTumor()

    print 'Generating output file...'

    # Path to patient scans
    gt.generate_bb( root_path, file_name )
