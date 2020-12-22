import hashlib
import json


def hash_string_256(string):
    """Create a SHA256 hash for a given input string.

    Arguments:
        :string: The string which should be hashed.
    """
    return hashlib.sha256(string).hexdigest()


def hash_block(block):
    """Hashes a block and returns a string representation of it.

    Arguments:
        :block: The block that should be hashed.
    """
    # sha256()      : takes a string as arg and returns bytehash value
    # hexdigest()   : used to convert bytehash value normal string hash
    # jason.dumps() : converts 'block' from dict -> string

    # convert Block object in to dict format to convert it to json format.
    hashable_block = block.__dict__.copy()

    # converting transactions in Dict format hashable_block to an orderedDict
    hashable_block['transactions'] = [tx.to_ordered_dict()
                                      for tx in hashable_block['transactions']]

    return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())
