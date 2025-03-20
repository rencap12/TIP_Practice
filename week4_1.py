from datetime import datetime

def calcMissing(readings):
    """
    Calculate missing mercury level values in a time series.
    Extremely simple approach using nearest neighbors.
    """
    # Parse data and identify missing values
    data = []
    missing_values = {}
    
    for i, line in enumerate(readings):
        parts = line.strip().split()
        # Handle format with date, time, and value
        date_str = parts[0] + " " + parts[1]
        value_str = " ".join(parts[2:])
        
        date = datetime.strptime(date_str, '%m/%d/%Y %H:%M:%S')
        
        if "Missing_" in value_str:
            missing_num = int(value_str.split('_')[1])
            missing_values[missing_num] = (i, date)
            data.append((date, None))
        else:
            data.append((date, float(value_str)))
    
    # For each missing value, find closest neighbors
    predictions = {}
    
    for missing_num, (idx, date) in missing_values.items():
        # Look for values before and after
        before_val = None
        after_val = None
        
        # Find closest before
        for i in range(idx-1, -1, -1):
            if data[i][1] is not None:
                before_val = data[i][1]
                break
        
        # Find closest after
        for i in range(idx+1, len(data)):
            if data[i][1] is not None:
                after_val = data[i][1]
                break
                
        # Simple prediction logic
        if before_val is not None and after_val is not None:
            # Average of neighbors
            predictions[missing_num] = (before_val + after_val) / 2
        elif before_val is not None:
            # Just use before value
            predictions[missing_num] = before_val
        elif after_val is not None:
            # Just use after value
            predictions[missing_num] = after_val
        else:
            # Unlikely case - calculate average of all values
            all_values = [v for _, v in data if v is not None]
            predictions[missing_num] = sum(all_values) / len(all_values)
    
    # Print results for all 20 possible missing values
    for i in range(1, 21):
        if i in predictions:
            print(predictions[i])
        else:
            # If a missing number isn't found, use average of all values
            all_values = [v for _, v in data if v is not None]
            print(sum(all_values) / len(all_values))




# Test manually
if __name__ == "__main__":
    # Uncomment the test case you want to try
    
    # Test Case 1
    # test_case_1 = [
    #     "1/1/2022 16:00:00 25.5",
    #     "1/2/2022 16:00:00 Missing_1",
    #     "1/3/2022 16:00:00 26.0",
    #     "1/4/2022 16:00:00 Missing_2",
    #     "1/5/2022 16:00:00 27.5",
    # ]
    # print("Running Test Case 1:")
    # calcMissing(test_case_1)
    
    # # Test Case 2
    # test_case_2 = [
    #     "2/1/2022 16:00:00 30.0",
    #     "2/2/2022 16:00:00 31.0",
    #     "2/3/2022 16:00:00 Missing_1",
    #     "2/4/2022 16:00:00 Missing_2",
    #     "2/5/2022 16:00:00 Missing_3",
    #     "2/6/2022 16:00:00 35.0",
    #     "2/7/2022 16:00:00 36.0",
    # ]
    # print("\nRunning Test Case 2:")
    # calcMissing(test_case_2)
    
    # # Test Case 3
    test_case_3 = [
        "3/1/2022 16:00:00 Missing_1",
        "3/2/2022 16:00:00 40.0",
        "3/3/2022 16:00:00 42.0",
        "3/4/2022 16:00:00 41.0",
        "3/5/2022 16:00:00 Missing_2",
    ]
    print("\nRunning Test Case 3:")
    calcMissing(test_case_3)