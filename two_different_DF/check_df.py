
import pandas as pd


df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8]},
                  index=['falcon', 'dog', 'spider', 'fish'])


dff = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [1, 2, 1, 0]},
                  index=[1,2,3,4])



def compare_two_dfs(input_df_1, input_df_2):
    df_1, df_2 = input_df_1.copy(), input_df_2.copy()
    ne_stacked = (df_1 != df_2).stack()
    changed = ne_stacked[ne_stacked]
    changed.index.names = ['id', 'col']
    difference_locations = np.where(df_1 != df_2)

    changed_from = df_1.values[difference_locations]

    changed_to = df_2.values[difference_locations]

    df = pd.DataFrame({'from': changed_from, 'to': changed_to}, index=changed.index)
    return df
  
#calling the function directly:
compare_two_df(df,dff)
compare_two_dfs(input_df_1=df, input_df_2=dff)
#mentiond the dataframe and calling
input_df_1 = df
input_df_2 = dff
compare_two_dfs(input_df_1, input_df_2)

#output:
------------------------------
		                from	to  |
id	  col		                  |
1	 num_legs	           1 	2   |
   num_wings	         1 	2   |
   num_specimen_seen	10	1   |
3	 num_legs	           2	8   |
4	 num_specimen_seen	 8	0   |
-------------------------------

 
  
