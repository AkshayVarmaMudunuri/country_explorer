def test_get_country_returns_correct_name(mocker):

    fake_api_data = [{

        "name":       {"common": "Japan", "official": "Japan"},
        "capital":    ["Tokyo"],
        "population": 125700000,
        "languages":  {"jpn": "Japanese"},
        "currencies": {"JPY": {"name": "Japanese yen", "symbol": "¥"}},
        "borders":    [],
        "flag":       "🇯🇵",
        "area":       377930,
        "region":     "Asia",
        "subregion":  "Eastern Asia",
        "timezones":  ["UTC+09:00"],
        "independent": "kw">True,
        "flags":      {"png": "https://flagcdn.com/jp.png"}

    }]

    mocker.patch("api.countries.requests.get",
    return_value = mocker.Mock(
        status_code = 200,
        json=lambda: fake_api_data
    ))

    from api.countries import get_country
    result = get_country("Japan")
    assert result["name"] == "Japan"
    assert result["capital"] == "Tokyo"
    assert result["population"] == 125700000


