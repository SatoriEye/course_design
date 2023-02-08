lineEdit.textEdited[str].connect(lambda :self.onChange())
   def onChange(self):
        facename = self.lineEdit.text()
        print("...",facename)