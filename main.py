from datetime import datetime, timedelta, date
# from pprint import pprint

# {"name": "Bill Gates", 
#  "birthday": datetime(1955, 10, 28).date()}


# test_users = [{"name": str((datetime.now() + timedelta(days=i)).day), 
#                "birthday": datetime.now() + timedelta(days=i)} for i in range(-5, 10)
#             ]



def get_birthdays_per_week(users: list)->dict:
    # birthdays={
    # 'Monday': [], 
    # "Tuesday":[],
    # 'Wednesday':[],
    # "Thursday":[],
    # "Friday":[],
    # }
    birthdays={}
    for user in users:
        birs_dat = year_now(user['birthday'])
        if -1<= (birs_dat - datetime.now()).days <= 5:
            if birs_dat.strftime("%A") == 'Sunday' or  birs_dat.strftime("%A") == 'Saturday':
                if "Monday" not in birthdays:
                    birthdays["Monday"]=[]
                birthdays["Monday"].append(user['name'])  
            else:
                if birs_dat.strftime("%A") not in birthdays:
                    birthdays[birs_dat.strftime("%A")]=[]
                birthdays[birs_dat.strftime("%A")].append(user['name'])      
    return birthdays


def year_now(birthdata:datetime)->datetime:
    today = datetime.now()
    year=today.year 
    if (year%4==0 and year%100!= 0 or year%400==0) or not(birthdata.month == 2 and birthdata.day == 29): 
        carent_birthday = datetime(today.year, birthdata.month, birthdata.day)
    else:
        carent_birthday = datetime(today.year, 3,1)
    return carent_birthday


# # print(get_birthdays_per_week(test_users))
# if __name__ == "__main__":
#     users = [
#         {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
#     ]

#     result = get_birthdays_per_week(users)
#     print(result)
#     # Виводимо результат
#     for day_name, names in result.items():
#         print(f"{day_name}: {', '.join(names)}")





        # {'Monday': ['Bill', 'Jan'], 'Wednesday': ['Kim']}