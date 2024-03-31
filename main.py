meme_dict = {
            "CRINGE": "Что-то очень странное или стыдное",
            "LOL": "Что-то очень смешное"
            }
word = input("Введите непонятное слово (большими буквами!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("there is no thing like that")
