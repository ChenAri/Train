# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"BMI", pos = wx.DefaultPosition, size = wx.Size( 225,187 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Height (cm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gSizer3.Add( self.m_staticText6, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Weight (kg)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_textCtrl3, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"BMI", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button6, 1, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_textCtrl4, 1, wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		self.SetSizer( gSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button6.Bind( wx.EVT_BUTTON, self.CalculateBmi )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def CalculateBmi( self, event ):
		event.Skip()
	

