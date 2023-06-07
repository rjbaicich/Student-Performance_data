import pandas as pd

class Base:
    def __init__(self):
        self.df = None
        self.csv_file = r'C:\Users\RedneckRandy\Documents\GitHub\Student-Performance_data\student-por.csv'
        self.get_data()
        self.clean_data()
        
    def return_string(self):
        return self.csv_file
        
    def get_data(self):
        self.df = pd.read_csv(self.csv_file)
        return self.df
    
    def clean_data(self):
    
        #Remove duplicates
        self.df.drop_duplicates(inplace=True)
        
        #Handle missing values
        self.df.fillna(0, inplace=True)
    
        #Changing Data Types
        self.df.convert_dtypes()

if __name__ == '__main__':
    c = Base()
    print(c.return_string())
    print(c.df)
    c.df.to_csv('students_perf.csv')
