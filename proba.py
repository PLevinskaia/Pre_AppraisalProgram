def add(self):
    self.connect = sqlite3.connect('DB.db')
    self.c = self.connect.cursor()
    self.c.execute(
        '''INSERT INTO Rubka (NameProject, pole_1, k1, n, k2, pole_3, k3, Un, nxN, costs_one, costs_N) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (name,
         self.ui.spinBox.text(),
         self.k1_func(int(self.ui.spinBox.text())),
         int(self.ui.spinBox_2.text()),
         self.k2_func(int(self.ui.spinBox_2.text())),
         self.ui.comboBox.text(),
         self.k3_func(self.ui.comboBox.text()),
         float(self.ui.lineEdit.text()),
         self.nxN_func(int(self.ui.spinBox_2.text()), N),
         self.Sone_func(self.k1_func(int(self.ui.spinBox.text())), self.k2_func(int(self.ui.spinBox_2.text())),
                        self.k3_func(self.ui.comboBox.text()), float(self.ui.lineEdit.text()),
                        int(self.ui.spinBox_2.text())),
         self.S_func(
             self.Sone_func(self.k1_func(int(self.ui.spinBox.text())), self.k2_func(int(self.ui.spinBox_2.text())),
                            self.k3_func(self.ui.comboBox.text()), float(self.ui.lineEdit.text()),
                            int(self.ui.spinBox_2.text())), N)
         ))
    self.connect.commit()