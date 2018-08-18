from Tkinter import *
import Tkinter
import tkMessageBox



import psycopg2
import xlrd
import time

# book = xlrd.open_workbook("datbase.xlsx")
# sheet = book.sheet_by_name("Scores as of March 2018")

database = psycopg2.connect (database = "latlong", user="postgres", password="123456", host="localhost", port="5082")

cursor = database.cursor()
status = 2




def q1(text,root,text1):
	print(status)
	text.delete(1.0, END)
	if status==2:
		query = """SELECT * FROM testing2 WHERE country='Tooele'"""
	elif status==3:
		query = """SELECT * FROM testing3 WHERE country='Tooele'"""
	else:
		query = """SELECT * FROM testing4 WHERE country='Tooele'"""
	start_time = time.time()
	cursor.execute(query)
	cursor.fetchall()
	end_time = time.time()
	total_time = end_time - start_time
	text.insert(1.0,total_time)
	text.insert(1.0, "   ")
	text.insert(1.0,"For SELECT data")
	text1.insert(1.0,total_time)
	text1.insert(1.0, "   ")
	text1.insert(1.0,"For SELECT data")
	text1.insert(1.0,"\n")


def q2(text,root,text1):
	text.delete(1.0, END)
	if status==2:
		query = """UPDATE testing2 SET first_name = 'FLASH' WHERE age = '29'"""
	elif status==3:
		query = """UPDATE testing3 SET first_name = 'FLASH' WHERE age = '29'"""
	else:
		query = """UPDATE testing4 SET first_name = 'FLASH' WHERE age = '29'"""
	start_time = time.time()
	cursor.execute(query)
	database.commit()
	end_time = time.time()
	total_time = end_time - start_time
	text.insert(1.0,total_time)
	text.insert(1.0, "   ")
	text.insert(1.0,"For UPDATE data")
	text1.insert(1.0,total_time)
	text1.insert(1.0, "   ")
	text1.insert(1.0,"For UPDATE data")
	text1.insert(1.0,"\n")

def q3(text,root,text1):
	text.delete(1.0, END)
	if status==2:
		query = """INSERT INTO testing2 (first_name, last_name, age, country, zip, lat, long) VALUES ('Tom B.', 'Erichsen', '50', 'Stavanger', '19265','26.19755983', '-97.6901975')"""
	elif status==3:
		query = """INSERT INTO testing3 (first_name, last_name, age, country, zip, lat, long) VALUES ('Tom B.', 'Erichsen', '50', 'Stavanger', '19265','26.19755983', '-97.6901975')"""
	else:
		query = """INSERT INTO testing4 (first_name, last_name, age, country, zip, lat, long) VALUES ('Tom B.', 'Erichsen', '50', 'Stavanger', '19265','26.19755983', '-97.6901975')"""
	start_time = time.time()
	cursor.execute(query)
	database.commit()
	end_time = time.time()
	total_time = end_time - start_time
	text.insert(1.0,total_time)
	text.insert(1.0, "   ")
	text.insert(1.0,"For INSERT data")
	text1.insert(1.0,total_time)
	text1.insert(1.0, "   ")
	text1.insert(1.0,"For INSERT data")
	text1.insert(1.0,"\n")

def q10(text,root,text1,button10,button11,button12,button1,button2,button3,text2):
	query0 = """DROP TABLE IF EXISTS testing2"""
	query1 = """CREATE TABLE testing2(
	 first_name VARCHAR (50),
	 last_name VARCHAR (50),
	 age VARCHAR (50),
	 country  VARCHAR (50),
	 zip VARCHAR (50),
	 lat VARCHAR (50),
	 long VARCHAR (50)
	)"""

	query2 = """COPY testing2 FROM 'C:/Users/HP/Desktop/python/datbase.csv' WITH DELIMITER AS ',' """
	a = cursor.execute(query0)
	p = cursor.execute(query1)
	q = cursor.execute(query2)
	database.commit()
	fat(root,text2)
	button10.config(state="disable")
	button11.config(state="active")
	button12.config(state="active")
	button1.config(state="active")
	button2.config(state="active")
	button3.config(state="active")

def fat(root,text2):
	query3 = """SELECT * FROM testing2"""
	cursor.execute(query3)
	m = cursor.fetchmany(10000)
	for x in range(1,9999):
		text2.insert(0.0,m[x])
		text2.insert(0.0,'\n')
	text2.insert(1.0,m[0])



def next(root):
	root.destroy()
	root1 = Tk()
	root1.geometry("1500x880")
	root1.configure(background='#54EDAA')
	root1.wm_iconbitmap('py.ico')
	root1.wm_title('Performance Analysis')



	label = Label(root1, text= 'Interactive tool for suggest the type of indexing based on the type of data on column', font=("Hoefler Text", 15))
	label.pack(anchor=CENTER)
	label.place(height=40, width=800, x=250, y=50)



	sList = ["bigint", "bigserial",
			"bit [ (n) ]", "bit varying [ (n) ]	",
			"boolean","box","bytea","character [ (n) ]","character varying [ (n) ]","cidr",
			"circle","date","double precision","inet","inetger","interval [ fields ] [ (p) ]","json","jsonb",
			"line","lseg","macaddr","money","numeric [ (p, s) ]","path","pg_lsn","point","polygon","real","smallint",
			"smallserial","serial","text","time [ (p) ] [ without time zone ]","time [ (p) ] with time zone	",
			"timestamp [ (p) ] [ without time zone ]","timestamp [ (p) ] with time zone","tsquery","tsvector",
			"txid_snapshot","uuid","xml"]

	option = StringVar(root1)
	option.set("Type of a column for indexing") # Set the first value to be the default option

	w = apply(OptionMenu, (root1, option) + tuple(sList))
	w.pack()
	w.place(height=50,width=600,x=350,y=250)
	menu = w.nametowidget(w.menuname) 
	menu.configure(font=("Hoefler Text", 20))

	label1 = Label(root1, text= 'Size if applicable on column', font=("Hoefler Text", 15))
	label1.pack(anchor=CENTER)
	label1.place(height=40, width=600, x=350, y=360)

	text1 = Text(root1,font=("Helvetica", 20))
	text1.place(height=50, width=600, x=350, y=400)

	label2 = Label(root1, text= 'Column Name Text box', font=("Hoefler Text", 15))
	label2.pack(anchor=CENTER)
	label2.place(height=40, width=600, x=350, y=110)

	text1 = Text(root1,font=("Helvetica", 20))
	text1.place(height=50, width=600, x=350, y=150)

	# text1.insert(END, 'Size if applicable on column')

	button1 = Button(root1, text='suggest',command=lambda:testfun(root1,option), font=("Hoefler Text", 15))
	button1.pack(expand=True, fill='both')
	button1.place(bordermode=OUTSIDE, height=40, width=150, x=550, y=500)






def testfun(root1,option):
	v3 = option.get()

	text2 = Text(root1,font=("Helvetica", 20))
	text2.place(height=100, width=600, x=350, y=550)
	text2.delete(1.0,END)

	ar1=["box","circle","line","path","point","polygon"]
	for x in range(0,6):
		if v3==ar1[x]:
			text2.delete(1.0,END)
			text2.insert(1.0,"SPATIAL INDEXING")
			break

	ar2 = ["bigint", "bigserial",
			"bit [ (n) ]", "bit varying [ (n) ]	",
			"boolean","bytea","character [ (n) ]","character varying [ (n) ]","cidr",
			"date","double precision","inet","inetger","interval [ fields ] [ (p) ]","json","jsonb",
			"lseg","macaddr","money","numeric [ (p, s) ]","pg_lsn","real","smallint",
			"smallserial","serial","text","time [ (p) ] [ without time zone ]","time [ (p) ] with time zone	",
			"timestamp [ (p) ] [ without time zone ]","timestamp [ (p) ] with time zone","tsquery","tsvector",
			"txid_snapshot","uuid","xml"]
	for x in range(0,35):
		if v3==ar2[x]:
			text2.delete(1.0,END)
			text2.insert(1.0,"CLUSTER INDEX")
			break



def cluster(text,root,text1,text2,button11):
	query0 = """DROP TABLE IF EXISTS testing3 """
	query1 = """CREATE TABLE testing3(
	 first_name VARCHAR (50),
	 last_name VARCHAR (50),
	 age VARCHAR (50),
	 country  VARCHAR (50),
	 zip VARCHAR (50),
	 lat VARCHAR (50),
	 long VARCHAR (50)
	)"""

	query2 = """COPY testing3 FROM 'C:/Users/HP/Desktop/python/datbase.csv' WITH DELIMITER AS ',' """
	a = cursor.execute(query0)
	p = cursor.execute(query1)
	q = cursor.execute(query2)
	database.commit()
	query3 = """CREATE INDEX test_id ON testing3 (first_name, last_name);"""
	query4 = """ALTER TABLE testing3 CLUSTER ON test_id"""
	query5 = """CLUSTER testing3"""
	p = cursor.execute(query3)
	q = cursor.execute(query4)
	r = cursor.execute(query5)
	database.commit()
	button11.config(state="disable")
	query6 = """SELECT * FROM testing3"""
	cursor.execute(query6)
	m = cursor.fetchmany(10000)
	text2.delete(1.0,END)
	for x in range(1,9999):
		text2.insert(0.0,m[x])
		text2.insert(0.0,'\n')
	text2.insert(1.0,m[0])
	global status
	status = 3


def spatial(text,root,text1,text2,button12):
	query0 = """DROP TABLE IF EXISTS testing4 """
	query1 = """CREATE TABLE testing4(
	 first_name VARCHAR (50),
	 last_name VARCHAR (50),
	 age VARCHAR (50),
	 country  VARCHAR (50),
	 zip VARCHAR (50),
	 lat VARCHAR (50),
	 long VARCHAR (50)
	)"""

	query2 = """COPY testing4 FROM 'C:/Users/HP/Desktop/python/datbase.csv' WITH DELIMITER AS ',' """
	a = cursor.execute(query0)
	p = cursor.execute(query1)
	q = cursor.execute(query2)
	database.commit()
	query3 = """CREATE INDEX geom_idx1 ON testing4 USING GIST (lat, long)"""
	cursor.execute(query3)
	database.commit()
	button12.config(state="disable")
	query6 = """SELECT * FROM testing3"""
	cursor.execute(query6)
	m = cursor.fetchmany(10000)
	text2.delete(1.0,END)
	for x in range(1,9999):
		text2.insert(0.0,m[x])
		text2.insert(0.0,'\n')
	text2.insert(1.0,m[0])
	global status
	status =4




def mainloop():
	root = Tk()
	root.geometry("1500x880")
	root.configure(background='#54EDAA')
	root.wm_iconbitmap('py.ico')
	root.wm_title('Performance Analysis')
	# photo = PhotoImage(file="3.gif")
	# w = Label (root, image=photo)
	# w.place(x=0, y=0, relwidth=10, relheight=10,height=100,width=150)
	# w.photo = photo
	# w.pack()

	label1 = Label(root, text= 'Showing Execution Time', font=("Hoefler Text", 10))
	label1.pack(anchor=CENTER)
	label1.place(height=30, width=1200, x=50, y=20)


	text = Text(root,font=("Helvetica", 20))
	text.place(height=50, width=1200, x=50, y=50)

	button1 = Button(root, text="SELECT ALL RECORD",command=lambda:q1(text,root,text1), font=("Hoefler Text", 15))
	button1.pack(expand=True, fill='both')
	button1.place(bordermode=OUTSIDE, height=40, width=250, x=550, y=150)
	button1.config(state="disable")


	button2 = Button(root, text='UPDATE ONE RECORD',command=lambda:q2(text,root,text1), font=("Hoefler Text", 15))
	button2.pack(expand=True, fill='both')
	button2.place(bordermode=OUTSIDE, height=40, width=250, x=550, y=250)
	button2.config(state="disable")

	button3 = Button(root, text='INSERT ONE RECORD',command=lambda:q3(text,root,text1), font=("Hoefler Text", 15))
	button3.pack(expand=True, fill='both')
	button3.place(bordermode=OUTSIDE, height=40, width=250, x=550, y=350)
	button3.config(state="disable")

	label1 = Label(root, text= 'Press the button for CREATEa new table', font=("Hoefler Text", 10))
	label1.pack(anchor=CENTER)
	label1.place(height=30, width=400, x=95, y=120)

	button10 = Button(root, text='CREATE TABLE',command=lambda:q10(text,root,text1,button10,button11,button12,button1,button2,button3,text2), font=("Hoefler Text", 15))
	button10.pack(expand=True, fill='both')
	button10.place(bordermode=OUTSIDE, height=40, width=200, x=200, y=150)


	label2 = Label(root, text= 'Press the button for CLUSTER indexing', font=("Hoefler Text", 10))
	label2.pack(anchor=CENTER)
	label2.place(height=30, width=400, x=95, y=220)

	button11 = Button(root, text='CLUSTER INDEXING',command=lambda:cluster(text,root,text1,text2,button11), font=("Hoefler Text", 15))
	button11.pack(expand=True, fill='both')
	button11.place(bordermode=OUTSIDE, height=40, width=200, x=200, y=250)
	button11.config(state="disable")

	label3 = Label(root, text= 'Press the button for SPATIAL indexing', font=("Hoefler Text", 10))
	label3.pack(anchor=CENTER)
	label3.place(height=30, width=400, x=95, y=320)


	button12 = Button(root, text='SPATIAL INDEXING',command=lambda:spatial(text,root,text1,text2,button12), font=("Hoefler Text", 15))
	button12.pack(expand=True, fill='both')
	button12.place(bordermode=OUTSIDE, height=40, width=200, x=200, y=350)
	button12.config(state="disable")

	button13 = Button(root, text='NEXT',command=lambda:next(root), font=("Hoefler Text", 15))
	button13.pack(expand=True, fill='both')
	button13.place(bordermode=OUTSIDE, height=40, width=150, x=950, y=650)


	label1 = Label(root, text= 'Description of all', font=("Hoefler Text", 10))
	label1.pack(anchor=CENTER)
	label1.place(height=30, width=500, x=850, y=110)


	text1 = Text(root,font=("Helvetica", 15))
	text1.place(height=250, width=500, x=850, y=140)



	label1 = Label(root, text= 'Showing Database Result', font=("Hoefler Text", 10))
	label1.pack(anchor=CENTER)
	label1.place(height=30, width=1000, x=150, y=420)

	text2 = Text(root,font=("Helvetica", 15))
	text2.place(height=150, width=1000, x=150, y=450)


	root.mainloop()



mainloop()
