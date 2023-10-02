import math
# Function to convert miles to kilometers
def miles_to_km(miles):
    ''' This function takes distance in miles and converts the miles to kilometersConvert miles to kilometers.
        Where 1 mile is equal to 1.06934 km
        Parameters:
        miles (float): The distance in miles to be converted.

        Returns:
        float: The equivalent distance in kilometers '''
    km = miles * 1.06934 # Conversion Factor 1 mile = 1.06934 km
    return km



# Function to convert kilometers per hour to meters per second
def km_per_hr_to_m_per_s(km_per_hr):
    ''' This function takes a speed in kilometers per hour and converts it to meters per second
    using the conversion factor: 1 km/h ≈ 0.27777778 m/s.
    Parameters:
    km_per_hr (float): The speed in kilometers per hour to be converted.

    Returns:
    float: The equivalent speed in meters per second.'''
    m_per_s = km_per_hr * 1000 / 3600
    return m_per_s



# Function to convert square meters to hectares
def sqmetres_to_hectares(sq_meters):
    ''' This function takes a area in square meters and converts it to hectares 
    using conversion factor: area in hectare = area in square meters devided by 10000 
    Parameters:
    sq_meters(float): the area in square meters to be converted.
    
    Returns:
    float: The equivalent area in hectare.'''
    hectares = sq_meters / 10000
    return hectares



# Function to convert square meters to acres
def sqmetres_to_acres(sq_meters):
    ''' This function takes a area in square meters and converts it to acres 
    using conversion factor: area in acre = area in square meters devided by 4046.86
    Parameters:
    sq_meters(float): the area in square meters to be converted.
    
    Returns:
    float: The equivalent area in acre.'''
    acres = sq_meters / 4046.86
    return acres


# Function to calculate the length of one edge of a square with given acres
def acres_to_edge_of_square(acres):
    ''' This function takes a area in acres and converts it to edge of square  
    1 acre is equal to approximately 4046.86 square meters
    To find the length of one edge of a square,  take the square root of the area in square meters
    (since a square has equal sides, only need one edge length)
    Parameters:
    acres(float): the area in acres to be converted.
    
    Returns:
    float: The length of an edge of square.''' 
    sq_meters = acres * 4046.86
    edge_length = math.sqrt(sq_meters)
    return edge_length

# Function to get the count of bears
def get_bear_count():
  """
    Get the count of bears.

    This function is used to determine the count of bears based on specific criteria or data sources.
    The exact implementation may vary depending on the context.

    Returns:
    int: The count of bears."""
    # You can implement the logic to count bears here.
    # The following is a placeholder; replace it with your actual logic.
    count = 10  
    return count


   

# Function to convert degrees, minutes, seconds (DMS) to decimal degrees (DD)
def dms_to_dd(degrees, minutes, seconds):
   ''' 
    This function takes degrees, minutes, and seconds and converts them to decimal degrees (DD) format.

    Parameters:
    degrees (int): The degrees part of the DMS representation.
    minutes (int): The minutes part of the DMS representation.
    seconds (float): The seconds part of the DMS representation.

    Returns:
    float: The equivalent decimal degrees value.
    Note:
    - The conversion is approximate, and the seconds part may include fractional seconds.
    - Positive values for degrees represent North or East directions; negative values represent South or West directions.'''
    # Implement the conversion here

    dd = degrees + minutes/60 + seconds/3600
    return dd



# Function to convert decimal degrees (DD) to degrees, minutes, seconds (DMS)
def dd_to_dms(decimal_degrees):
    '''  This function takes a decimal degrees value and converts it to degrees, minutes, and seconds (DMS) format.

    Parameters:
    decimal_degrees (float): The decimal degrees value to be converted.

    Returns:
    tuple: A tuple containing three elements:
        - int: Degrees part of the DMS representation.
        - int: Minutes part of the DMS representation.
        - float: Seconds part of the DMS representation.
     Note:
    - The conversion is approximate, and the seconds part may include fractional seconds.
    - Negative values for decimal degrees represent South or West directions.'''
    # Implement the conversion here
    degrees = int(decimal_degrees)
    remaining_minutes = (decimal_degrees - degrees) * 60
    minutes = int(remaining_minutes)
    seconds = (remaining_minutes - minutes) * 60
    return degrees, minutes, seconds


# Function to calculate fuel cost based on mileage and fuel price
def get_fuel_cost(mileage, fuel_price):
    ''' This function takes the mileage (distance) of a trip in miles and the price of fuel per unit
    (e.g., per gallon) and calculates the total fuel cost for the trip.

    Parameters:
    mileage (float): The distance of the trip in miles.
    fuel_price (float): The price of fuel per unit (e.g., per gallon).

    Returns:
    float: The calculated fuel cost for the trip.'''
    # Implement the calculation here
    if mileage <= 0 or fuel_price <= 0:
        return 0
    fuel_cost = mileage * fuel_price
    return fuel_cost
   