import sys
import os
import logging
import subprocess
from rdkit import Chem
from rdkit.Chem import Draw
import PIL.Image
import shlex
import hashlib
import json
import operator
import urllib
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
    k,v = line
    dic_total = {"conf" : v, "smiles" : k, "img" : "{}".format(urllib.quote(open("{}.png".format(hashlib.md5(k).hexdigest()[:12]), "rb").read().encode("base64")))}
    #dic_conf = {'conf' : v}
    #dic_smiles = {'smiles' : k}
    #dic_img = {'img' : '{}'.format(urllib.quote(open("{}.png".format(hashlib.md5(k).hexdigest()[:12]), "rb").read().encode("base64")))}
    #return dic_conf,dic_img,dic_smiles
    return dic_total

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

def end(pic):
    #pic = sys.argv[1]
    #pic = 'good_pic_copy.jpg'
    arg_dic = {'-j':'','-i':'','-p' : pic}

    smile_CV = _exec_log('osra', arg_dic=arg_dic)
    #smile_CV = '''C#CCCCC(C(C)C)C -0.130591
    #CCCCCC -0.0858108
    #CCCCCC 0.0411409
    #*CCCCCCC=* -0.800324
    #CCCCCC -0.0858108'''

    best_guesses_CV = ord_fxn(smile_CV[:-2])
    best_guesses = dic_fxn(smile_CV[:-2])
    #idx = 0
    #for j in best_guesses:
        #idx += 1
        #if idx == 6:
            #break
        #else:
            #print "\"{}\"".format(j)

    for element in best_guesses:
        try:
            hash_nm = hashlib.md5(element).hexdigest()[:12]
            m = Chem.MolFromSmiles(element)
            img = Draw.MolToImage(m)
            img.save('{}.png'.format(hash_nm))
        except ValueError:
            print "RDKit can't read this smiles!"
            break

    dic_list = []
    for line in best_guesses_CV:
        json_list = json_fxn(line)
        return json_list
        
    #print(json_list)
    #return dic_list
    #return dic_list

if __name__=='__main__':
	print end()
