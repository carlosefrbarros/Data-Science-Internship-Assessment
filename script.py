
import pandas as pd

assignees_dta = 'Patent datasets and initial task/Assignees_1975-2010.dta'
citations_dta_1 = 'Patent datasets and initial task/Citations_1975-1999.dta'
citations_dta_2 = 'Patent datasets and initial task/Citations_2000-2010 part 1.dta'
citations_dta_3 = 'Patent datasets and initial task/Citations_2000-2010 part 2.dta'
class_dta = 'Patent datasets and initial task/Class-Subclass_1975-2010.dta'
inventors_dta_1 = 'Patent datasets and initial task/Inventors_1975-2010 part 1.dta'
inventors_dta_2 = 'Patent datasets and initial task/Inventors_1975-2010 part 2.dta'
patents_dta = 'Patent datasets and initial task/Patents_1975-2010.dta'

# assignees_df = pd.read_stata(assignees_dta)
#citations_df_1 = pd.read_stata(citations_dta_1)
#citations_df_2 = pd.read_stata(citations_dta_2)
#citations_df_3 = pd.read_stata(citations_dta_3)
class_df = pd.read_stata(class_dta)
# inventors_df_1 = pd.read_stata(inventors_dta_1)
# inventors_df_2 = pd.read_stata(inventors_dta_2)
patents_df = pd.read_stata(patents_dta)
'''
print(assignees_df.shape)
print(list(assignees_df.columns))
print(citations_df_1.shape)
print(list(citations_df_1.columns))
print(citations_df_2.shape)
print(list(citations_df_2.columns))
print(citations_df_3.shape)
print(list(citations_df_3.columns))
print(class_df.shape)
print(list(class_df.columns))
print(inventors_df_1.shape)
print(list(inventors_df_1.columns))
print(inventors_df_2.shape)
print(list(inventors_df_2.columns))
print(patents_df.shape)
print(list(patents_df.columns))
'''
table_1 = pd.DataFrame(columns=['patent', 'year', '# of citations', '# of unique classes', '# of unique subclasses'])

table_1['patent'] = patents_df['patent']
table_1['year'] = patents_df['gyear']

print(table_1.head(-5))

print(class_df.head(-5))

for i, row in table_1.iterrows():
    pat = row['patent']
    row['# of unique classes'] = class_df.query('patent == @pat')['class'].sum()
    row['# of unique subclasses'] = class_df.query('patent == @pat')['subclass'].sum()
    print(row['patent'], 'classes')

table_1.to_stata('table_1.dta')

'''
n_citations = 0
    if row['year'] <= 1999:
        for i_2, row_2 in citations_df_1.iterrows():
            if row_2['patent'] == row['patent']:
                n_citations += 1
        row['# of citations'] == n_citations
        print(row['patent'], n_citations)
    else:
        for i_2, row_2 in citations_df_2.iterrows():
            if row_2['patent'] == row['patent']:
                n_citations += 1
        for i_2, row_2 in citations_df_3.iterrows:
            if row_2['patent'] == row['patent']:
                n_citations += 1
        row['# of citations'] = n_citations
        print(row['patent'], n_citations)

'''