import csv
from .models import *

def run():

    book_data = open("pg-catalog-csv.csv")
    reader = csv.reader(book_data)

    # print("CSV Loaded.")

    for row in reader:
        g_id, created = Book.objects.get_or_create(gut_id = row[0])
        t_id, created = Gutenberg_Type.objects.get_or_create(gut_type = row[1])
        d, created = Book.objects.get_or_create(gut_issued = row[2])
        t, created = Book.objects.get_or_create(title = row[3])
        #print("language = ", row[4])
        author = row[5].split(";")
        author_count = len(author)
        
        for x in range(author_count):
            individual = author[x].split(",")
            a_ln, created = Author.objects.get_or_create(last_name = individual[0])
            if len(individual) > 1:
                a_fn, created = Author.objects.get_or_creat(first_name = individual[1])

            if "Jr." or "Sir" in author[x]:
                #print("Jr.")
                if len(individual) > 3:
                    dates = individual[3].split("-")
                    bd, created = Author.objects.get_or_create(dob = dates[0])
                    if len(dates) > 1:
                        if "[" in dates[1]:
                            dd, created = Author.objects.get_or_create(dod = dates[1][:4])
                            r, created = Author_Role.objects.get_or_create(role = dates[1][6:int(len(dates[1])-1)])
                        else:
                            dd, created = Author.objects.get_or_create(dod = dates[1])
                if len(individual) > 4:
                    r, created = Author_Role.objects.get_or_create(role = individual[4])

            if len(individual) > 2:
                dates = individual[2].split("-")
                bd, created = Author.objects.get_or_create(dob = dates[0])
                if len(dates) > 1:
                    if "[" in dates[1]:
                        dd, created = Author.objects.get_or_create(dod = dates[1][:4])
                        r, created = Author_Role.objects.get_or_create(role = dates[1][6:int(len(dates[1])-1)])
                    else:
                        dd, created = Author.objects.get_or_create(dod = dates[1])
            if len(individual) > 3:
                r, created = Author_Role.objects.get_or_create(role = individual[3])
        # print ("author = ", author)
        for x in range(3):
            col = x + 6
            if len(row[col]) > 0:
                sub, created = Subject.objects.get_or_create(subject = row[col])
