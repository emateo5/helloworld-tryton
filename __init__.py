
from trytond.pool import Pool
from .hello import *


def register():
    Pool.register(
        Hello,
        module='helloworld', type_='model')

