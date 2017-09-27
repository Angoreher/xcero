from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog


class MagicClient(object):

    def get_sets(self):
        return Set.all()

    def get_cards(self):
        return Card.all()

    def get_cards_by_set_code(selfi, set_code):
        return Card.where(set=set_code).all()
