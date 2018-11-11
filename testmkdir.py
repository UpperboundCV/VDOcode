import os
import argparse


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True,
	help="path of Image")
args = vars(ap.parse_args())

if not os.path.exists(args['path']):
    os.mkdir(args['path'])