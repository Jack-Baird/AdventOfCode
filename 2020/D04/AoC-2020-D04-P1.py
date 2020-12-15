# AoC 2020, Day 04, Part 1
# https://adventofcode.com/2020/day/4

#* Part 1
#[x]: Read in input data
#[x]: Parse whole passports (into list of passports?)
#[x]: Parse individual passports to read their details
#[x]: Determine how many passports have all 7 required fields (cid is optional)
#* Part 2
#[x]: Determine how many of those passports have valid data

"""DISCLAIMER: This isn't all mine - I found Redditor u/andrew502502's post with a much
more elegant solution than my non-starter and decided to reinforce my Class knowledge
by building on his example. His is at https://pastebin.com/J3W445Bi (as at 15/12/20).
"""

# -- Passport Fields --
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

import re

class Passport:
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid=None):
        self.byr = int(byr)
        self.iyr = int(iyr)
        self.eyr = int(eyr)
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def is_valid_height(self):
        #* This reads horribly compared to the original, but I wanted to explore chaining inline conditionals
        return 150 <= int(self.hgt.strip('cm')) <= 193 if 'cm' in self.hgt else 59 <= int(self.hgt.strip('in')) <= 76 if 'in' in self.hgt else False

    def is_valid_document(self):
        valid_eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return True if (
            1920 <= self.byr <= 2002 and                # Assumes 18 <= Valid age to hold a passport <= 100
            2010 <= self.iyr <= 2020 and                # Assumes passport is less than 10 years old
            2020 <= self.eyr <= 2030 and                # Checks that the passport isn't expired or valid for more than 10 years
            self.is_valid_height() and                  # Checks that a valid height is recorded
            re.match(r'^#[a-f0-9]{6}$', self.hcl) and   # Checks for a valid hair colour hexcode*
            self.ecl in valid_eye_colours and           # Checks that recorded hair colour matches one of the valid entries
            re.match(r'^[0-9]{9}$', self.pid)           # Checks that the passport number is the correct length (9 digits)*
        ) else False                                    #_*for both of these, adding '$' to the end of the regex ensures there are no further chars

def read_data(filename):
    with open(filename, 'r') as infile:
        return infile.read().split('\n\n')

def has_required_fields(string):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    #* This was interesting - I hadn't come across all(x) before!
    return True if all([field in string for field in required_fields]) else False

def string_to_passport(string):
    params = {}
    for field_string in re.split(' |\n', string):
        #* Again interesting - I would have regex'd this but this is much more efficient!
        [field, value] = field_string.split(':')
        params[field] = value
    return Passport(**params)

# Read in input data
data = read_data('2020/D04/D04-Input.txt')

# Parse whole passports (into list of passports?)
valid_strings = [string for string in data if has_required_fields(string)]

# Parse individual passports to read their details
passports = [string_to_passport(string) for string in valid_strings]

# Determine how many passports have all 7 required fields (cid is optional) - Part 1 solution
print(f'\x1b[32;1mValid Passports:\x1b[0m {len(valid_strings)}') #! 235

# Determine how many of those passports have valid data
valid_passports = [passport for passport in passports if passport.is_valid_document()]
print(f'\x1b[32;1mWith Valid Data:\x1b[0m {len(valid_passports)}') #! 194