### Util library for interacting with csv files

import csv
import os


def readerWithFunction(filepath, function, arg=None):
    """Read from a csv and execute a function using each row. Return a sequential list of all values returned by the function.

    filepath -- the path of the csv we're reading
    function -- the function we're executing once per row
    arg -- if the function takes an additional argument, we pass arg (default None)
    """
    with open(filepath, newline="") as file:
        reader = csv.reader(file, delimiter=",")
        value = []
        for row in reader:
            if arg == None:
                value.append(function(row))
            else:
                value.append(function(row, arg))
        file.close()
        return value


def dictWriter(filepath, dict, flag="w"):
    """Completely rewrite a csv using the values in a single dictionary.

    filepath -- the path of the csv, whether or not it exists
    dict -- the dictionary to pull all values from
    flag -- flag for open() (default "w")
        "w" will also activate writeheader()
    """
    with open(filepath, flag, newline="") as file:

        dictWriter = csv.DictWriter(file, fieldnames=dict.keys(), delimiter=",")
        if flag == "w":
            dictWriter.writeheader()
        dictWriter.writerow(dict)
        file.close()


def dictReaderFirstRow(filepath):
    """Get a dictionary of the first (non-header) row of values in a csv

    filepath -- the path of the csv, whether or not it exists
    """
    with open(filepath, newline="") as file:
        dict = {}
        dictReader = csv.DictReader(file)
        for row in dictReader:
            firstRow = True
            if firstRow:
                dict = row
            firstRow = False
        file.close()
        return dict


def dictReaderMultiRow(filepath, idName):
    """Get a dictionary of dictionaries of the (non-header) row of values in a csv

    filepath -- the path of the csv, whether or not it exists
    """
    with open(filepath, newline="") as file:
        dict = {}
        dictReader = csv.DictReader(file)
        for row in dictReader:
            dict[row[idName]] = row
        file.close()
        return dict


def getIndexOfField(filepath, field):
    """Get the index (column number) of a field in a csv.

    filepath -- the path of the csv we're searching
    field -- the field string we're looking for
    """
    return readerWithFunction(filepath, sub_getIndexOfField, field)[0]


def sub_getIndexOfField(row, field):
    """Helper function for getIndexOfField() that can be passed to readerWithFunction().

    row - the array representation of a csv row (presumably the fields row)
    field - the field string we're looking for
    """
    return row.index(field)
