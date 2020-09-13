from pymongo import MongoClient
import lesson2 as l2t1
from pprint import pprint


def main():
    df = l2t1.main()
    print(df)

    client = MongoClient('mongodb://90.154.71.215:32')
    db = client['vacancy']
    docs = db.docs

    for i in range(len(df)):
        result = docs.insert_one(df.iloc[i].to_dict())
        print(f'New doc: {result.inserted_id}')
    phil_doc = docs.find_one({'Сайт': 'SuperJob'})
    pprint(phil_doc)

    client.close()


if __name__ == "__main__":
    main()