from datetime import datetime
from datetime import timedelta

users = [
        {"name":"Bill", "birthday":datetime(1995,6,30)},
        {"name":"Stiv", "birthday":datetime(1990,6,26)},
        {"name":"Jill", "birthday":datetime(1990,6,28)},
        {"name":"John", "birthday":datetime(1998,6,28)},
        {"name":"Evgen", "birthday":datetime(1992,6,30)},
        {"name":"Jack", "birthday":datetime(1980,7,1)},
        {"name":"Ann", "birthday":datetime(1964,7,1)},
        {"name":"Helen", "birthday":datetime(1999,7,1)},
        {"name":"Max", "birthday":datetime(1991,7,2)},
        {"name":"Jax", "birthday":datetime(1999,7,2)},
        {"name":"Piter", "birthday":datetime(1984,7,1)},
        {"name":"Charles", "birthday":datetime(1984,6,1)},
        {"name":"German", "birthday":datetime(1981,7,1)},
        {"name":"Aaron", "birthday":datetime(1992,6,29)},
        {"name":"Alex", "birthday":datetime(1993,6,30)},
        {"name":"Alice", "birthday":datetime(1998,6,29)},
        {"name":"Andy", "birthday":datetime(1997,6,30)},
        {"name":"Bert", "birthday":datetime(1994,6,30)},
        {"name":"Bruno", "birthday":datetime(1992,6,28)},
        {"name":"Joan", "birthday":datetime(1987,6,28)},
        {"name":"Kent", "birthday":datetime(1959,6,26)},
        {"name":"Kate", "birthday":datetime(1978,6,26)},
        {"name":"Karen", "birthday":datetime(1968,6,26)},
        {"name":"Logan", "birthday":datetime(1988,6,24)}
]

# =======================================
# Функція формує/друкує словник осіб які відмічають День народження +7 днів
# =======================================
def get_birthdays_per_week(users:dict)->dict:
    
    dct = {"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[], "Saturday":[], "Sunday":[]}
    now_date = datetime.now() # дата сьогодні
    end_date = datetime.now() + timedelta(days=7)  # кінцева дата == +7 днів
    
    for person in users:
        person_month = person["birthday"].month 
        person_day = person["birthday"].day 
        # рік народження змінемо на рік який зараз
        dt = datetime(now_date.year, person_month, person_day) # день.місяць.ТЕКУЩИЙ РІК  <- для особи
        
        # відбираємо людей у яких Д.Н. буде on next week
        # now_date = дата ЗАРАЗ
        # end_date = дата ЗАРАЗ + 7 днів
        if dt.date() > now_date.date() and dt.date() <= end_date.date():
            if dt.strftime("%A") in ["Saturday", "Sunday"]:
                match dt.strftime("%A"):
                    case "Saturday": dt = dt.date() + timedelta(days=2)
                    case  "Sunday": dt = dt.date() + timedelta(days=1)
                    
                # якщо виходимо за межі 7 днів
                if dt > end_date.date(): # відпрац. людей у яких Д.Н. у суб, неділю. але вони виходять за межі +7 днів
                    try:
                        dct["next_Monday"].append(person["name"])
                    except KeyError:
                        dct["next_Monday"] = []
                        dct["next_Monday"].append(person["name"])
                else:        
                    dct["Monday"].append(person["name"]) # вітаємо у Понеділок
            else:    
                dct[dt.strftime("%A")].append(person["name"])
            
    # друкуємо результати роботи
    print_birthday_man(dct)


# =======================================
# Функція друкує людей
# які святкують Д.Н. впродовж неділі
# =======================================
def print_birthday_man(birthdays:dict):
    for week_day, value in birthdays.items():
        if len(value) > 0:
            s = ", ".join(value)
            print(f"{week_day}: {s}")
    

def main():
    get_birthdays_per_week(users)
    

if __name__ == "__main__":
    main()
