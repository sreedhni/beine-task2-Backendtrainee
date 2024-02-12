def check_attendance(roll_number, total_students):
    present_roll_numbers = []

    for _ in range(total_students):
        present_roll_numbers.append(int(input("Enter roll number of present student: ")))

    if roll_number in present_roll_numbers:
        return "Present"
    else:
        return "Absent"

total_students = int(input("Enter the total number of students: "))
roll_num = int(input("Enter the roll number: "))
attendance_status = check_attendance(roll_num, total_students)
print(f"Student with roll number {roll_num} is {attendance_status}")
