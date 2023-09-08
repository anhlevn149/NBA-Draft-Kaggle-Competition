def convert_ht(text):
    """
    Convert column ht into float values
    """
    # Split the string value by the hyphen
    parts = str(text).split("-")
    result = ""
    # Define a dictionary to map month names to numbers
    month_map = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7}
    
    # Check if the parts list contains two elements
    if len(parts) == 2:
        # Save the second location of the parts list as month
        month = parts[1]
        # Check if month in month_map, then result is f"{month_number}.{parts[0]}". If month is 00 and parts[0] in month_map, then result is f"{month_number}.1"
        if month in month_map:
            month_number = month_map[month]
            result = f"{month_number}.{parts[0]}"
        elif month == "00" and parts[0] in month_map:
            month_number = month_map[parts[0]]
            result = f"{month_number}.1"
    #If not, replace as NaN value
    else:
        result = np.NaN
    
    return result