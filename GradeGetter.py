#brandon robbins
#12/18
#AVG GRADES

gradelist=[]
def getGrade(gradelist):

    while True:
        maxGrade=100
        grade =input("enter in a grade or to exit press space bar")
        if grade == " ":
            break
        elif grade.isdigit():
            grade = float(grade)
            if grade<= maxGrade:
                gradelist.append(grade)
            else:
                q= input("are you sure this "+str(grade)+" is a good grade y or n")
                if q=="y":
                    gradelist.append(grade)
                else:
                    print("Thats not a good grade")
        else:
            print("Thats not a good grade")

def avgfunction(gradelist):
    total=0
    for grade in gradelist:
        total += grade
    avg = total / len(gradelist)
    return avg

def main(gradelist):
    getGrade(gradelist)
    avg = avgfunction(gradelist)
    print("your grade is ",avg)
main(gradelist)
