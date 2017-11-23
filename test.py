#  ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ _________ ____ ____ ____ ____
# ||I |||n |||s |||e |||r |||t |||       |||C |||o |||d |||e |||       |||H |||e |||r |||e ||
# ||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||_______|||__|||__|||__|||__||
# |/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|

# DON'T FORGET TO CHANGE the2.minority_shape_intersect TO minority_shape_intersect IF YOU DONT USE IMPORT !!!

# def minority_shape_intersect(first_minority_shape, second_minority_shape):
#     return ()


# Or import the2.py
import the2


#   *   )             )
# ` )  /(   (      ( /( (          (  (
#  ( )(_)) ))\ (   )\()))\   (     )\))(
# (_(_()) /((_))\ (_))/((_)  )\ ) ((_))\
# |_   _|(_)) ((_)| |_  (_) _(_/(  (()(_)
#   | |  / -_)(_-<|  _| | || ' \))/ _` |
#   |_|  \___|/__/ \__| |_||_||_| \__, |
#                                 |___/

# Set SENSITIVITY
SENSITIVITY = 0.001

# Create Empty Test List
tests = []

# This means run all tests. You can specify which tests to run by setting this to ["X", "Uber Basic"] etc.
wantedTests = []

# Whether to show calculated input or not
show_calculated_input = True

### Example Tests ###

# Test X (On the instruction PDF)
if len(wantedTests) == 0 or wantedTests.find("X") < 0:
    text_x_calculations = the2.minority_shape_intersect(
        [(4., 8.), (20.6, 10.), (9.4, 18.1)],
        [(12.5, 7.), (18.7, 16.2), (2., 12.), (12.5, 11.3)]
    )

    test_x_results = [
        (12.5, 11.3),
        (12.5, 9.024096385542167),
        (13.984606613454961, 9.202964652223491),
        (16.513454260733393, 12.955448257862459),
        (13.748900224891674, 14.954813230212277),
        (6.781560380848003, 13.202548119734228),
        (5.996175908221797, 11.733588272785214)
    ]

    test_x = ("X", test_x_results, text_x_calculations)

    tests.append(test_x)

# Test Uber Basic
if len(wantedTests) == 0 or wantedTests.find("Uber Basic") < 0:
    test_uber_basic_calculations = the2.minority_shape_intersect(
        [(-6, 6), (0, 6), (0, -6), (-6, -6)],
        [(-2, -2), (-2, 2), (0, 0)]
    )

    test_uber_basic_results = [
        (-2, -2),
        (-2, 2),
        (0, 0)
    ]

    test_uber_basic = ("Uber Basic", test_uber_basic_results,
                       test_uber_basic_calculations)

    tests.append(test_uber_basic)

### End Of Example Tests ###

### Tests in honour of Arda Kara ###

# Test One Point In
if len(wantedTests) == 0 or wantedTests.find("One Point In") < 0:

    test_triangle_ONEPOINTIN_calculations = the2.minority_shape_intersect(
        [(1.1, 6.9), (2.8, 4.3), (5.3, 8.2)],
        [(3., 7.), (5.9, 4.), (8., 7.1)]
    )

    test_triangle_ONEPOINTIN_results = [
        (3.920414673046252, 6.047846889952153),
        (4.550649350649351, 7.031012987012987),
        (3.0, 7.0)
    ]

    test_triangle_ONEPOINTIN = ("One Point In",
                                test_triangle_ONEPOINTIN_results, test_triangle_ONEPOINTIN_calculations)

    tests.append(test_triangle_ONEPOINTIN)

# Test Two Point In
if len(wantedTests) == 0 or wantedTests.find("Two Point In") < 0:
    test_triangle_TWOPOINTIN_calculations = the2.minority_shape_intersect(
        [(0.1, 0.1), (0.5, 0.1), (0.1, 1.0)],
        [(0.2, 0.5), (0.3, 0.3), (0.3, 1.0)]
    )

    test_triangle_TWOPOINTIN_results = [
        (0.3, 0.5500000000000002),
        (0.23793103448275862, 0.6896551724137931),
        (0.2, 0.5),
        (0.3, 0.3)
    ]

    test_triangle_TWOPOINTIN = ("Two Point In",
                                test_triangle_TWOPOINTIN_results, test_triangle_TWOPOINTIN_calculations)

    tests.append(test_triangle_TWOPOINTIN)

# Test Whole Inside
if len(wantedTests) == 0 or wantedTests.find("Whole Inside") < 0:
    test_triangle_WHOLEINSIDE_calculations = the2.minority_shape_intersect(
        [(6., 6.), (9., 1.), (12., 6.)],
        [(8., 5.), (8., 4.), (9., 3.)]
    )

    test_triangle_WHOLEINSIDE_results = [(8., 5.), (8., 4.), (9., 3.)]

    test_triangle_WHOLEINSIDE = ("Whole Inside",
                                 test_triangle_WHOLEINSIDE_results, test_triangle_WHOLEINSIDE_calculations)

    tests.append(test_triangle_WHOLEINSIDE)

# Test Adjacent Edge
if len(wantedTests) == 0 or wantedTests.find("Adjacent Edge") < 0:
    test_triangle_WHOLEINSIDE_calculations = the2.minority_shape_intersect(
        [(6., 6.), (9., 1.), (12., 6.)],
        [(6., 6.), (12., 6.), (6., 10.)]
    )

    test_triangle_WHOLEINSIDE_results = [(6., 6.), (12., 6.)]

    test_triangle_WHOLEINSIDE = ("Adjacent Edge",
                                 test_triangle_WHOLEINSIDE_results, test_triangle_WHOLEINSIDE_calculations)

    tests.append(test_triangle_WHOLEINSIDE)

# Test Point on Edge
if len(wantedTests) == 0 or wantedTests.find("Point on Edge") < 0:
    test_triangle_POINTONEDGE_calculations = the2.minority_shape_intersect(
        [(6., 6.), (9., 1.), (12., 6.)],
        [(7., 6.), (8., 8.), (4., 8.)]
    )

    test_triangle_POINTONEDGE_results = [(7., 6.)]

    test_triangle_POINTONEDGE = ("Point on Edge",
                                 test_triangle_POINTONEDGE_results, test_triangle_POINTONEDGE_calculations)

    tests.append(test_triangle_POINTONEDGE)

# Test Common Corner
if len(wantedTests) == 0 or wantedTests.find("Common Corner") < 0:
    test_triangle_COMMONCORNER_calculations = the2.minority_shape_intersect(
        [(6., 6.), (9., 1.), (12., 6.)],
        [(6., 6.), (8., 8.), (4., 8.)]
    )

    test_triangle_COMMONCORNER_results = [(6., 6.)]

    test_triangle_COMMONCORNER = ("Common Corner",
                                  test_triangle_COMMONCORNER_results, test_triangle_COMMONCORNER_calculations)

    tests.append(test_triangle_COMMONCORNER)

### End Of Arda Kara ###


# Insert your own cool named test here

# Right below this comment


# Ok thats enough


import datetime

total_start_time = datetime.datetime.now()

print ""

failed_post_count = 0

for test in tests:

    start_time = datetime.datetime.now()

    name, results, calculations = test

    results_length = len(results)
    calculations_length = len(calculations)

    is_failed = False

    print "Test", name
    print "-" * 30

    if show_calculated_input:
        print "(@) Calculations:", calculations

    if results_length != calculations_length:
        print "(!) Failed: Correct results has", results_length, "items, but calculations has", calculations_length
        is_failed = True
    else:
        print "(~) Passed: Correct results has", results_length, "items, calculations also has", calculations_length

    print ""

    for result in results:

        is_calculated = False

        for calculation in calculations:
            if abs(result[0] - calculation[0]) <= SENSITIVITY and abs(result[1] - calculation[1]) <= SENSITIVITY:
                is_calculated = True
                break

        if is_calculated:
            print "(~) Passed:", result
        else:
            print "(!) Failed:", result
            is_failed = True

    print ""

    finish_time = datetime.datetime.now()

    if is_failed:
        failed_post_count = failed_post_count + 1
        print "(!) Test", name, "failed. (In " + str((finish_time - start_time).total_seconds() * 1000) + " milliseconds)"
    else:
        print "(~) Test", name, "passed. (In " + str((finish_time - start_time).total_seconds() * 1000) + " milliseconds)"

    print ""

total_finish_time = datetime.datetime.now()

print "--- Tested", len(tests), "conditions,", failed_post_count, "failed", len(tests) - failed_post_count, "passed. (In " + str((total_finish_time - total_start_time).total_seconds() * 1000) + " milliseconds) ---"
