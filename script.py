
import pandas as pd

citations_dta_1 = 'Patent datasets and initial task/Citations_1975-1999.dta'
citations_dta_2 = 'Patent datasets and initial task/Citations_2000-2010 part 1.dta'
citations_dta_3 = 'Patent datasets and initial task/Citations_2000-2010 part 2.dta'
class_dta = 'Patent datasets and initial task/Class-Subclass_1975-2010.dta'
patents_dta = 'Patent datasets and initial task/Patents_1975-2010.dta'

citations_df_1 = pd.read_stata(citations_dta_1)
citations_df_2 = pd.read_stata(citations_dta_2)
citations_df_3 = pd.read_stata(citations_dta_3)
class_df = pd.read_stata(class_dta)
patents_df = pd.read_stata(patents_dta)

table_1 = pd.DataFrame(columns=['patent', 'year', 'n_of_citations', 'n_of_unique_classes', 'n_of_unique_subclasses'])

table_1['patent'] = patents_df['patent']
table_1['year'] = patents_df['gyear']

table_1['n_of_citations'] = (table_1['patent'].map(citations_df_1['patent'].value_counts()) +
                             table_1['patent'].map(citations_df_2['patent'].value_counts()) +
                             table_1['patent'].map(citations_df_3['patent'].value_counts()))
print('citations')
table_1['n_of_unique_classes'] = table_1['patent'].map(class_df.groupby('patent')['class'].sum())
print('classes')
table_1['n_of_unique_subclasses'] = table_1['patent'].map(class_df.groupby('patent')['subclass'].sum())
print('subclasses')

print(table_1.shape)
print(table_1.head(-5))

table_1.to_stata('table_1.dta', version=117)
