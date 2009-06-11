from chiplotle import *
from chiplotle.hpgl.compound.compound import _CompoundHPGL

def test_compound_hpgl_01( ):
   t = _CompoundHPGL((1, 2))

   assert t.pen is None
   assert t.xy.tolist( ) == [1, 2]
   assert t.xyabsolute.tolist( ) == [1, 2]
   assert t.x == 1
   assert t.y == 2
   assert t.xabsolute == 1
   assert t.yabsolute == 2

   assert t._subcommands == [ ]
   assert t.format == ''


def test_compound_hpgl_pen_01( ):
   '''pen can be int.'''
   t = _CompoundHPGL((1, 2), 1)

   assert isinstance(t.pen, Pen)
   assert t.pen.number == 1
   assert len(t._subcommands) == 1
   assert t.pen is t._subcommands[0]
   assert t.format == 'SP1;'
   

def test_compound_hpgl_pen_02( ):
   '''pen can be int.'''
   t = _CompoundHPGL((1, 2), 1)
   t.pen = 2

   assert isinstance(t.pen, Pen)
   assert t.pen.number == 2
   assert t.format == 'SP2;'
   

def test_compound_hpgl_pen_03( ):
   '''pen can be Pen.'''
   t = _CompoundHPGL((1, 2), 1)
   t.pen = Pen(2)

   assert isinstance(t.pen, Pen)
   assert t.pen.number == 2
   assert t.format == 'SP2;'
   
