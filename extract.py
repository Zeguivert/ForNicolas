#!/usr/bin/env python
# coding: utf-8

# In[14]:


# SOME USEFUL TRICKS

import ROOT
import rootpy
import numpy as np
#import root_numpy as rnp


from rootpy.tree import Tree

from rootpy.io import root_open


# In[15]:


# DATA

def extract_tree(file_path, tree_path, tree_name):

    data_file = root_open(file_path,"read")
    dir = data_file.GetDirectory(tree_path)

    if data_file:
        return dir.Get(tree_name) #rnp.tree2array( dir.Get(tree_name) )
    else:
        print "File or tree not found, try again !"


# In[16]:


#tree = extract_tree("data/dvcs_tree_P07slot2_DR4.7.root","With RPD/Dvcs Tree - t_cut_2","T_dvcs")
#from rootpy.plotting import Hist, HistStack, Canvas, Pad

#c1=Canvas()
#to_plot = "phi"
#selection ="1.*(beam_charge == 1)"
#hist = Hist(100, -1, 1, type='F') #this is old school, using rootpy there are much better ways
#tree.Draw(to_plot,selection=selection,hist=hist)
#c1.cd()
#hist.Draw("hist")
#c1


# In[5]:


#cnt=0
#for el in tree:
#    print el.phi
#    cnt+=1
#    if cnt==10: break


# In[3]:


def add_array_stack(stack,hist):
    for i in range(len(stack)):
        (stack[i]).Add(hist[i])


# In[6]:


#def extract_kin(beam_charge):

#    xbj = np.array([el.xbj for el in tree])
#    Q2 = np.array([el.Q2 for el in tree])
#    nu = np.array([el.nu for el in tree])
#    phi = np.array([el.phi for el in tree])


#extract_kin(-1)


# In[7]:


# créer classe pour mu+ et mu- avec les bons paramètres
# USELESS


# In[8]:


#class npTree:
#    """

#    """
#    def __init__(self, file_path, tree_path, tree_name, charge):
        # self.sourceTree = extract_tree(file_path, tree_path, tree_name)
        # #self.npTree_charge = extract_tree(file_path, tree_path, tree_name)
        # self.beam_charge = charge
        #     # extract subtree in array according to beam_charge choice
        #
        # #self.npTree_charge = [el for el in self.sourceTree if el.beam_charge == charge]
        # #self.npTree_charge = self.sourceTree[ (el.beam_charge == charge) for el in self.sourceTree]
        # #self.xbj = np.array([el.xbj for el in self.npTree_charge])
        #
        # self.t = np.array([el.t for el in self.sourceTree if el.beam_charge == charge])
        # self.xbj = np.array([el.xbj for el in self.sourceTree if el.beam_charge == charge])
        # self.Q2 = np.array([el.Q2 for el in self.sourceTree if el.beam_charge == charge])
        # self.nu = -np.array([el.nu for el in self.sourceTree if el.beam_charge == charge])
        # self.phi = np.array([el.phi for el in self.sourceTree if el.beam_charge == charge])
        



# In[9]:


#data_minus = npTree("data/hist.root","With RPD/Dvcs Tree - t_cut_2","T_dvcs",-1)
#data_minus = npTree("data/dvcs_tree_P07slot2_DR4.7.root","With RPD/Dvcs Tree - t_cut_2","T_dvcs",-1)

#print data_minus.t


# In[ ]:
