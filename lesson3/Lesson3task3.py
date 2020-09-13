from pymongo import MongoClient
import lesson2 as l2t1


def main():
    df = l2t1.main()

    # инициация и подключение к монго
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['vacancy']
    docs = db.docs

    # количество новый вакансий
    count = 0
    # поиск вакансий с хх в монго, елси не найдено то вставка
    for i in range(len(df)):
        unique = df.iloc[i]['Ссылка на вакансию']
        if docs.find_one({'Ссылка на вакансию': unique}) is None:
            docs.insert_one(df.iloc[i].to_dict())
            count += 1

    print(f'Всего найдено и записано {count} новых вакансий.')
    print('\necho')
    client.close()


if __name__ == "__main__":
    main()