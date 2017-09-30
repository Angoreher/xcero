from random import randint
from mtgsdk import Card
from mtgsdk import Set
# from mtgsdk import Type
# from mtgsdk import Supertype
# from mtgsdk import Subtype
# from mtgsdk import Changelog


class MagicClient(object):

    def get_sets(self):
        return Set.all()

    def get_set_by_set_code(self, set_code):
        return Set.find(set_code)

    def get_cards(self):
        return Card.all()

    def get_card_by_name(self, name):
        return Card.where(name=name).all()

    def get_cards_by_set_code(selfi, set_code):
        return Card.where(set=set_code).all()


class MagicMapper(object):
    CARD_TO_MODEL = {
        'set': 'card_set',
        'subtypes': 'card_subtypes',
        'supertypes': 'card_supertypes',
        'type': 'card_type',
        'types': 'card_types',
        'id': 'external_id',
    }

    SET_TO_MODEL = {
        'id': 'external_id',
        'type': 'set_type',
    }


def get_random_card(cards=None):
    if cards:
        return cards[randint(0, cards.count())]
