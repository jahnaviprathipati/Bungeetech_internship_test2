import pandas as pd


# 1 done

ques1_data = pd.read_csv('./input/question-1/main.csv')

ques_data = ques1_data

ques1_data.drop(columns='Total', inplace=True)
ques1_data['Year'] = (10 * (ques1_data['Year'] // 10))
ques1_data = ques1_data.groupby('Year').sum()

ques1_data.to_csv('./output/answer-1/main.csv')


# 2 done

ques2_data = pd.read_csv('./input/question-2/main.csv')

ques2_data = ques2_data.groupby('occupation').agg({'age': ['min', 'max']})
ques2_data.to_csv('./output/answer-2/main.csv')


# 3 done 

ques3_data = pd.read_csv('./input/question-3/main.csv')
ques3_data = ques3_data[['Team', 'Yellow Cards', 'Red Cards']]

ques3_data = ques3_data.groupby('Team').sum()
ques3_data = ques3_data.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)
ques3_data.to_csv('./output/answer-3/main.csv')