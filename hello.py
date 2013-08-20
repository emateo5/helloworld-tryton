from trytond.model import ModelView, ModelSQL, fields

__all__ = ['Hello']


class Hello(ModelSQL, ModelView):
    "Hello World"
    __name__ = "hello.hello"

    name = fields.Char('Name')
    greeting = fields.Char('Greeting')
