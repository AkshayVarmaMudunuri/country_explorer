from utils.validator import is_valid_country_name, clean_name
from utils.display import format_population 

def test_valid_name_returns_true():
    assert is_valid_country_name("Japan") == True

def test_empty_name_returns_false():
    assert is_valid_country_name("") == False

def test_name_with_numbers_returns_false():
    assert is_valid_country_name("Japan123") == False

def test_clean_name_strips_spaces():
    assert clean_name(" japan ") == "Japan"

def test_clean_name_title_cases():
    assert clean_name( "united kingdom" ) == "United Kingdom"