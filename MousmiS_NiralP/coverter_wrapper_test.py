import converter_wrapper as cw

#1
def test_miles_to_km():
    miles = 10
    actual = cw.miles_to_km(miles)
    expected = '10 mi = 16.0934 km'
    print(f'Expected : {expected}')
    print(f'actual :{actual}')
    test_miles_to_km()
    print('')

#2
def test_km_per_hr_to_m_per_s():
    km_per_hr = 100
    actual = cw.km_per_hr_to_m_per_s(km_per_hr)
    expected = '100 km/hr = 27.8 m/s'
    print(f'Expected: {expected}')
    print(f'Actual: {actual}')
    test_km_per_hr_to_m_per_s()
    print('')

#3
def test_sqmetres_to_hectares():
    sq_meters = 10000
    actual = cw.sqmetres_to_hectares(sq_meters)
    expected = '10000 sqm = 1 hectare'
    print(f'Expected: {expected}')
    print(f'Actual: {actual}')
    test_sqmetres_to_hectares()
    print('')

#4
def test_sqmetres_to_acres():
    sq_meters = 4000
    actual = cw.sqmetres_to_acres(sq_meters)
    expected = '4000 sqm = 0.988 acre'
    print(f'Expected: {expected}')
    print(f'Actual: {actual}')
    test_sqmetres_to_acres()
    print('')

#5
def test_acres_to_edge_of_square():
    acres = 1
    actual = cw.acres_to_edge_of_square(acres)
    expected = '1 acre = 4046.84 sqm  edge_length = sqrt(4046.84) = 63.615'
    print(f'Expected: {expected}')
    print(f'Actual: {actual}')
    test_acres_to_edge_of_square()
    print('')

#6
def test_get_bear_count():
    count = 10
    actual = cw.get_bear_count(count)
    expected = ' g_b_c = 10 '
    print(f'Expected: {expected}')
    print(f'Actual: {actual}')
    test_get_bear_count()
    print('')


#7
def test_dms_to_dd():
    degrees = 25
    minutes = 55
    seconds = 34
    actual = cw.dms_to_dd(degrees, minutes, seconds)
    expected =  ' dms(75,56,34) = 75.9428 dd '
    print(f'Expected: {expected}')
    print(f'Actual: {actual}')
    test_dms_to_dd()
    print('')

#8
def test_dd_to_dms():
    degrees = 25.13
    actual = cw.dd_to_dms(degrees)
    expected =  'dd 25.13 = dms(25,7,48) '
    print(f'Expected: {expected}')
    print(f'Actual: {actual}')
    test_dd_to_dms()
    print('')

#9
def test_get_fuel_cost():
    mileage = 35
    fuel_price = 112
    actual = cw.get_fuel_cost(mileage, fuel_price)
    expected = ' fuel_cost = 35 * 112 = 3920 '
    print(f'Expected: {expected}')
    print(f'Actual: {actual}')
    test_get_fuel_cost()
    print('')
