import csv


def write_into_csv (info_list):
    with open ('student_info.csv', 'a' , newline=' ') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(["Name" , "Age" , "Contact number" , "Email ID" ])
        writer.writerow(info_list)


if __name__ == '__main__':
    condition = True
    student_num = 1

while (condition):
    student_info = input ("Enter student information for student #{} in the following format (Name Age Contact_Number Email ID): ". format(student_num))

    student_info_list = student_info.split( ' ' )
    print ("\nThe entered information is -\nName: {}\nAge: {}\nContact_number: {}\nE-mail ID: {} ". format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
    choice_check = input ("Is the entered information correct (yes/n0): " )

    if choice_check == "yes":
         write_into_csv(student_info_list)

         condition_check + input("enter (yes?no) if you want ti enter information for another student: ")
         if condition_check == "yes":
             conditon = True
             student_num = student_num + 1
         elif condition_check == "no":
             condition = False

    elif condition_check == "n0":
        condition = False

