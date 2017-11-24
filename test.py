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

# Import sys to read CLI Arguments
import sys

### Options ###

# This means run all tests. You can specify which tests to run by setting this to ["X", "Uber Basic"] etc.
wanted_tests = []

# This means run all tests. You can specify which tests to not run by setting this to ["X", "Uber Basic"] etc.
# Eg. If "X" is specified, every test other than X will run
# !!! This is overwirtes wanted_tests and has more POWER !!!
unwanted_tests = []

# Whether to show calculated input or not
show_calculated_input = True

# Whether to show shapes used in the test or not
show_minority_shapes = True

# Whether to show only fails or whole test result
show_only_fails = False

### Options ###

### Check CLI arguments to change options ###

if "-fo" in sys.argv or "--fails-only" in sys.argv:
    show_only_fails = True

if "-nms" in sys.argv or "--no-minority-shapes" in sys.argv:
    show_minority_shapes = False

if "-nci" in sys.argv or "--no-calculated-input" in sys.argv:
    show_calculated_input = False

### Check CLI arguments to change options ###

### Example Tests ###

wanted_tests_length = len(wanted_tests)
unwanted_tests_length = len(unwanted_tests)

# Test X (On the instruction PDF)
if ((wanted_tests_length == 0 or "X" in wanted_tests) and ("X" not in unwanted_tests)):

    test_x_shapes = (
        [(4., 8.), (20.6, 10.), (9.4, 18.1)],
        [(12.5, 7.), (18.7, 16.2), (2., 12.), (12.5, 11.3)]
    )

    test_x_calculations = the2.minority_shape_intersect(
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

    test_x = (
        "X",
        test_x_results,
        test_x_calculations,
        test_x_shapes
    )

    tests.append(test_x)

# Test Uber Basic
if ((wanted_tests_length == 0 or "Uber Basic" in wanted_tests) and ("Uber Basic" not in unwanted_tests)):

    test_uber_basic_shapes = (
        [(-6, 6), (0, 6), (0, -6), (-6, -6)],
        [(-2, -2), (-2, 2), (0, 0)]
    )

    test_uber_basic_calculations = the2.minority_shape_intersect(
        [(-6, 6), (0, 6), (0, -6), (-6, -6)],
        [(-2, -2), (-2, 2), (0, 0)]
    )

    test_uber_basic_results = [
        (-2, -2),
        (-2, 2),
        (0, 0)
    ]

    test_uber_basic = (
        "Uber Basic",
        test_uber_basic_results,
        test_uber_basic_calculations,
        test_uber_basic_shapes
    )

    tests.append(test_uber_basic)

### End Of Example Tests ###

### Tests in honour of Arda Kara ###

# Test One Point In
if ((wanted_tests_length == 0 or "One Point In" in wanted_tests) and ("One Point In" not in unwanted_tests)):

    test_triangle_ONEPOINTIN_shapes = (
        [(1.1, 6.9), (2.8, 4.3), (5.3, 8.2)],
        [(3., 7.), (5.9, 4.), (8., 7.1)]
    )

    test_triangle_ONEPOINTIN_calculations = the2.minority_shape_intersect(
        [(1.1, 6.9), (2.8, 4.3), (5.3, 8.2)],
        [(3., 7.), (5.9, 4.), (8., 7.1)]
    )

    test_triangle_ONEPOINTIN_results = [
        (3.920414673046252, 6.047846889952153),
        (4.550649350649351, 7.031012987012987),
        (3.0, 7.0)
    ]

    test_triangle_ONEPOINTIN = (
        "One Point In",
        test_triangle_ONEPOINTIN_results, test_triangle_ONEPOINTIN_calculations,
        test_triangle_ONEPOINTIN_shapes
    )

    tests.append(test_triangle_ONEPOINTIN)

# Test Two Point In
if ((wanted_tests_length == 0 or "Two Point In" in wanted_tests) and ("Two Point In" not in unwanted_tests)):

    test_triangle_TWOPOINTIN_shapes = (
        [(0.1, 0.1), (0.5, 0.1), (0.1, 1.0)],
        [(0.2, 0.5), (0.3, 0.3), (0.3, 1.0)]
    )

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

    test_triangle_TWOPOINTIN = (
        "Two Point In",
        test_triangle_TWOPOINTIN_results, test_triangle_TWOPOINTIN_calculations,
        test_triangle_TWOPOINTIN_shapes
    )

    tests.append(test_triangle_TWOPOINTIN)

# Test Whole Inside
if ((wanted_tests_length == 0 or "Whole Inside" in wanted_tests) and ("Whole Inside" not in unwanted_tests)):

    test_triangle_WHOLEINSIDE_shapes = (
        [(6., 6.), (9., 1.), (12., 6.)],
        [(8., 5.), (8., 4.), (9., 3.)]
    )

    test_triangle_WHOLEINSIDE_calculations = the2.minority_shape_intersect(
        [(6., 6.), (9., 1.), (12., 6.)],
        [(8., 5.), (8., 4.), (9., 3.)]
    )

    test_triangle_WHOLEINSIDE_results = [
        (8., 5.),
        (8., 4.),
        (9., 3.)
    ]

    test_triangle_WHOLEINSIDE = (
        "Whole Inside",
        test_triangle_WHOLEINSIDE_results, test_triangle_WHOLEINSIDE_calculations,
        test_triangle_WHOLEINSIDE_shapes
    )

    tests.append(test_triangle_WHOLEINSIDE)

# Test Adjacent Edge
if ((wanted_tests_length == 0 or "Adjacent Edge" in wanted_tests) and ("Adjacent Edge" not in unwanted_tests)):

    test_triangle_ADJACENTEDGE_shapes = (
        [(6., 6.), (9., 1.), (12., 6.)],
        [(6., 6.), (12., 6.), (6., 10.)]
    )

    test_triangle_ADJACENTEDGE_calculations = the2.minority_shape_intersect(
        [(6., 6.), (9., 1.), (12., 6.)],
        [(6., 6.), (12., 6.), (6., 10.)]
    )

    test_triangle_ADJACENTEDGE_results = [
        (6., 6.),
        (12., 6.)
    ]

    test_triangle_ADJACENTEDGE = (
        "Adjacent Edge",
        test_triangle_ADJACENTEDGE_results, test_triangle_ADJACENTEDGE_calculations,
        test_triangle_ADJACENTEDGE_shapes
    )

    tests.append(test_triangle_ADJACENTEDGE)

# Test Point on Edge
if ((wanted_tests_length == 0 or "Point on Edge" in wanted_tests) and ("Point on Edge" not in unwanted_tests)):

    test_triangle_POINTONEDGE_SHAPES = (
        [(6., 6.), (9., 1.), (12., 6.)],
        [(7., 6.), (8., 8.), (4., 8.)]
    )

    test_triangle_POINTONEDGE_calculations = the2.minority_shape_intersect(
        [(6., 6.), (9., 1.), (12., 6.)],
        [(7., 6.), (8., 8.), (4., 8.)]
    )

    test_triangle_POINTONEDGE_results = [
        (7., 6.)
    ]

    test_triangle_POINTONEDGE = (
        "Point on Edge",
        test_triangle_POINTONEDGE_results, test_triangle_POINTONEDGE_calculations,
        test_triangle_POINTONEDGE_SHAPES
    )

    tests.append(test_triangle_POINTONEDGE)

# Test Common Corner
if ((wanted_tests_length == 0 or "Common Corner" in wanted_tests) and ("Common Corner" not in unwanted_tests)):

    test_triangle_COMMONCORNER_shapes = (
        [(6., 6.), (9., 1.), (12., 6.)],
        [(6., 6.), (8., 8.), (4., 8.)]
    )

    test_triangle_COMMONCORNER_calculations = the2.minority_shape_intersect(
        [(6., 6.), (9., 1.), (12., 6.)],
        [(6., 6.), (8., 8.), (4., 8.)]
    )

    test_triangle_COMMONCORNER_results = [
        (6., 6.)
    ]

    test_triangle_COMMONCORNER = (
        "Common Corner",
        test_triangle_COMMONCORNER_results, test_triangle_COMMONCORNER_calculations,
        test_triangle_COMMONCORNER_shapes
    )

    tests.append(test_triangle_COMMONCORNER)

### End Of Arda Kara ###


# Insert your own cool named test here

# Right below this comment


# Ok thats enough


import datetime

total_start_time = datetime.datetime.now()

failed_post_count = 0

for test in tests:

    start_time = datetime.datetime.now()

    willBePrintedResult = "\n"

    name, results, calculations, shapes = test

    results_length = len(results)
    calculations_length = len(calculations)

    is_failed = False

    willBePrintedResult += " Test " + name + "\n"
    willBePrintedResult += "-" * 30 + "\n"

    if show_minority_shapes:
        willBePrintedResult += "\t(@) First Shape: " + str(shapes[0]) + "\n"
        willBePrintedResult += "\t(@) Second Shape: " + str(shapes[1]) + "\n\n"

    if show_calculated_input:
        willBePrintedResult += "\t(@) Calculations: " + \
            str(calculations) + "\n\n"

    if results_length != calculations_length:
        willBePrintedResult += "\t(!) Failed: Correct results has " + str(
            results_length) + " items, but calculations has " + str(calculations_length)
        is_failed = True
    else:
        willBePrintedResult += "\t(~) Passed: Correct results has " + str(
            results_length) + " items, calculations also has " + str(calculations_length)

    willBePrintedResult += "\n\n"

    for result in results:

        is_calculated = False

        for calculation in calculations:
            if abs(result[0] - calculation[0]) <= SENSITIVITY and abs(result[1] - calculation[1]) <= SENSITIVITY:
                is_calculated = True
                break

        if is_calculated:
            willBePrintedResult += "\t(~) Passed: " + str(result)
        else:
            willBePrintedResult += "\t(!) Failed: " + str(result)
            is_failed = True
        willBePrintedResult += "\n"

    willBePrintedResult += "\n"

    finish_time = datetime.datetime.now()

    if is_failed:
        failed_post_count = failed_post_count + 1
        willBePrintedResult += "\t(!) Test " + name + " failed. (In " + str(
            (finish_time - start_time).total_seconds() * 1000) + " milliseconds)"

    else:
        willBePrintedResult += "\t(~) Test " + name + " passed. (In " + str(
            (finish_time - start_time).total_seconds() * 1000) + " milliseconds)"

    willBePrintedResult += "\n"

    if show_only_fails:
        if is_failed:
            print willBePrintedResult
    else:
        print willBePrintedResult

total_finish_time = datetime.datetime.now()

print "--- Tested", len(tests), "conditions,", failed_post_count, "failed", len(tests) - failed_post_count, "passed. (In " + str((total_finish_time - total_start_time).total_seconds() * 1000) + " milliseconds) ---"
