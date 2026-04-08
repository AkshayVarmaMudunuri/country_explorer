def test_very_long_name_is_invalid():
    long_name = "A" * 101
    assert is_valid_country_name(long_name) == False

def test_single_character_is_invalid():
    assert is_valid_country_name("A") == False

def test_spaces_only_is_invalid():
    assert is_valid_country_name("  ") == False

def test_valid_two_char_name():
    assert is_valid_country_name("UK") == True

def test_country_with_no_neighbours():
    from api.countries import get_country
    country = {"name": "Japan", "neighbours": []}
    neighbours_str = ", ".join(country["neighbours"]) or " None (island nation)"
    assert neighbours_str == " None (island nation)"

