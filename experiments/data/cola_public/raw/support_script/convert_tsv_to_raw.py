"""
Convert TSV file into raw sentence break
Stack every sentence on top of each other
"""

import sys
import argparse

'''
    Parse the raw input into a suitable format that can help 
    If anything wrong happen here
'''
# def parse_extr_character(s):
#     i = 0
#     result = ''
#     while i < len(s):
#         if i+2 < len(s) and s[i:i+3] == 'n\'t':
#             result += ' n\'t'
#             i += 3
#             continue
#         elif i+2 < len(s) and s[i:i+3] == 's\' ':
#             result += 's \' '
#             i += 3
#             continue
#         elif i+6 < len(s) and s[i:i+7] == 'o\'clock':
#             result += 'o\'clock'
#             i += 7
#             continue
#         elif i+5 < len(s) and s[i:i+6] == 'cannot':
#             result += 'can not'
#             i += 6
#             continue
#         elif s[i] == '\'':
#             if i+1 < len(s) and s[i+1] == '\'':
#                 result += '\'\''
#                 i += 2
#                 continue
#             else:
#                 result += ' '
#         elif s[i] == ':':
#             if i-1 >= 0 and s[i-1] != ' ':
#                 result += ' '
#             if i+1 < len(s) and s[i+1] != ' ':
#                 result += ': '
#                 i += 1
#                 continue
#         elif s[i] == '–':
#             result += '--'
#             i += 1
#             continue
#         elif s[i] == '$':
#             result += '$ '
#             i += 1
#             continue

#         result += s[i]
#         i += 1

#     return result

argp = argparse.ArgumentParser()
argp.add_argument('input_raw_filepath')
argp.add_argument('output_conll_filepath')
args = argp.parse_args()

sys.stdout = open(args.output_conll_filepath, 'w')

for line in open(args.input_raw_filepath):
    line = line.split('\t')  
    sentence = line[3]
    if sentence.find('(') == -1 and sentence.find(')') == -1:
        sys.stdout.write(sentence)
