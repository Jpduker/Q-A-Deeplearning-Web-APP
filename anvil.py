from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def primary_color_1_click(self, **event_args):
    # accessing the values passed in the app
    question_text=self.question_box.text
    context_text=self.input_text.text
    # calling the uplink methon created in jupyter notebook
    result=anvil.server.call('reply',question_text,context_text)
    #setting result to be displayed in the app
    self.answer_text.text=result
  
  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass