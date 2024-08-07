import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

'1'
data = pd.read_csv('employee_promotion.csv')
data.sample(15)



'2'
data.info()

'3'
data.describe(include="object")

for column in data[['department','education','gender','recruitment_channel']]:
    print(column,'-',data[column].unique())
"""
'4'
'Rename'
df_model =data.rename(columns={'previous_year_rating':'last_year_rating'})

'''Re code'''
df_model.department =  df_model.department.map({Sales & Marketing':0, 'Operations':1,'Technology':2,'Analytics':3,
'R&D':4,'Procrurement':5,'Finance':6,'HR':7,'Legal':8})
df_model.education= df_model.education.map({“Master's & above”:0, “Bachelor's”:1,'unknown':2, 'Below Secondary':3})
df_model.gender=df_model.gender.map({'f':0, 'm':1})
df_model.recruitment_channel=df_model.recruitment_channel.map({'sourcing':0, 'other':1,'referred':2})

'''Drop data column'''
df_model_drop=df_model.drop(['employee_id','region','is_promoted'],axis=1)
#df_model_drop=df =pd.get_dummies(df_model_drop)
fig=plt.figure(figsize=(15,12),dpi=600)
ax= sns.heatmap(df_model_drop.corr(),cmap="YlGnBu",linecolor='black',lw=.65,annot=True,alpha=.95)
plt.show()

"""

