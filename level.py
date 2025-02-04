import csv

class Level():
    def __init__(self, matrix_path):
        self.matrix = []
        with open(matrix_path, newline='') as csvfile:
            spamreader =  csv.reader(csvfile, delimiter=',')
