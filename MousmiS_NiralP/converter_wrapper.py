import converter
#1
def miles_to_km(miles):
    print(f'{miles} miles = {converter.miles_to_km(miles)} km')

#2
def km_per_hr_to_m_per_s(km_per_hr):
    print(f'{km_per_hr} km_per_hr = {converter.km_per_hr_to_m_per_s(km_per_hr):.1f} m_per_s')

#3
def sqmetres_to_hectares(sq_meters):
    print(f'{sq_meters} sq_meters = {converter.sqmetres_to_hectares(sq_meters)} hectares')

#4
def sqmetres_to_acres(sq_meters):
    print(f'{sq_meters} sq_meters = {converter.sqmetres_to_acres(sq_meters)} acres')

#5
def acres_to_edge_of_square(acres):
    print(f'{acres} acres = {converter.acres_to_edge_of_square(acres)} edge_of_square')

#6
def get_bear_count(count):
    print(f'{count} count = {converter.get_bear_count(10)} get_bear_count')

#7
def dms_to_dd(degrees, minutes, seconds):
    print(f'{degrees, minutes, seconds} d_m_s =  {converter.dms_to_dd(degrees, minutes, seconds)} dd')

#8
def dd_to_dms(degrees):
    print(f'{degrees} dd = {converter.dd_to_dms(degrees)} dms')

#9
def get_fuel_cost(mileage,fuel_price):
    print(f'{mileage, fuel_price} m_fp = {converter.get_fuel_cost(mileage, fuel_price)} fuel_cost')








