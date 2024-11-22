import psycopg2
import random

conn = psycopg2.connect(database="JobsProject",
                        host="localhost",
                        user="postgres",
                        password="Usman",
                        port="5432")

conn.autocommit = True

cursor = conn.cursor()

## Adding companies to the companies table

companies = set() # holds companies already seen
categories = set()
location = set()
com_count = 1 # for id
cat_count = 1 # for id 
l_count = 1 # for id  

for line in open("jobsUS.txt", "r", encoding="UTF-8"):
    x = line.split("!!!")

    if(len(x)==13):
        if x[3] not in companies:
            s = x[3].replace(" ", "")
            z = s.replace("'", "")
            cursor.execute(
                "INSERT INTO company VALUES (%s, %s)", (com_count, s)
            )
            companies.add(x[3])
            com_count+=1

        if x[4] not in categories:
            s = x[4].replace(" ", "")
            z = s.replace("'", "")
            cursor.execute(
                "INSERT INTO category VALUES (%s, %s)", (cat_count, s)
            )
            categories.add(x[4])
            cat_count+=1
        
        z=""
        for i in range(5,9):
            if(x[i] != "n/a" and not(x[i].isnumeric())):
                x[i] = x[i].replace("'", "")
                z = z + x[i] + ","

        if z not in location:
            cursor.execute(
                "INSERT INTO location VALUES (%s, %s)", (l_count, z)
            )
            location.add(z)
            l_count+=1

for line in open("jobsCA.txt", "r", encoding="UTF-8"):
    x = line.split("!!!")

    if(len(x)==13):
        if x[3] not in companies:
            s = x[3].replace(" ", "")
            z = s.replace("'", "")
            cursor.execute(
                "INSERT INTO company VALUES (%s, %s)", (com_count, s)
            )
            companies.add(x[3])
            com_count+=1

        if x[4] not in categories:
            s = x[4].replace(" ", "")
            z = s.replace("'", "")
            cursor.execute(
                "INSERT INTO category VALUES (%s, %s)", (cat_count, s)
            )
            categories.add(x[4])
            cat_count+=1
        
        z=""
        for i in range(5,9):
            if(x[i] != "n/a" and not(x[i].isnumeric())):
                x[i] = x[i].replace("'", "")
                z = z + x[i] + ","

        if z not in location:
            cursor.execute(
                "INSERT INTO location VALUES (%s, %s)", (l_count, z)
            )
            location.add(z)
            l_count+=1

for line in open("jobsAU.txt", "r", encoding="UTF-8"):
    x = line.split("!!!")

    if(len(x)==13):
        if x[3] not in companies:
            s = x[3].replace(" ", "")
            z = s.replace("'", "")
            cursor.execute(
                "INSERT INTO company VALUES (%s, %s)", (com_count, s)
            )
            companies.add(x[3])
            com_count+=1

        if x[4] not in categories:
            s = x[4].replace(" ", "")
            z = s.replace("'", "")
            cursor.execute(
                "INSERT INTO category VALUES (%s, %s)", (cat_count, s)
            )
            categories.add(x[4])
            cat_count+=1
        
        z=""
        for i in range(5,9):
            if(x[i] != "n/a" and not(x[i].isnumeric())):
                x[i] = x[i].replace("'", "")
                z = z + x[i] + ","

        if z not in location:
            cursor.execute(
                "INSERT INTO location VALUES (%s, %s)", (l_count, z)
            )
            location.add(z)
            l_count+=1

for line in open("jobsR.txt", "r", encoding="UTF-8"):
    x = line.split("!!!")

    if(len(x)==13):
        if x[3] not in companies:
            s = x[3].replace(" ", "")
            z = s.replace("'", "")
            cursor.execute(
                "INSERT INTO company VALUES (%s, %s)", (com_count, s)
            )
            companies.add(x[3])
            com_count+=1

        if x[4] not in categories:
            s = x[4].replace(" ", "")
            z = s.replace("'", "")
            cursor.execute(
                "INSERT INTO category VALUES (%s, %s)", (cat_count, s)
            )
            categories.add(x[4])
            cat_count+=1
        
        z=""
        for i in range(5,9):
            if(x[i] != "n/a" and not(x[i].isnumeric())):
                x[i] = x[i].replace("'", "")
                z = z + x[i] + ","

        if z not in location:
            cursor.execute(
                "INSERT INTO location VALUES (%s, %s)", (l_count, z)
            )
            location.add(z)
            l_count+=1
        
print("Done adding data to companies, location and categories table!")

## ADDING JOBS

j_id=1

for line in open("jobsUS.txt", "r", encoding="UTF-8"):
    x = line.split("!!!")

    if(len(x) == 13):
        s = x[3].replace(" ", "")
        s = s.replace("'","")
        cursor.execute(f"SELECT company_id FROM company WHERE company_name='{s}'")
        for s in cursor:
            for company in s:
                com_id = company

        s = x[4].replace(" ", "")
        s = s.replace("'","")
        cursor.execute(f"SELECT category_id FROM category WHERE category_name='{s}'")
        for s in cursor:
            for company in s:
                cat_id = company

        z=""
        for i in range(5,9):
            if(x[i] != "n/a" and not(x[i].isnumeric())):
                z = z + x[i] + ","
        z = z.replace("'", "")
        cursor.execute(f"SELECT location_id FROM location WHERE area='{z}'")
        for s in cursor:
            for company in s:
                l_id = company

        min_sal = 0 if x[9]=="n/a" else float(x[9])
        max_sal = min_sal+20000
        cursor.execute(
            "INSERT INTO job VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (j_id, x[1].replace("'",""), x[2], min_sal, max_sal, x[11], com_id, cat_id, l_id)
        )
        j_id+=1

for line in open("jobsCA.txt", "r", encoding="UTF-8"):
    x = line.split("!!!")

    if(len(x) == 13):
        s = x[3].replace(" ", "")
        s = s.replace("'","")
        cursor.execute(f"SELECT company_id FROM company WHERE company_name='{s}'")
        for s in cursor:
            for company in s:
                com_id = company

        s = x[4].replace(" ", "")
        s = s.replace("'","")
        cursor.execute(f"SELECT category_id FROM category WHERE category_name='{s}'")
        for s in cursor:
            for company in s:
                cat_id = company

        z=""
        for i in range(5,9):
            if(x[i] != "n/a" and not(x[i].isnumeric())):
                z = z + x[i] + ","
        z = z.replace("'", "")
        cursor.execute(f"SELECT location_id FROM location WHERE area='{z}'")
        for s in cursor:
            for company in s:
                l_id = company

        min_sal = 0 if x[9]=="n/a" else float(x[9])
        max_sal = min_sal+20000
        cursor.execute(
            "INSERT INTO job VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (j_id, x[1].replace("'",""), x[2], min_sal, max_sal, x[11], com_id, cat_id, l_id)
        )
        j_id+=1

for line in open("jobsAU.txt", "r", encoding="UTF-8"):
    x = line.split("!!!")

    if(len(x) == 13):
        s = x[3].replace(" ", "")
        s = s.replace("'","")
        cursor.execute(f"SELECT company_id FROM company WHERE company_name='{s}'")
        for s in cursor:
            for company in s:
                com_id = company

        s = x[4].replace(" ", "")
        s = s.replace("'","")
        cursor.execute(f"SELECT category_id FROM category WHERE category_name='{s}'")
        for s in cursor:
            for company in s:
                cat_id = company

        z=""
        for i in range(5,9):
            if(x[i] != "n/a" and not(x[i].isnumeric())):
                z = z + x[i] + ","
        z = z.replace("'", "")
        cursor.execute(f"SELECT location_id FROM location WHERE area='{z}'")
        for s in cursor:
            for company in s:
                l_id = company

        min_sal = 0 if x[9]=="n/a" else float(x[9])
        max_sal = min_sal+20000
        cursor.execute(
            "INSERT INTO job VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (j_id, x[1].replace("'",""), x[2], min_sal, max_sal, x[11], com_id, cat_id, l_id)
        )
        j_id+=1

for line in open("jobsR.txt", "r", encoding="UTF-8"):
    x = line.split("!!!")

    if(len(x) == 13):
        s = x[3].replace(" ", "")
        s = s.replace("'","")
        cursor.execute(f"SELECT company_id FROM company WHERE company_name='{s}'")
        for s in cursor:
            for company in s:
                com_id = company

        s = x[4].replace(" ", "")
        s = s.replace("'","")
        cursor.execute(f"SELECT category_id FROM category WHERE category_name='{s}'")
        for s in cursor:
            for company in s:
                cat_id = company

        z=""
        for i in range(5,9):
            if(x[i] != "None" and not(x[i].isnumeric())):
                z = z + x[i] + ","
        z = z.replace("'", "")
        cursor.execute(f"SELECT location_id FROM location WHERE area='{z}'")
        for s in cursor:
            for company in s:
                l_id = company

        if(x[9]=="n/a"):
            min_sal = 0
        elif(x[9]=="None"):
            min_sal = 0
        else: 
            float(x[9])
        max_sal = min_sal+20000
        cursor.execute(
            "INSERT INTO job VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (j_id, x[1].replace("'",""), x[2], min_sal, max_sal, x[11], com_id, cat_id, l_id)
        )
        j_id+=1



print("Done Adding data to the jobs Table")

## ADDING TO PARTTIME AND FULLTIME JOBS TABLE


cursor.execute("SELECT job_id, title, description, salary_min::float as min, salary_max::float as max, contract_type, company_id, category_id, location_id FROM job WHERE contract_type='Full Time' OR contract_type='permanent'")
for s in cursor.fetchall():

    cursor.execute(
        "INSERT INTO fulltimejob VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], random.randint(30, 41))
    )

cursor.execute("SELECT job_id, title, description, salary_min::float as min, salary_max::float as max, contract_type, company_id, category_id, location_id FROM job WHERE contract_type='Part Time'")
for s in cursor.fetchall():

    cursor.execute(
        "INSERT INTO parttimejob VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], random.randint(30, 41))
    )

print("Done Adding Part/Full time jobs to table")
