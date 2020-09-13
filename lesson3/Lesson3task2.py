from pymongo import MongoClient
from pprint import pprint


def main():
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['vacancy']
    docs = db.docs

    salary_min = input('Введите минимальную ЗП: ')
    try:
        salary_min = int(salary_min)
        print(f'Ищем в БД вакансию с ЗП не меньше {salary_min}')
    except ValueError:
        print(f'Вы ввели не цифру - {salary_min}.')
        raise SystemExit(1)

    for post in docs.find({"Зарплата.0": {'$gt': salary_min}}):
        pprint(post)

    print('\necho')
    client.close()


if __name__ == "__main__":
    main()