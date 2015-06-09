# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:40:34 2015

@author: collinjlarkin
"""

import sys
import os
from os.path import expanduser, join
import logging
import subprocess
from rdkit import Chem
from rdkit.Chem import Draw
import PIL.Image
import shlex
import hashlib
import json
import operator
sys.modules['Image'] = PIL.Image

def dic_fxn(x):    
    dic = {}
    by_lines = x.split('\n')
    for line in by_lines:
        k,v = shlex.split(line)
        dic[k] = float(v)
        sort_dic = sorted(dic, key=dic.__getitem__, reverse=True)
    return sort_dic

def ord_fxn(x):
    dic = {}
    by_lines = x.split('\n')
    for line in by_lines:
        k,v = line.split()
        dic[k] = float(v)
        sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse = True)
    return sorted_dic

def json_fxn(line):
    k,v = shlex.split(line)
    dic_conf = {'conf' : v}
    dic_smiles = {'smiles' : k}
    dic_img = {'img' : '{}.png'.format(hashlib.md5(k).hexdigest()[:12])}
    return dic_conf,dic_img,dic_smiles

def _exec_log(string, arg_dic=None, input=None):
    """
    Smartly executes the given string and logs the results
    """
    if(arg_dic is not None):
        for k,v in arg_dic.iteritems():
            string += ' {} {}'.format(k,v)
    logging.info('Running {} with arguments'.format(string))
    try:
        process = subprocess.Popen(string, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
                           
        if(input is None):
            out, err = process.communicate()
        else:
            out, err = process.communicate(input)
        retcode = process.returncode
        if(len(err) > 0):
            logging.warning(err)
            logging.debug(out)
        if retcode < 0:
            logging.error('{} failed with {}. stderr follow'.format(string, retcode))
            logging.error(err)
            raise OSError('{} failed with {}. stderr follow'.format(string, retcode))
        return out
        for line in out:
            return line
    except OSError as e:
        print >>sys.stderr, 'Execution of {} failed:'.format(string), e

#pic = sys.argv[1]
pic = 'Good_pic.jpg'
#dest = sys.argv[2]
arg_dic = {'-p' : '', '' : pic }

#smile_CV = _exec_log('osra', arg_dic=arg_dic)
smile_CV = '''C#CCCCC(C(C)C)C -0.130591
CCCCCC -0.0858108
CCCCCC 0.0411409
*CCCCCCC=* -0.800324
CCCCCC -0.0858108'''

best_guesses_CV = ord_fxn(smile_CV[:-2])
best_guesses = 
idx = 0
for j in best_guesses:
    idx += 1
    if idx == 6:
        break
    else:
        print "\"{}\"".format(j)


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no'")

ans = query_yes_no('Do you want to save the best guess as a .png file?')

if ans == True:
    nm_list = []
    for element in best_guesses:
        hash_nm = hashlib.md5(element).hexdigest()[:12]
        m = Chem.MolFromSmiles(element)
        img = Draw.MolToImage(m)
        #img.save('{}.png'.format(hash_nm))

by_lines = smile_CV[:-2].split('\n')
dic_list = []
for line in by_lines:
    dic_list.append(json_fxn(line))
json_list = json.dumps(dic_list, sort_keys=True)
#print sorted(json_list,key=operator.itemgetter(1))
count = 0
#conf_list = {}
for l in json_list:
    count += 1
    n = int(count-1)
    #conf_list.append(dic_list[n][0])
    #print sorted(json_list, key=operator.itemgetter(1)(json_list[n]))
#print sorted(conf_list.items(), key=operator.itemgetter(1))