class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def avg(self):
        sum_marks = 0
        for val in self.marks:
            sum_marks += val
        avg = sum_marks / len(self.marks) 
        print("MY NAME IS: ", self.name, "Avg is : ", avg)
s1 = student("Sheri", [90, 80, 60])
s1.avg()
