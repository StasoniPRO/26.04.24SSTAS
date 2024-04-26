# import pandas packagess
import pandas as pd

#Define a dictionary containing employee data
data = {'Name': ['Jal', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Addess':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']
        }
#Convert the dictionary into DataFrame
df = pd.DataFrame(data)

#Loc. DataFrame method
#Filtering rows and selecting columns by label format
#df.loc[rows, columns]
#row 1, all columns
print(df.loc[0,:])