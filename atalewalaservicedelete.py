import mysql.connector;
email=input("enter email id");
con=mysql.connector.connect(host="localhost",user="root",password="root",database="test");
operation=con.cursor();
#sql="delete * from atalewalaservice;
sql="delete * from atalewalaservice where email=%s";
values=(email);
operation.execute(sql,values);
con.commit();
con.close();
print("Record deleted");