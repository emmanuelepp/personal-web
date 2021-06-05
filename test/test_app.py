import pytest
import datetime

# arr
date = datetime.datetime.now().strftime('%Y')

# act


def test_date_case():
    result = date
    return result


# assert
assert test_date_case() != None
