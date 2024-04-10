import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def cal_percent(data_model: pd.DataFrame, data_test: pd.DataFrame, target: str, feature: str) -> None:
    print((data_model.groupby(target)[feature].value_counts() / data_model.groupby(target)[feature].count())*100)

def uni_stat_summary(data_model: pd.DataFrame, data_test: pd.DataFrame, column: str) -> None:
    pd.set_option('display.max_rows', None)

    counts_train =  data_model[column].value_counts()
    percentage_train = data_model[column].value_counts(normalize=True)

    counts_test =  data_test[column].value_counts()
    percentage_test = data_test[column].value_counts(normalize=True)

    print(f'----{column}----')
    print('Train data')
    print(pd.concat([counts_train, percentage_train], axis=1, keys=['Counts', 'Percentage']))
    print()
    print('Test data')
    print(pd.concat([counts_test, percentage_test], axis=1, keys=['Counts', 'Percentage']))
    print()
    print(pd.concat(
    [
        data_model[column].describe(include='all'), 
        data_test[column].describe(include='all')
    ], 
    axis=1,
    keys=['data_model', 'data_test']
    )
)
    


def uni_cat_plot(data_model: pd.DataFrame, data_test: pd.DataFrame,column: str, labels_list: list) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(12, 8), sharex=False, sharey=False)
    
    
    labels_train = []
    labels_test = []
    for i in labels_list:
        labels_train.append(f'{i} (train)')
        labels_test.append(f'{i} (test)')
    
    axes[1].pie(data_model[column].value_counts(), labels=labels_train, autopct='%1.1f%%', startangle=90, colors=['salmon', 'chocolate', 'darksalmon', 'lemonchiffon', 'steelblue'], shadow=False)
    axes[1].set_title('Train data')
    axes[2].pie(data_test[column].value_counts(), labels=labels_test, autopct='%1.1f%%', startangle=90, colors=['deeppink', 'limegreen', 'darkturquoise', 'mediumpurple', 'thistle'], shadow=False)
    axes[2].set_title('Test data')

    sns.barplot(x=data_model[column].value_counts().index, y=data_model[column].value_counts().values, color='slateblue', alpha=0.5, ax=axes[0])
    sns.barplot(x=data_test[column].value_counts().index, y=data_test[column].value_counts().values, color='palegreen', alpha=0.5, ax=axes[0])
    
    fig.legend()
    plt.show()

def uni_num_plot(data_model: pd.DataFrame, data_test: pd.DataFrame, column: str) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 8), sharex=False, sharey=False)
    
    sns.histplot(data_model[column], kde=True, color='slateblue', alpha=0.5, ax=axes[0])
    sns.histplot(data_test[column], kde=True, color='palegreen', alpha=0.5, ax=axes[0])
    
    sns.boxplot(y=data_model[column], color='slateblue', ax=axes[1])
    sns.boxplot(y=data_test[column], color='palegreen', ax=axes[1])
    
    plt.show()