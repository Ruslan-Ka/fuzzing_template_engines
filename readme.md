## Templates fuzzer

### Requirements
- Python >= 3.8
- [fuzzingbook](https://github.com/uds-se/fuzzingbook)
- [TatSu](https://github.com/neogeny/TatSu)
- [Jinja2 = 3.1](https://github.com/pallets/jinja/tree/3.1.x)
- Other packages are in the requirements.txt file.

### Usage
<arg\> - optinal argument
#### Generate HTML samples with placeholders for template block
``./script.py generate_samples input_dir output_dir``
#### Generate a template block and display the result in console or file
``./script.py generate_templates <path_to_grammar> <max_length_regex> <max_counter> <recursion_limit> <html_template_dir> <output_dir>``  
**max_length_regex** - limit the derivations for all terminals of the grammar with a regex patterns to this length  
**max_counter** - select all options randomly until each has been chosen max_counter of times  
**recursion_limit** - sys.setrecursionlimit()  
**Note:**  
If `html_template_dir`  and `output_dir` are provided. randomly select  html template from `html_template_dir` and replace placeholder \\$TEMPLATE\\$ with generated template block. Write result to `output_dir`  
#### Count coverage and display the result in console
``./script.py coverage input_file``  
**input_file** - template file  
Count coverage lines for input template.
