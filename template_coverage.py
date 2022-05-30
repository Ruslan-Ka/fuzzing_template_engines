import jinja2
import json
import os
import random
from fuzzingbook.Coverage import *
from create_template import Jinja

CUR_FILE = os.path.basename(__file__)
ENGINE = CUR_FILE[CUR_FILE.rfind("_")+1:-3]

xss_vectors = open("xss_vectors.txt", "r").readlines()
XSS = random.choice(xss_vectors)
IDENTIFIER = random.choice([XSS, "VALUE"])


def test_cov(input_template, output_dir):
    try:
        with Coverage() as first_cov:
            Jinja(f_input=input_template, f_output="", context={"IDENTIFIER": IDENTIFIER})
    except Exception as e:
        pass
    print(f'COVERADE_LINES: {len(first_cov.coverage())}')


