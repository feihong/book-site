from pathlib import Path
import jinja2

here = Path(__file__).parent

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(here / 'templates'),
    autoescape=jinja2.select_autoescape(),
    trim_blocks=True,
    lstrip_blocks=True)

def get_template(template_name):
  return env.get_template(template_name)
