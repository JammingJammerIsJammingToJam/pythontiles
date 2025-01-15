from parse import *
import os
class Decoder:
  def __init__(self, filename, number):
    self.filename = filename
    self.number = number - 1
  def check_file(self):
    return os.path.isfile(self.filename)
  def file_contents(self):
    with open(self.filename) as file:
      return file.readlines()[self.number]
  def decode(self):
    if not self.check_file():
      print("ERROR FILE NOT FOUND")
      quit()
    contents = self.file_contents()
    list = []
    i = 0
    for j in range(0, 6):
      text = parse(contents, i, "/")
      list.append(text)
      i += len(text) + 1
    return list
def NME_Decode(filename, number):
  dcdr = Decoder(filename, number)
  return dcdr.decode()
