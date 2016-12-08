import wx 
  
#import the newly created GUI file 
import BmiFrame
class CalFrame(BmiFrame.MyFrame1): 
   def __init__(self,parent): 
      BmiFrame.MyFrame1.__init__(self,parent)  
		
   def CalculateBmi(self,event): 
      height = int(self.m_textCtrl2.GetValue())
      weight = int(self.m_textCtrl3.GetValue()) 
      bmi = float(weight)/height/height*10000
      self.m_textCtrl4.SetValue (str(bmi)) 
        
app = wx.App(False) 
frame = CalFrame(None) 
frame.Show(True) 
#start the applications 
app.MainLoop() 