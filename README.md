ddd-flask-example
=================

A terse example of DDD-inspired architecture using Flask and SQLAlchemy and MongoDB as storage options.


setup.py --- Code Golf
=================

from blogex_app import Context

if __name__ == "__main__": Context.setup()

presentation.py --- Cook Book
=================

from jinja2 import Undefined
from jinja2.filters import do_mark_safe

def linebreaksp(text):
    if text is None or isinstance(text, Undefined):
        return text 
    text = "<p>" + text.replace('\n', '</p><p>') + "</p>"
    return do_mark_safe(text)

def register_filters(app):
    app.jinja_env.filters['linebreaksp'] = linebreaksp
