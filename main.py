import requests
import json
try: 
    f = open("jobsadzunaUS.txt", 'x',  encoding='utf-8')
except FileExistsError as e:
    print(f"File already exists - {e}")
    
try:
    # Fetch data from Watchmode API
    for i in range(0, 2500):
        adzuna_url = f"https://api.adzuna.com/v1/api/jobs/us/search/{i+1}?app_id=aa844f73&app_key=bc0b0ed13a53941a0d385649b3597eb6&results_per_page=50"  #US-1300
        response = requests.get(adzuna_url)
        response.encoding = 'UTF-8'
        data = response.json()
        
        print(i)

        for x in data['results']:

            #title
            f.write(f"{x['title']}!!!")

            #desc
            f.write(f"{x['description']}!!!")  

            #company
            f.write(f"{x['company']['display_name']}!!!")  

            #category
            f.write(F"{x['category']['label']}!!!")   

            #location
            count = 0
            for z in x['location']['area']:
                f.write(f"{z}!!!")
                count+=1
            if(count==3):
                f.write("n/a!!!")  

            #salary
            if('salary_min' in x):
                f.write(f"{x['salary_min']}!!!")
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