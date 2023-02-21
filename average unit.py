#โปรแกรมเฉลี่ยหน่วยการใช้ไฟฟ้า

from tkinter import*
from typing import Collection

def show():
    month=Label(root,text=f"เริ่มการแก้ไขบิลเดือน {clicked.get()}").grid(row=6, columnspan=2)

def select_method ():
    s=solution.get()
    if s== "On1":
        month=Label(root,text=f"เริ่มการแก้ไขบิลเดือน {clicked.get()}").grid(row=7, columnspan=2)
        a=Label(root,text="เฉลี่ยหน่วย 3 เดือน").grid(row=8, columnspan=2)
        #method()
    elif s=="M2" :
        month=Label(root,text=f"เริ่มการแก้ไขบิลเดือน {clicked.get()}").grid(row=7, columnspan=2)
        Label(root,text="โดย การเฉลี่ยจากมิเตอร์เครื่องใหม่").grid(row=8, columnspan=2)


def submit(a1,a2,a3,amount_day):
    c=str(clicked.get())
    o=m.index(c)
    sum_unit_3m=a1+a2+a3
    average3M=sum_unit_3m/amount_day
    Label(root, text=f"รวมหน่วย 3 เดือน เท่ากับ {sum_unit_3m}").grid(column=0)
    Label(root, text=f"รวมจำนวนวัน 3 เดือน เท่ากับ {amount_day}").grid(column=1)
    Label(root, text=f"เฉลี่ย ได้ {sum_unit_3m} / {amount_day}  = {average3M} หน่วย/วัน").grid(columnspan=2)
    Label(root, text=f"ดังนั้น เดือน {m[o]} ใช้ไฟเฉลี่ย {average3M} x {day[o]}  = {int(average3M)*int(day[o])} หน่วย").grid(columnspan=2)

# ฟังก์ชันรับค่าเฉลี่ย 3 เดือน
def method ():
    m=["มกราคม","กุมภาพันธ์","มีนาคม","เมษายน","พฤษภาคม","มิถุนายน",
    "กรกฎาคม","สิงหาคม","กันยายน","ตุลาคม","พฤศจิกายน","ธันวาคม"]
    day=[31,28,31,30,31,30,31,31,30,31,30,31]
    s=solution.get()
    c=str(clicked.get())
    o=m.index(c)
    amount_day=0
    # วนลูปเก็บจำนวนวันที่นำมาเฉลี่ย
    for i in range(3):
        #Label(root,text = f"เดือน {m[o-i]} จำนวนวัน = {day[o-i]}").grid()
    
        amount_day+=day[o-i]
    
    
    # month Lable
    a1_Label=Label(root,text=f"ใส่หน่วย เดือน {m[o-3]}").grid(row=9, column=0)
    a2_Label=Label(root,text=f"ใส่หน่วย เดือน {m[o-2]}").grid(row=10, column=0)
    a3_Label=Label(root,text=f"ใส่หน่วย เดือน {m[o-1]}").grid(row=11, column=0)
    
    #Entry
    a1_ent=IntVar()
    a2_ent=IntVar()
    a3_ent=IntVar()
    a1_ent=Entry(root,text=f"ใส่หน่วย เดือน {m[o-3]}").grid(row=9, column=1)
    a2_ent=Entry(root,text=f"ใส่หน่วย เดือน {m[o-2]}").grid(row=10, column=1)
    a3_ent=Entry(root,text=f"ใส่หน่วย เดือน {m[o-1]}").grid(row=11, column=1)
    Button(root, text="เฉลี่ย").grid()
    Label(root, text= f"รวมหน่วย = {a1_ent+a2_ent+a3_ent}").grid()
    #c(a1_ent, a2_ent, a3_ent)
    #sum_unit_3m=int(a1_Label)+int(a2_Label)+int(a3_Label)
    #submit_btn=Button(root,text="submit",command=submit(a1_ent,a2_ent,a3_ent,amount_day)).grid(row=13, column=1)
    '''
    sum_unit_3m=int(a1_Label)+int(a2_Label)+int(a3_Label)
    average3M=sum_unit_3m/amount_day
    Label(root, text=f"รวมหน่วย 3 เดือน เท่ากับ {sum_unit_3m}").grid(column=0)
    Label(root, text=f"รวมจำนวนวัน 3 เดือน เท่ากับ {amount_day}").grid(column=1)
    Label(root, text=f"เฉลี่ย ได้ {sum_unit_3m} / {amount_day}  = {average3M} หน่วย/วัน").grid(columnspan=2)
    Label(root, text=f"ดังนั้น เดือน {m[o]} ใช้ไฟเฉลี่ย {average3M} x {day[o]}  = {int(average3M)*int(day[o])} หน่วย").grid(columnspan=2)
    '''
def c(a1,a2,a3):
    Label(root, text="พร้อม").grid()
root=Tk()
#root.minsize(width=400, height=400)

m=["มกราคม","กุมภาพันธ์","มีนาคม","เมษายน","พฤษภาคม","มิถุนายน",
    "กรกฎาคม","สิงหาคม","กันยายน","ตุลาคม","พฤศจิกายน","ธันวาคม"]
day=[31,28,31,30,31,30,31,31,30,31,30,31]
# สร้าง drop downlist ให้เลือกเดือนแก้ไขบิล
clicked= StringVar()
clicked.set("ระบุเดิอน")
drop=OptionMenu(root,clicked,*m).grid(row=0, columnspan=2)
#Button(root,text="Select",command=show).pack()

# สร้าง Checkbox ให้เลือกวิธีการเฉลี่ยหน่วย
Label(root,text="เลิอกวิธีการเฉลี่ยหน่วย").grid(row=1, column=0)
solution= StringVar()
mean3m= Checkbutton(root,text="เฉลี่ยหน่วย 3 เดือน",variable=solution, onvalue="On1")
mean3m.deselect()
mean3m.grid(row=2, column=0)

new_meter=Checkbutton(root, text="เฉลี่ยหน่วยจากมิเตอร์เครื่องใหม่", variable=solution, onvalue="M2")
new_meter.deselect()
new_meter.grid(row=3, column=0)

select_method=Button(root,text="ยืนยัน",command=select_method).grid(row=4, columnspan=2)

# วิธีการเฉลี่ย

Button(root, text="start",command=method).grid(row=5, columnspan=2)

#ปุ่มสั่งให้คำนวนค่า





root.mainloop()