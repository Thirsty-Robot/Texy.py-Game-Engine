from texy import Texy_event

def text_white():
  print (Texy_event.text("Hello I'm normal text"))
  
def text_alert():
  print (Texy_event.alert("Hello I'm an alert"))
  
def text_notification():
  print (Texy_event.notification("Hello I'm a notification"))
  
def text_emphasis():
  print (Texy_event.emphasis("Hello I'm a text with emphasis"))
  
  
def text_dim():
  print (Texy_event.dim("I'm just dim text"))
 
text_white()
text_alert()
text_notification()
text_emphasis()
text_dim()
