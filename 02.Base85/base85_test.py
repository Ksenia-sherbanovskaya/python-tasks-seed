"""
Unit tests for 02.Base85

TODO: Add more tests!
"""

import base85ed


def test_shorts_encode():
    """
    Test trivial short encodes
    """
    assert base85ed.encode(b"1") == b"F#"
    assert base85ed.encode(b"12") == b"F){"
    assert base85ed.encode(b"123") == b"F)}j"
    assert base85ed.encode(b"1234") == b"F)}kW"


def test_shorts_decode():
    """
    Test trivial short decodes
    """
    assert base85ed.decode(b"F#") == b"1"
    assert base85ed.decode(b"F){") == b"12"
    assert base85ed.decode(b"F)}j") == b"123"
    assert base85ed.decode(b"F)}kW") == b"1234"

def test_empty_string():
    assert base85ed.encode(b"") == b""
    assert base85ed.decode(b"") == b""

def test_zeros():
    original = b"\x00\x00\x00\x00"
    encoded = base85ed.encode(original)
    decoded = base85ed.decode(encoded)
    assert original == decoded

def test_string():
    original = b"hi everyone"
    encoded = base85ed.encode(original)
    decoded = base85ed.decode(encoded)
    assert original == decoded

def test_random_data():
    import random
    random.seed(42)
    for i in range(17):
        original = bytes(random.randint(0,255) for j in range(i))
        assert original == base85ed.decode(base85ed.encode(original))

def test_not_multiples_4():
    for b in (b"A", b"AB", b"ABC"):
        assert b == base85ed.decode(base85ed.encode(b))