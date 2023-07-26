import numpy as np
import pandas as pd
import re

db = pd.read_csv("animefile.csv")

db = db.drop_duplicates()

meann = np.mean(db['score'])

db['score'] = db['score'].fillna(meann)

anime = db.copy()

for index,row in db.iterrows():
    order = row['genre'].translate({ord('['):None})
    order = order.translate({ord(']'):None})
    order = order.translate({ord("'"):None})
    listrow = list(order.split(','))
#     print(listrow)
    for genre in listrow:
        genre = genre.translate({ord(" "):None})
        anime.at[index,genre] = int(1)
        
anime = anime.fillna(0)

def predict(x):
    title = x

    df = anime[anime['title'] == title]

    df = df.drop(['uid','title','synopsis','genre','aired','episodes','members','popularity','ranked','score','link','img_url'],axis = 1)

    userinput = df.to_numpy()
    weightmatrix = 5*userinput
    summ = np.sum(weightmatrix)
    weightmatrix = weightmatrix/summ
    process = anime.drop_duplicates()
    example = process.copy()
    process = process.drop(['uid','title','synopsis','genre','aired','episodes','members','popularity','ranked','score','link','img_url'],axis = 1)
    processmatrix = process.to_numpy()

    weightmatrix = weightmatrix.reshape(44,1)

    overview = np.matmul(processmatrix,weightmatrix)

    overview = overview * 5

    example['rating'] = overview

    example['finalrating'] = example['rating'] * example['score']

    example = example[example['title'] != title]
    sorted_df = example.sort_values(by=['finalrating'], ascending=False)
    recommandation = []
    
    for index,row in sorted_df.head(6).iterrows():
        recommandation.append(row)
        
    return recommandation


# x = input("Enter the correct anime name = ")
# listt = predict(x)

# for i in listt:
#     print(i['title'])
#     print(i['synopsis'])
#     print("\n")