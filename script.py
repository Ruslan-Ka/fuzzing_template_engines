#!/home/ruslan/учеба/диплом/final_project/env1/bin/python

from create_template import Jinja
from template_coverage import test_cov
from tatsu_generate import generate_template
from sys import argv
import getopt
from os import listdir
from os.path import isfile, join
import random

if argv[1] == "generate_samples":
    #d_in = argv[2]
    #d_out = argv[3]
    d_in = "./templates/base_templates1"
    d_out = "./templates/jinja"
    onlyfiles = [f for f in listdir(d_in) if isfile(join(d_in, f))]
    for i in onlyfiles:
        base_template = open(f'{d_in}/{i}', "r")
        lines = base_template.readlines()
        place = random.randint(0, len(lines) - 1)
        base_template.seek(0)
        new_file = open(f'{d_out}/{i}', "a+")
        for i in range(0, len(lines)):
            new_file.write(lines[i])
            if i == place:
                new_file.write("<br/>$TEMPLATE$<br/>")

elif argv[1] == "generate_templates":
    check = 1
    max_length_regex = 100
    max_counter = 2
    recursion_limit = 1000
    grammar = "jinja2.ebnf"
    d_in = ""
    d_out = ""
    if len(argv) >= 3:
        grammar = argv[2]
    if len(argv) >= 4:
        max_length_regex = int(argv[3])
    if len(argv) >= 5:
        max_counter = int(argv[4])
    if len(argv) == 6:
        recursion_limit = int(argv[5])
    if len(argv) == 7:
        print("Wrong number of arguments")
        exit()
    if len(argv) == 8:
        d_in = argv[6]
        d_out = argv[7]

    result = ""
    stack = ""
    try:
        result, stack = generate_template(grammar, max_length_regex, max_counter, recursion_limit)
        check = 1
    except Exception as e:
        check = 0
        print(f'Error:{e}')

    if check == 1:
        if d_in == "" or d_out == "":
            print(result)
            print(stack)
        else:
            d_in = "./templates/jinja"
            d_out = "./results/templates"
            onlyfiles = [f for f in listdir(d_in) if isfile(join(d_in, f))]
            f_name = random.choice(onlyfiles)
            f = open(f'{d_in}/{f_name}', "r")
            text = f.read()
            text = text.replace("$TEMPLATE$", result)
            new_file = open(f'{d_out}/{f_name}', "a+")
            new_file.write(text)

elif argv[1] == "coverage":
    f_output = ""
    test_cov(argv[2], f_output)


