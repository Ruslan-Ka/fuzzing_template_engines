# Django
import django
from django.template import loader, Template, Context
from django.conf import settings
# Jinja
import jinja2
# Tornado
from tornado import template


def Jinja(f_input, f_output, context: dict):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./results/templates'))
    template = env.get_template(f'{f_input}')
    result = template.render(context)
    with open(f'./results/templates/jinja/{f_input}', 'w+') as f:
        print(result, file=f)

def Django(f_input, f_output, context:dict):
    settings.configure(TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['./templates/'],
            'APP_DIRS': False,
        },
    ])
    django.setup()
    template = loader.get_template(f"django/{f_input}")
    result = template.render(context)
    if f_output != "":
        with open(f'./results/templates/django/{f_output}', 'w+') as f:
            print(result, file=f)

def Tornado(f_input, f_output, context: dict):
    loader = template.Loader("./templates/tornado")
    result = loader.load(f"{f_input}").generate(var=context)
    if f_output != "":
        with open(f'./results/templates/tornado/{f_output}', 'w+') as f:
            print(result, file=f)