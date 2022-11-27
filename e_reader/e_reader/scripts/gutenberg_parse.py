import csv

book_data = open("pg-catalog-csv.csv")
reader = csv.reader(book_data)

print("CSV Loaded.")

for row in reader:
    print("gut_id = ", row[0])
    print("gut_type = ", row[1])
    print("gut_date = ", row[2])
    print("title = ", row[3])
    print("language = ", row[4])
    author = row[5].split(";")
    author_count = len(author)
    for x in range(author_count):
        individual = author[x].split(",")
        print("author_last_name = ", individual[0])
        if len(individual) > 1:
            print("author_first_name = ", individual[1])

        if "Jr." or "Sir" in author[x]:
            print("Jr.")
            if len(individual) > 3:
                dates = individual[3].split("-")
                print("author_born = ", dates[0])
                if len(dates) > 1:
                    if "[" in dates[1]:
                        print("author_died = ", dates[1][:4])
                        print("author_role = ", dates[1][6:int(len(dates[1])-1)])
                    else:
                        print("author_died = ", dates[1])
            if len(individual) > 4:
                print("author_role = ", individual[4])

        if len(individual) > 2:
            dates = individual[2].split("-")
            print("author_born = ", dates[0])
            if len(dates) > 1:
                if "[" in dates[1]:
                    print("author_died = ", dates[1][:4])
                    print("author_role = ", dates[1][6:int(len(dates[1])-1)])
                else:
                    print("author_died = ", dates[1])
        if len(individual) > 3:
            print("author_role = ", individual[3])
    # print ("author = ", author)


