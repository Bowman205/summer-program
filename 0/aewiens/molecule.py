#! /usr/bin/python

import numpy as np

class Molecule:
   """
   implements the basic properties of a molecule
   """

   def __init__(self, geom_str, units="Angstrom"):
      self.read(geom_str)
      self.units = units

   def read(self, geom_str):
      """
      Read in the geometry (as a list of strings, by readlines() ), and store 2 class variables:
      1. self.atoms (a list of labels of the N atoms)
      2. self.geom (an Nx3 numpy array of the x,y,z coordinates of each of the atoms) 
      """
      self.atoms = [i[0] for i in geom_str[2:]]
      self.geom = np.array([ [float(i.split()[j]) for j in range(1,4)] for i in geom_str[2:] ])

   def __str__(self):
      """
      Print the molecule in a nice format
      """
      out = "%d\n%s\n" % (len(self),self.units)
      for i in range(len(self.geom)):
         out += "%s%15.7f%15.7f%15.7f\n" % (self.atoms[i], self.geom[i][0], self.geom[i][1], self.geom[i][2])
      return out

   def __len__(self):
      """
      return the length of the molecule (think of as the # of atoms, N)
      """
      return len(self.geom)


   def bohr(self):
      """
      return the geometry in bohr
      """
      conv = 1.889725989
      if self.units == "Angstrom":
         self.geom = [ [i[0]*conv, i[1]*conv, i[2]*conv] for i in self.geom]
         self.units == "Bohr"
      return self.geom

   def angs(self):
      """
      return the geometry in Angstroms
      """
      conv = 1.889725989
      if self.units == "Bohr":
         self.geom = [ [i[0]/conv, i[1]/conv, i[2]/conv] for i in self.geom]
         self.units = "Angstrom"
      return self.geom 

#### Example of an input
#f = open("molecule.xyz","r")
#f = f.readlines()

#mol = Molecule(f)

#print mol.geom
#print mol.atoms
#print mol.__len__()
#print mol.__str__()

#print mol.angs()
#print mol.bohr()
