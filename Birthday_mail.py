import datetime as dt
import pandas as pd
import smtplib
import random

today_time = dt.datetime.now()
today_month = today_time.month
today_day = today_time.day

################## VERIFYNG THE DATES / CSV WORK ##################
csv_data = pd.read_csv("birthdays.csv")

only_mom = csv_data[csv_data.name == "Mama"]
only_dad = csv_data[csv_data.name == "Tata"]

the_receiver = " "

if (only_mom.month == today_month).any() and (only_mom.day == today_day).any():
    the_receiver = str(only_mom["name"].values[0])
    print(type(the_receiver))

elif(only_dad.month == today_month).any() and (only_dad.day == today_day).any():
    the_receiver = str(only_dad["name"].values[0])

else:
    pass


first_letter = "letter_1.txt"
second_letter = "letter_2.txt"
third_letter = "letter_3.txt"
letter_list = [first_letter, second_letter, third_letter]

final_list = []


random.seed()
random_letter = random.choice(letter_list)


with open(f"./letter_templates/{random_letter}", 'r') as random_letter1:
    letter = random_letter1.read()
    new_letter = letter.replace("[NAME]", the_receiver)
    with open(f"./finished_letters/{random_letter}", 'w') as random_letter2:
        random_letter2.write(new_letter)
        print(new_letter)




my_email = "caramaniulian@mail.ru"
second_email = "caramaniulian15@gmail.com"
password = "f1mxiteNRAardNHnQJuz"

with smtplib.SMTP("smtp.mail.ru") as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(from_addr=my_email, to_addrs=second_email, msg=f"Subject:Happy birthday!\n\n{new_letter}")
