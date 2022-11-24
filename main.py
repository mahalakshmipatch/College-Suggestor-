print("College Suggester")
print()
try:
    # List of Locations
    locations = [
        "California", "New York", "Massachusetts", "New Jersey", "Connecticut"
    ]
    
    # List of Colleges
    colleges = [
        "Stanford University", "New York University", "Columbia University",
        "Massachusetts Institute of Technology", "Harvard University",
        "Yale University", "Princeton University"
    ]
    
    # List of Majors
    majors = [
        "Computer Science", "Engineering", "Government/Political Science",
        "Business", "Medical"
    ]
    
    # List of General Grade
    grade = ["A", "B", "C", "D", "F", "E"]
    
    # List of Price Range
    priceUnder = ["70000", "60000", "45000", "30000", "20000"]
    
    # List of SAT Scores
    satMore = ["1500", "1200", "1000", "700", "500"]
    
    # List of ACT Scores
    actUnder = ["36", "30", "24", "18", "10"]
    
    #Given Values
    
    givenLocations = []
    
    givenColleges = []
    
    givenMajors = []
    
    givenGrades = []
    
    givenPrices = []
    
    givenSat = []
    
    givenAct = []
    
    collegesInfo = {
        colleges[0]: [
            locations[0], colleges[0], majors[4], grade[0], priceUnder[1],
            satMore[1], actUnder[0]
        ],
        colleges[1]: [
            locations[1], colleges[1], majors[3], grade[0], priceUnder[1],
            satMore[1], actUnder[0]
        ],
        colleges[2]: [
            locations[1], colleges[2], majors[2], grade[0], priceUnder[0],
            satMore[1], actUnder[0]
        ],
        colleges[3]: [
            locations[2], colleges[3], majors[1], grade[0], priceUnder[0],
            satMore[1], actUnder[0]
        ],
        colleges[4]: [
            locations[2], colleges[4], majors[1], grade[0], priceUnder[0],
            satMore[1], actUnder[0]
        ],
        colleges[5]: [
            locations[4], colleges[5], majors[2], grade[0], priceUnder[1],
            satMore[1], actUnder[0]
        ],
        colleges[6]: [
            locations[3], colleges[6], majors[1], grade[0], priceUnder[0],
            satMore[1], actUnder[0]
        ]
    }
    collegeSuggestion = {
        colleges[0]: 0,
        colleges[1]: 0,
        colleges[2]: 0,
        colleges[3]: 0,
        colleges[4]: 0,
        colleges[5]: 0,
        colleges[6]: 0
    }
    
    # Take input
    
    # Location
    for i in range(len(locations)):
        print(i + 1, locations[i])
    print()
    preferedLocations = list(map(int,input("Enter your options (Use commas in between, use numbers):").split(",")))
    print()
    print(preferedLocations)
    print()
    
    # # Colleges
    for i in range(len(colleges)):
        print(i + 1, colleges[i])
    print()
    preferedColleges = list(map(int,input("Enter your options (Use commas in between, use numbers):").split( ",")))
    print()
    print(preferedColleges)
    print()
    
    # # Majors
    for i in range(len(majors)):
        print(i+1,majors[i])
    print()
    preferedMajors = list(map(int,input("Enter your options (Use commas in between, use numbers):").split(",")))
    print()
    print(preferedMajors)
    print()
    
    # Grades
    for i in range(len(grade)):
        print(i+1,grade[i])
    print()
    preferedGrade = int(input("Enter your overall grade:"))
    print()
    print(preferedGrade)
    print()
    
    # Price Range
    for i in range(len(priceUnder)):
        print(i+1,priceUnder[i])
    print()
    preferedPrice = int(input("Enter your price range: "))
    print()
    print(preferedPrice)
    print()
    
    # ACT/SAT Scores
    satOract = input("Did you take the SAT or ACT, Both or None? (Type sat,act,both,none(all lowercase): ")
    print()
    if (satOract=="sat"):
        # SAT Score
        for i in range(len(satMore)):
            print(i+1,satMore[i])
        print()
        sat = int(input("Enter your SAT Score: "))
        print()
        print(sat) 
        print()
    elif(satOract=="act"):
        # ACT Scores
        for i in range(len(actUnder)):
            print(i+1,actUnder[i])
        print()
        act = int(input("Enter your ACT Score: "))
        print()
        print(act)
        print()
    elif(satOract=="both"):
        # SAT Score
        for i in range(len(satMore)):
            print(i+1,satMore[i])
        print()
        sat = int(input("Enter your SAT Score: "))
        print()
        print(sat) 
        print()
        # ACT Scores
        for i in range(len(actUnder)):
            print(i+1,actUnder[i])
        print()
        act = int(input("Enter your ACT Score: "))
        print()
        print(act)
        print()
    
    
    
    for i in range(len(colleges)):
        
        for preferedLocation in preferedLocations:
            for location in collegesInfo[colleges[i]]:
                if (locations[preferedLocation - 1] == location):
                    collegeSuggestion[colleges[i]] += 1
    
        for preferedCollege in preferedColleges:
            for college in collegesInfo[colleges[i]]:
                # print(colleges[preferedCollege-1],college)
                if (colleges[preferedCollege - 1] == college):
                    collegeSuggestion[colleges[i]] += 1
                    
        for preferedMajor in preferedMajors:
            for major in collegesInfo[colleges[i]]:
                # print(colleges[preferedCollege-1],college)
                if (majors[preferedMajor - 1] == major):
                    collegeSuggestion[colleges[i]] += 1
                    
        for grades in collegesInfo[colleges[i]]:
            # print(colleges[preferedCollege-1],college)
            if (grade[preferedGrade - 1] == grades):
                collegeSuggestion[colleges[i]] += 1
                    
        for price in collegesInfo[colleges[i]]:
            # print(colleges[preferedCollege-1],college)
            if (priceUnder[preferedPrice - 1] == price):
                collegeSuggestion[colleges[i]] += 1
                
        if(satOract=="sat" or satOract=="both"):          
            for sAt in collegesInfo[colleges[i]]:
                # print(colleges[preferedCollege-1],college)
                if (satMore[sat - 1] == sAt):
                    collegeSuggestion[colleges[i]] += 1
        elif(satOract=="act" or satOract=="both"):        
            for aCt in collegesInfo[colleges[i]]:
                # print(colleges[preferedCollege-1],college)
                if (actUnder[act - 1] == aCt):
                    collegeSuggestion[colleges[i]] += 1
    print("Below are your college suggestions in order.")
    print("The college on the top is you most prefered college and the last college is your least prefered. ")
    print()
    collegeSuggestionList = []
    for college,points in collegeSuggestion.items():
        collegeSuggestionList.append((points,college))
    collegeSuggestionList = sorted(collegeSuggestionList)
    collegeSuggestionList.reverse()
    for i in range(len(collegeSuggestionList)):
        print(i+1,collegeSuggestionList[i][1])
        
except Exception as e:
    print("Oops! An error occurred, please try again.")
    print("Please make sure to enter the correct input.")
    tryAgain = input("Enter 1 for troubleshoot.")
    if(tryAgain=="1"):
        print("We checked and found this error: ",e)
