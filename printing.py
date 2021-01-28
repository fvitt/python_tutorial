def print_comparison(name, dates, times, original_data, computed_data):
    """
    Print a comparison of two time series (original and computed)
    
    Parameters:
        name: A string name for the data being compared. (Limited
              to 9 characters in length)
        dates: List of strings representing the dates for each data element
        times: List of strings representing time of day for each data element
        original_data: List of original data (floats)
        computed_data: List of computed data (floats)
    """

    # Output comparison of data
    print('                ORIGINAL  COMPUTED')
    print(' DATE    TIME {name.upper():>9} {name.upper():>9} DIFFERENCE')
    print('------- ------ --------- --------- ----------')
    zip_data = zip(dates, times, original_data, computed_data)

    for date, time, orig, comp in zip_data:
        diff = orig - comp
        print(f'{date} {time:>6} {orig:9.6f} {comp:9.6f} {diff:10.6f}')

