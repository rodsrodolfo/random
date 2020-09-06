# taken from https://magpylib.readthedocs.io/en/latest/_pages/2_guideExamples/

import magpylib as magpy
from magpylib.source.current import Circular
from numpy import linspace

# windings of three parts of a coil
coil1a = [Circular(curr=1,dim=3,pos=[0,0,z]) for z in linspace( -3,-1,10)]
coil1b = [Circular(curr=1,dim=3,pos=[0,0,z]) for z in linspace( -1, 1,10)]
coil1c = [Circular(curr=1,dim=3,pos=[0,0,z]) for z in linspace(  1, 3,10)]

# create collection and manipulate step by step
c1 = magpy.Collection(coil1a)
c1.move([-1,-1,0])
c1.addSources(coil1b)
c1.move([-1,-1,0])
c1.addSources(coil1c)
c1.move([-1,-1,0])

# windings of three parts of another coil
coil2a = [Circular(curr=1,dim=3,pos=[3,3,z]) for z in linspace(-3,-1,15)]
coil2b = [Circular(curr=1,dim=3,pos=[3,3,z]) for z in linspace( -1,1,15)]
coil2c = [Circular(curr=1,dim=3,pos=[3,3,z]) for z in linspace( 1,3,15)]

# create individual sub-collections
c2a = magpy.Collection(coil2a)
c2b = magpy.Collection(coil2b)
c2c = magpy.Collection(coil2c)

# combine sub-collections to one big collection
c2 = magpy.Collection(c2a,c2b,c2c)

# still manipulate each individual sub-collection
c2a.rotate(-15,[1,-1,0],anchor=[0,0,0])
c2c.rotate(15,[1,-1,0],anchor=[0,0,0])

# combine all collections and display system
c3 = magpy.Collection(c1,c2)
magpy.displaySystem(c3,figsize=(6,6))