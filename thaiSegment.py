#!/opt/python-2.7/bin/python2.7 -S
#  -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 23:12:40 2013

@author: Haotian He
# collaborated with Jonggun Park and T. J. Trimble
# student ID: 1261169
# course: LING 473
# Project: 3
# instructor: Jim White
"""

# sets the default encoding to UTF-8 to make Thai readable
import sys
reload(sys)
sys.setdefaultencoding("UTF-8")

import codecs

# uses the codecs to open the input file and split on new lines
data = codecs.open('fsm-input.utf8.txt', encoding='utf-8').read()

V1 = u"\u0E40\u0E41\u0E42\u0E43\u0E44"
C1 = u"\u0E01\u0E02\u0E03\u0E04\u0E05\u0E06\u0E07\u0E08\u0E09\u0E0A\u0E0B\u0E0C\u0E0D\u0E0E\u0E0F" \
     + u"\u0E10\u0E11\u0E12\u0E13\u0E14\u0E15\u0E16\u0E17\u0E18\u0E19\u0E1A\u0E1B\u0E1C\u0E1D\u0E1E\u0E1F" \
     + u"\u0E20\u0E21\u0E22\u0E23\u0E24\u0E25\u0E26\u0E27\u0E28\u0E29\u0E2A\u0E2B\u0E2C\u0E2D\u0E2E"
C2 = u"\u0E23\u0E25\u0E27\u0E19\u0E21"
V2 = u"\u0E34\u0E35\u0E36\u0E37\u0E38\u0E39\u0E31\u0E47"
T  = u"\u0E48\u0E49\u0E4A\u0E4B"
V3 = u"\u0E32\u0E2D\u0E22\u0E27"
C3 = u"\u0E07\u0E19\u0E21\u0E14\u0E1A\u0E01\u0E22\u0E27"

# sets the initial state for the syllables as 0
state = 0
# sets the original result text as null
result = ''

# reads each character in Thai data
for char in data:
	
    # having the state 7 or 8, puts a space before the previous character
    if state == 7 or state == 8:
        post = result[-1]
        result = result[:-1]
        result += ' '
        result += post
        if state == 7: state = 1
        else: state = 2
    # having the state 9, put a space after the currect character
    elif state == 9:
        result += ' '
        state = 0
								
    # having the escape character, change to a new line
    if char == u'\u000A':
        state = 0
        result += '<br />'
    else: result += char
				
    # having the state 0
    if state == 0:
        if char in V1:
            state = 1
        elif char in C1:
            state = 2
    # having the state 1
    elif state == 1:
        if char in C1:
            state = 2
    # having the state 2
    elif state == 2:
        if char in C2:
            state = 3
        elif char in V2:
            state = 4
        elif char in T:
            state = 5
        elif char in V3:
            state = 6
        elif char in C3:
            state = 9
        elif char in V1:
            state = 7
        elif char in C1:
            state = 8
    # having the state 3
    elif state == 3:
        if char in V2:
            state = 4
        elif char in T:
            state = 5
        elif char in V3:
            state = 6
        elif char in C3:
            state = 9
    # having the state 4
    elif state == 4:
        if char in T:
            state = 5
        elif char in V3:
            state = 6
        elif char in C3:
            state = 9
        elif char in V1:
            state = 7
        elif char in C1:
            state = 8
    # having the state 5
    elif state == 5:
        if char in V3:
            state = 6
        elif char in C3:
            state = 9
        elif char in V1:
            state = 7
        elif char in C1:
            state = 8
    # having the state 6
    elif state == 6:
        if char in C3:
            state = 9
        elif char in V1:
            state = 7
        elif char in C1:
            state = 8

# adds up the html form to the original text.
htmloutput = ''
htmloutput += u"<html><meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />" + u"<body>"
htmloutput += result
htmloutput += u"</body></html>"

# writes the Thai script in the html form to an html file
open('output.html', 'w').write(htmloutput)