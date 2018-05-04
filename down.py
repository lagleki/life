#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from sys import argv
from ete3 import Tree
from ete3 import NCBITaxa
ncbi = NCBITaxa()
#ncbi.update_taxonomy_database()

descendants = ncbi.get_descendant_taxa(argv[1], collapse_subspecies=True) #2759 - eukarya
# com = ncbi.get_common_names(descendants)
# names = ncbi.translate_to_names(descendants)
# with open("eu.txt", 'w') as f:
#     f.write("\n".join(map(str, names)))
    
#regex = re.compile(r"y", re.IGNORECASE)
"""
with open('eu-res.txt','w') as text_file:  
    print ('start')
    for line in descendants:
        com = ncbi.get_common_names([line])
        linn = ncbi.translate_to_names([line])[0]
        if r"'" in linn:
          print (str(line)+"\t"+ "\t" + str(linn.encode('utf-8')) + "\t" +str(com.get(line)))
        #print(str(line)+"\t"+com.get(line)+"\t"+linn,flags=re.UNICODE)

        lineold = linn
        #remove symbols that are special in lojban:
        linn = re.sub(r"y", "yui", linn,flags=re.UNICODE)
        linn = re.sub(r"w", "yuu", linn,flags=re.UNICODE)
        linn = re.sub(r"yui", "ywi", linn,flags=re.UNICODE)
        linn = re.sub(r"yuu", "ywu", linn,flags=re.UNICODE)
        linn = re.sub(r"[hH]", "y'", linn,flags=re.UNICODE)
        #h must both follow and be followed by a vowel, diphthong, or y:
        linn = re.sub(r"'([^aeiouy])", "'y\g<1>", linn,flags=re.UNICODE)
        #detect glides, krulermonize them:
        linn = re.sub(r"([aeiouy])(i)([aeiouy])", u"\g<1>ɩ\g<2>", linn,flags=re.UNICODE)
        linn = re.sub(r"([aeiouy])(u)([aeiouy])", u"\g<1>w\g<2>", linn,flags=re.UNICODE)
        #add ' between vowels:
        linn = re.sub(r"(a)([aeo])", "\g<1>'\g<2>", linn,flags=re.UNICODE)
        linn = re.sub(r"(e)([aeou])", "\g<1>'\g<2>", linn,flags=re.UNICODE)
        linn = re.sub(r"(i)([aeiou])", "\g<1>'\g<2>", linn,flags=re.UNICODE)
        linn = re.sub(r"(o)([aeou])", "\g<1>'\g<2>", linn,flags=re.UNICODE)
        linn = re.sub(r"(u)([aeiou])", "\g<1>'\g<2>", linn,flags=re.UNICODE)
        linn = re.sub(r"([aeiouy])y", "\g<1>'y", linn,flags=re.UNICODE)
        #voiced consonants can't be next to voiceless ones, and vice versa:
        linn = re.sub(r"([ptkfsc])([ptkfsc])", "\g<1>|\g<2>", linn,flags=re.UNICODE)
        linn = re.sub(r"([bdgvzj])([bdgvzj])", "\g<1>|\g<2>", linn,flags=re.UNICODE)
        linn = re.sub(r"([ptkfscbdgvzj])([ptkfscbdgvzj])", "\g<1>y\g<2>", linn,flags=re.UNICODE)
        linn = re.sub(r"\|", "", linn,flags=re.UNICODE)
        #no consonant can be followed by itself:
        linn = re.sub(r"([ptkfscbdgvzjlmnrx])\1", "\g<1>y\g<1>", linn,flags=re.UNICODE)
        #sibilants (cjsz) can't be next to each other:
        linn = re.sub(r"([cjsz])([cjsz])", "\g<1>y\g<2>", linn,flags=re.UNICODE)
        #x can't be next to c or k:
        linn = re.sub(r"([x])([ck])", "\g<1>y\g<2>", linn,flags=re.UNICODE)
        linn = re.sub(r"([ck])([x])", "\g<1>y\g<2>", linn,flags=re.UNICODE)
        #the substrings mz, nts, ntc, ndz, ndj are not allowed:
        linn = re.sub(r"mz", "myz", linn,flags=re.UNICODE)
        linn = re.sub(r"nts", "nyts", linn,flags=re.UNICODE)
        linn = re.sub(r"ntc", "nytc", linn,flags=re.UNICODE)
        linn = re.sub(r"ndz", "nydz", linn,flags=re.UNICODE)
        linn = re.sub(r"ndj", "nydj", linn,flags=re.UNICODE)
        #add consonant to the end
        linn = re.sub(r"c(?![\'])(\b|$)", "cyc", linn,flags=re.UNICODE)
        linn = re.sub(r"([aeiou]) ", "\g<1>c ", linn,flags=re.UNICODE)
        linn = re.sub(r"([aeiou])$", "\g<1>c", linn,flags=re.UNICODE)
        #special words:
        linn = re.sub(r"\bx\b", "ku'a la", linn,flags=re.UNICODE)
        #final:
        linn = r"la " + linn
        #output:
        fin = str(line)+"\t"+str(lineold) + "\t" + str(linn.encode('utf-8')) + "\t" +str(com.get(line))
        #print(fin+"\n")
        #text_file.write(fin+'\n')
"""
print("end")
"""
with open('new.txt') as text_file, open('xyz.txt', 'w') as myfile:  
    for line in text_file:
        var1, var2 = line.split(",");
        myfile.write(var1+'\n')
"""
"""
print(">>> Downloading Archaeal tree...")
tarc = ncbi.get_descendant_taxa(2157, return_tree=True)
print(">>> DONE")
print("\n>>> Writing trees to files...")
tarc.write(outfile = "ARCHAEA", features = ["name", "taxid", "sci_name","common_name","rank"], format_root_node=True)
print("\n>>> Downloading Bacterial tree...")
tbac = ncbi.get_descendant_taxa(2, return_tree=True)
print(">>> DONE")
print("\n>>> Writing trees to files...")
tbac.write(outfile = "BACTERIA", features = ["name", "taxid", "sci_name","common_name","rank"], format_root_node=True)
print("\n>>> Downloading Euka tree...")
teuc = ncbi.get_descendant_taxa(2759, return_tree=True)
print(">>> DONE")
print("\n>>> Writing trees to files...")
teuc.write(outfile = "EUKARYOTES", features = ["name", "taxid", "sci_name","common_name","rank"], format_root_node=True)
print(">>> DONE")
"""

"""
def toLojban( linn ):
    linn = re.sub(r"y", "yui", linn,flags=re.UNICODE)
    linn = re.sub(r"w", "yuu", linn,flags=re.UNICODE)
    linn = re.sub(r"yui", "ywi", linn,flags=re.UNICODE)
    linn = re.sub(r"yuu", "ywu", linn,flags=re.UNICODE)
    linn = re.sub(r"[hH]", "y'", linn,flags=re.UNICODE)
    #h must both follow and be followed by a vowel, diphthong, or y:
    linn = re.sub(r"'([^aeiouy])", "'y\g<1>", linn,flags=re.UNICODE)
    #detect glides, krulermonize them:
    linn = re.sub(r"([aeiouy])(i)([aeiouy])", u"\g<1>ɩ\g<2>", linn,flags=re.UNICODE)
    linn = re.sub(r"([aeiouy])(u)([aeiouy])", u"\g<1>w\g<2>", linn,flags=re.UNICODE)
    #add ' between vowels:
    linn = re.sub(r"(a)([aeo])", "\g<1>'\g<2>", linn,flags=re.UNICODE)
    linn = re.sub(r"(e)([aeou])", "\g<1>'\g<2>", linn,flags=re.UNICODE)
    linn = re.sub(r"(i)([aeiou])", "\g<1>'\g<2>", linn,flags=re.UNICODE)
    linn = re.sub(r"(o)([aeou])", "\g<1>'\g<2>", linn,flags=re.UNICODE)
    linn = re.sub(r"(u)([aeiou])", "\g<1>'\g<2>", linn,flags=re.UNICODE)
    linn = re.sub(r"([aeiouy])y", "\g<1>'y", linn,flags=re.UNICODE)
    #voiced consonants can't be next to voiceless ones, and vice versa:
    linn = re.sub(r"([ptkfsc])([ptkfsc])", "\g<1>|\g<2>", linn,flags=re.UNICODE)
    linn = re.sub(r"([bdgvzj])([bdgvzj])", "\g<1>|\g<2>", linn,flags=re.UNICODE)
    linn = re.sub(r"([ptkfscbdgvzj])([ptkfscbdgvzj])", "\g<1>y\g<2>", linn,flags=re.UNICODE)
    linn = re.sub(r"\|", "", linn,flags=re.UNICODE)
    #no consonant can be followed by itself:
    linn = re.sub(r"([ptkfscbdgvzjlmnrx])\1", "\g<1>y\g<1>", linn,flags=re.UNICODE)
    #sibilants (cjsz) can't be next to each other:
    linn = re.sub(r"([cjsz])([cjsz])", "\g<1>y\g<2>", linn,flags=re.UNICODE)
    #x can't be next to c or k:
    linn = re.sub(r"([x])([ck])", "\g<1>y\g<2>", linn,flags=re.UNICODE)
    linn = re.sub(r"([ck])([x])", "\g<1>y\g<2>", linn,flags=re.UNICODE)
    #the substrings mz, nts, ntc, ndz, ndj are not allowed:
    linn = re.sub(r"mz", "myz", linn,flags=re.UNICODE)
    linn = re.sub(r"nts", "nyts", linn,flags=re.UNICODE)
    linn = re.sub(r"ntc", "nytc", linn,flags=re.UNICODE)
    linn = re.sub(r"ndz", "nydz", linn,flags=re.UNICODE)
    linn = re.sub(r"ndj", "nydj", linn,flags=re.UNICODE)
    #add consonant to the end
    linn = re.sub(r"c(?![\'])(\b|$)", "cyc", linn,flags=re.UNICODE)
    linn = re.sub(r"([aeiou]) ", "\g<1>c ", linn,flags=re.UNICODE)
    linn = re.sub(r"([aeiou])$", "\g<1>c", linn,flags=re.UNICODE)
    #special words:
    linn = re.sub(r"\bx\b", "ku'a la", linn,flags=re.UNICODE)
    #final:
    linn = r"la " + linn
    return linn
"""
