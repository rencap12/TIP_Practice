# #!/bin/python

# import math
# import os
# import random
# import re
# import sys



# #
# # Complete the 'calcMissing' function below.
# #
# # The function accepts STRING_ARRAY readings as parameter.
# #
# from datetime import datetime


# def calcMissing(readings):
#     data = []
#     missing_vals = {}
#     for i, lines in enumerate(readings):
#         parts = lines.strip().split()
#         date_s = parts[0] + " " + parts[1]
#         value_s = parts[2]

#         date = datetime.strptime(date_s, '%m/%d/%Y %H:%M:%S')

#         if "Missing_" in value_s:
#             val = int(value_s.split('_')[1])
#             missing_vals[val] = (i, date)
#             data.append((date, None))
#         else:
#             data.append((date, float(value_s)))

#     predictions = {}

#     for missing_val, (idx, date) in missing_vals.items():
#         before_val = None
#         after_val = None

#         # find before
#         for i in range(idx - 1, -1, -1):
#             if data[i][1] is not None:
#                 before_val = data[i][1]
#                 break
        
#         # find after
#         for j in range(idx + 1, len(data)):
#             if data[j][1] is not None:
#                 after_val = data[j][1]
#                 break

#         if before_val is not None and after_val is not None:
#             predictions[missing_val] = (before_val + after_val) / 2
#         elif before_val is not None:
#             predictions[missing_val] = before_val
#         elif after_val is not None:
#             predictions[missing_val] = after_val
#         else:
#             all_vals = [v for _, v in data if v is not None]
#             predictions[missing_val] = sum(all_vals) / len(all_vals)

#     # for k, v in predictions.items():
#     #     print(v)
#     for l in range(1, 21):
#         if l in predictions:
#             print(predictions[l])
#         else:
#             # If a missing number isn't found, use average of all values
#             all_values = [v for _, v in data if v is not None]
#             print(sum(all_values) / len(all_values))


# # if __name__ == '__main__':
# #     readings_count = int(raw_input().strip())

# #     readings = []

# #     for _ in xrange(readings_count):
# #         readings_item = raw_input()
# #         readings.append(readings_item)

# #     calcMissing(readings)





























from datetime import datetime


def parser(readings):
    data = []
    missing_vals = {}

    for i, lines in enumerate(readings):
        parts = lines.strip().split()
        date_s = parts[0] + " " + parts[1]
        val_s = parts[2]

        date = datetime.strptime(date_s, '%m/%d/%Y %H:%M:%S')

        if "Missing_" in val_s:
            temp = int(val_s.split("_")[1])
            missing_vals[temp] = (i, date)
            data.append((date, None))
        else:
            data.append((date, float(val_s)))

    predictions = {}

    for missing_val, (idx, date) in missing_vals.items():
        before = None
        after = None

        for x in range(idx - 1, -1, -1):
            if data[x][1] is not None:
                before = data[x][1]
                break
        
        for j in range(idx + 1, len(data)):
            if data[j][1] is not None:
                after = data[j][1]

        if before is not None and after is not None:
            predictions[missing_val] = (before + after) / 2
        elif before is not None:
            predictions[missing_val] = before
        elif after is not None:
            predictions[missing_val] = after
        else:
            all_val = [v for _, v in data if v is not None]
            predictions[missing_val] = sum(all_val) / len(all_val)

    for m, n in predictions.items():
        print(n)
