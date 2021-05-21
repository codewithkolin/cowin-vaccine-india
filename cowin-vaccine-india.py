from cowin_api import CoWinAPI
cowin = CoWinAPI()
states = cowin.get_states()
sta_count=len(states['states'])
StateName="Jharkhand"                   #Change State Name
DistrictName="East Singhbhum"           #Change District Name
date = '22-05-2021'                     # Change date as per your convenience
min_age_limit = 0                      #By default returns centers without filtering by min_age_limit
for i in range(sta_count):
    print("State name:", states['states'][i]['state_name'],"---State ID:",states['states'][i]['state_id'])
for i in range(sta_count):
    if StateName == states['states'][i]['state_name']:
        print("-----------State Selected----------------\n")
        state_id = str(states['states'][i]['state_id'])
        print("State number :", state_id , "State Name:", StateName,"\n" )
        print("-------------------------------------------------------------------\n")
districts = cowin.get_districts(state_id)
dis_count=len(districts['districts'])
for i in range(dis_count):
    print("Districts name:", districts['districts'][i]['district_name'],"District ID:", districts['districts'][i]['district_id'])
for i in range(dis_count):
    if DistrictName == districts['districts'][i]['district_name']:
        print("--------------------District Selected-------------------------\n")
        print("District Number :", districts['districts'][i]['district_id'],"District Name:", DistrictName ,"\n")
        district_id = str(districts['districts'][i]['district_id'])
        print("-------------------------------------------------------------------\n")
available_centers = cowin.get_availability_by_district(district_id, date, min_age_limit)
total_centers=len(available_centers['centers'])
y=0
for i in range(total_centers):
    x=available_centers['centers'][i]
    total_session = len(x['sessions'])
    for count in range(total_session):
        available_capacity=available_centers['centers'][i]['sessions'][count]['available_capacity']
        if available_capacity > 0:
            y=+1
            results =available_centers['centers'][i]
            print("--------Oh Yeah , You Found a Slot, Quickly get Vaccinated --------\n")
            print("Name:",results['name'],"Address:" ,results['address'],"Minimum Age:" , results['sessions'][count]['min_age_limit'],"Available Slots:" , results['sessions'][count]['available_capacity'])
            print("-------------------------------------------------------------------\n")
if y==0:
    print("No Vaccination Center found")
else:
    print("Good News! We found",y,"Vaccination Center. Please get Vaccinated quickly")