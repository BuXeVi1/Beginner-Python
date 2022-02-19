#BMI ดัชนีมวลกาย
#BMI = kg / ส่วนสูง * ส่วนสูง (m)

#input
weight=int(input("ป้อนน้ำหนักของคุณ (kg) :"))
high=int(input("ป้อนส่วนสูงของคุณ (cm) : "))

#process
high=high/100           #cm => m
bmi=weight/(high*high)  #calculate bmi

#output
print("BMI = ",bmi)