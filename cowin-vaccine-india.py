import time as t
from cowin_api import CoWinAPI
from datetime import *
from gtts import gTTS
import os
today = date.today()
d1 = today.strftime("%d-%m-%Y")
print("d1 =", d1)
presentday = datetime.now()  # or presentday = datetime.today()
yesterday = presentday - timedelta(1)
tomorrow = presentday + timedelta(1)
date_after_tommorrow = presentday + timedelta(2)
pre=presentday.strftime('%d-%m-%Y')
tom=tomorrow.strftime('%d-%m-%Y')
tomm=date_after_tommorrow.strftime('%d-%m-%Y')
print(pre)
print(tomm)
print(tom)
def cowin_vacc(date):
    cowin = CoWinAPI()
    states = cowin.get_states()
    sta_count = len(states['states'])
    StateName = "Jharkhand"  # Change State Name
    DistrictName = "East Singhbhum"  # Change District Name  # Change date as per your convenience
    min_age_limit = 18  # By default returns centers without filtering by min_age_limit
    '''for i in range(sta_count):
        print("State name:", states['states'][i]['state_name'],"---State ID:",states['states'][i]['state_id'])'''
    for i in range(sta_count):
        if StateName == states['states'][i]['state_name']:
            print("-----------State Selected----------------")
            state_id = str(states['states'][i]['state_id'])
            print("State number :", state_id, "State Name:", StateName, "")
            print("-------------------------------------------------------------------")
    districts = cowin.get_districts(state_id)
    dis_count = len(districts['districts'])
    '''for i in range(dis_count):
        print("Districts name:", districts['districts'][i]['district_name'],"District ID:", districts['districts'][i]['district_id'])'''
    for i in range(dis_count):
        if DistrictName == districts['districts'][i]['district_name']:
            print("--------------------District Selected-------------------------")
            print("District Number :", districts['districts'][i]['district_id'], "District Name:", DistrictName)
            district_id = str(districts['districts'][i]['district_id'])
            print("-------------------------------------------------------------------")
    available_centers = cowin.get_availability_by_district(district_id, date, min_age_limit)
    total_centers = len(available_centers['centers'])
    y = 0
    print("Date Selected:- ", date )
    for i in range(total_centers):
        x = available_centers['centers'][i]
        total_session = len(x['sessions'])
        for count in range(total_session):
            available_capacity = available_centers['centers'][i]['sessions'][count]['available_capacity']
            if available_capacity > 0:
                y = +1
                results = available_centers['centers'][i]
                print("--------Oh Yeah , You Found a Slot, Quickly get Vaccinated --------\n")
                print("Name:", results['name'], "Address:", results['address'], "Minimum Age:",
                      results['sessions'][count]['min_age_limit'], "Available Slots:",
                      results['sessions'][count]['available_capacity'])
                print("-------------------------------------------------------------------\n")
            else:
                results = available_centers['centers'][i]
                print("Name:", results['name'], "Address:", results['address'], "Minimum Age:",
                      results['sessions'][count]['min_age_limit'], "Available Slots:",
                      results['sessions'][count]['available_capacity'])
    if y == 0:
        mytext = "No Vaccination Center found for {} for age {} ".format(date , min_age_limit)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save('NoVaccinationCenterFound.mp3')
        t.sleep(5)
        print("-------------------------------------------------------------------\n")
        print("No Vaccination Center found")
        print("-------------------------------------------------------------------\n")
        os.system('NoVaccinationCenterFound.mp3')
    else:
        mytext = "Alert! Alert! , We Found a vaccination Slot for {} year on {}".format(min_age_limit,date)
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save(y, "Vaccination Center Found.mp3")
        t.sleep(5)
        print("Good News! We found", y, "Vaccination Center. Please get Vaccinated quickly")
        os.system("Vaccination Center Found.mp3")
cowin_vacc(pre)
t.sleep(10)
cowin_vacc(tom)
t.sleep(10)
cowin_vacc(tomm)