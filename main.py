import requests
import json
import requests
from base64 import b64encode

# Your API key
api_key = "3242e827-90df-4f89-8472-20d269f42b05"

# Encode the API key in the Basic Authentication format
auth_value = f"Basic {b64encode((api_key + ':').encode()).decode()}"

# Define the headers
headers = {
    "Authorization": auth_value
}

try: 
    f = open("jobsReedUK(new).txt", 'a',  encoding='utf-8')
except FileExistsError as e:
    print(f"File already exists - {e}")

try: 
    for i in range(54007584, 54060400):
        adzuna_url = f"https://www.reed.co.uk/api/1.0/jobs/{i}"  #US-1300
        response = requests.get(adzuna_url, headers=headers)
        response.encoding = 'UTF-8'
        data = response.json()

        print(i)
        
        #job-id [0]
        f.write(f"{data['jobId']}!!!")

        #title [1]
        f.write(f"{data['jobTitle']}!!!")

        #desc [2]
        f.write(f"{data['jobDescription']}!!!")  

        #company [3]
        f.write(f"{data['employerName']}!!!")  

        #category [4]
        f.write(F"{data['jobTitle']}!!!")   

        #location [5-8]
        f.write("United Kingdom!!!")
        f.write("n/a!!!")
        f.write("n/a!!!")
        f.write(f"{data['locationName']}!!!")  

        #salary-min [9]
        f.write(f"{data['minimumSalary']}!!!")

        #salary-max [10]
        f.write(f"{data['maximumSalary']}!!!")


        #contract-type[11]
        if(data['fullTime'] == True):
            f.write("Full Time")
        elif(data['partTime'] == True):
            f.write("Part Time")
        else:
            f.write(f"{data['contractType']}")
            
        #new line
        f.write("\n")

except KeyError as e:
    print(f"Missing key in response data: {e}")

try: 
    f = open("jobsadzunaAU(new).txt", 'a',  encoding='utf-8')
except FileExistsError as e:
    print(f"File already exists - {e}")
    
try:
    # Fetch data from Watchmode API
    for i in range(1696 , 2500):
        adzuna_url = f"https://api.adzuna.com/v1/api/jobs/au/search/{i+1}?app_id=aa844f73&app_key=bc0b0ed13a53941a0d385649b3597eb6&results_per_page=50"  #US-1300
        response = requests.get(adzuna_url)
        response.encoding = 'UTF-8'
        data = response.json()
        
        print(i)

        for x in data['results']:

            #job-id
            f.write(f"{x['id']}!!!")

            #title
            f.write(f"{x['title']}!!!")

            #desc
            f.write(f"{x['description']}!!!")  

            #company
            if('display_name' in x['company']):
                f.write(f"{x['company']['display_name']}!!!")  
            else:
                f.write("n/a!!!")

            #category
            f.write(F"{x['category']['label']}!!!")   

            #location
            count = 0
            for z in x['location']['area']:
                f.write(f"{z}!!!")
                count+=1
            if(count==3):
                f.write("n/a!!!")  

            #salary-min
            if('salary_min' in x):
                f.write(f"{x['salary_min']}!!!")
            else:
                f.write("n/a!!!")

            #salary-max
            if('salary_max' in x):
                f.write(f"{x['salary_max']}!!!")
            else:
                f.write("n/a!!!")

            #contract-type
            if('contract_type' in x):
                f.write(f"{x['contract_type']}")
            else:
                f.write("n/a")
            
            #new line
            f.write("\n")
            

        


except KeyError as e:
    print(f"Missing key in response data: {e}")


f.close()