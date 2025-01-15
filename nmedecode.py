from parse import *
import os
class Decoder:
  def __init__(self, filename):
    self.filename = filename
  def num(self, number):
    self.number = number
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
def NME_Decode_Line(filename, number):
  dcdr = Decoder(filename)
  dcdr.num(number)
  return dcdr.decode()
def NME_Decode_File(filename):
  kale = Decoder(filename)
  if not kale.check_file():
    print("ERROR FILE NOT FOUND")
    quit()
  file = open(filename, "r")
  length = len(file.readlines())
  file.close()
  lists = []
  for i in range(0, length):
    lists.append(NME_Decode_Line(filename, i))
  return lists
