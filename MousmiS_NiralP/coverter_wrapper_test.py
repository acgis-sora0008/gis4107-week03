import converter_wrapper as cw
def test_miles_to_km():
    miles = 10
    actual = cw.miles_to_km(miles)
    expected = '10 mi = 16.0934 km'
    print(f'Expected : {expected}')
    print(f'actual :{actual}')

    test_miles_to_km()
    print('')