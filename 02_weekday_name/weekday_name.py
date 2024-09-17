def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] 

    if day_of_week < 1 or day_of_week > 7:
        return None
    return week_days[day_of_week - 1] # when I return week_days[day_of_week - 1] its important to remember that when returning, it is based off of the 0-based indexing 
   
    print('weekday_name(1)')




    