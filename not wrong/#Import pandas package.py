#Import pandas package
import pandas as pd

#Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
'Age':[127, 24, 22, 32],
'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
'Qualification':['Mac', 'MA', 'MCA', 'Phd']}

#Convert the dictionary into DataFrame
df = pd.DataFrame(data)
#select three rows and two columns print/df.loc[1:3, ['Name', 'Qualification'])
print(df.loc[1:3,['Name', 'Qualification']])
