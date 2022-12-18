import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image,ImageDraw,ImageFont
import qrcode
from datetime import date  
import random as rand

while True:
      print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
      print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
      print("--------------------------------ONEPLUS LIBRARY----------------------------------------")
      print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
      print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
      print('Welcome to this library management program')
      print("  MAIN NENU")
      print("1. Display Books")
      print("2. Add Books")
      print("3. Search Books")
      print("4. Members Record-Delete,Search and Add Member's Record")
      print("5.Issue books")
      print("6. Show issued books")
      print("7.Delete Issued Books")
      print("8.Return Book")
      print("9.Show Returned Books")
      print("10.Delete Returned Book record")
      print("11.Update member's issue record")
      print('12.Apply for Membership')
      print('13.Update Membership')
      print("14.View Charts")
      print('15.Cancel Membership')
      print('16.Know More')
      print('17.Any Feedback')
      print('18.Any Query')
      print("19.Show Feedback/Queries")
      print("20.Delete Feedback/Query")
      print("21.Answer a Query")
      print("22.OnePlus Special Contest for the readers")
      print("23.Contact Us")
      print("24.Show Membership card")
      print("25.Exit")
      ch=int(input("Enter your choice:   "))
      if ch==1:
            df=pd.read_csv("libdata.csv")
            print(df)
      elif ch==2:
            print("1.Add Books")
            print("2.Edit Books")
            opt=int(input("Select Your Choice:  "))
            if opt==1:
                  bookname=input("Enter Book name:  ")
                  authorname=input("Enter Author's name: ")
                  dot=input("enter date of entry(DD-MM-YYYY): ")
                  bookcode=input("Enter Book code no.: ")
                  SUB=input("Enter Subject:  ")
                  AMOUNT=int(input("Enter Price:   "))
                  Totalbooks=int(input('Enter the quantity of book you are adding:   '))
                  df=pd.DataFrame({'Book Name':[bookname],'Author Name':[authorname],
                  ' date of issue':[dot],'Code No':[bookcode],'Subject':[SUB],'Price':[AMOUNT],'Quantity':[Totalbooks]})
                  df.to_csv('libdata.csv',mode='a',index=False,header=None)
                  print("Record added sucessfully")
            if opt==2:
                  ax=input("Wanna change any book details(Yes or No):  ")
                  if ax=='Yes':
                        print("1.Edit Book Name")
                        print("2.Edit Author Name")
                        print("3.Edit Date of Entry")
                        print("4.Edit Code No.")
                        print("5.Edit Subject")
                        print("6.Edit Price")
                        print("7.Edit Quantity")
                        elibdta=int(input("Enter your choice:  "))
                        if elibdta==1:
                              df=pd.read_csv('libdata.csv')
                              pbname=input("Enter the book name:  ")
                              Ename=input("Enter the name you want to show:  ")
                              Elib=df[df["Book Name"]==pbname].index
                              print(Elib)
                              #Elibin=int(input("Enter the index showing with the book name:  "))
                              df.loc[Elib,["Book Name"]]=pbname
                              df.to_csv('libdata.csv',index=False)
                        if elibdta==2:
                              df=pd.read_csv('libdata.csv')
                              bname=input("Enter the Book Name:  ")
                              aname=input("Enter the Author Name you want to show:  ")
                              arn=df[df["Book Name"]==bname].index
                              print(arn)
                              #arnin=int(input("Enter the index with the book name:  "))
                              df.loc[arn,['Author Name']]=aname
                              df.to_csv('libdata.csv',index=False)
                        elif elibdta==3:
                              df=pd.read_csv('libdata.csv')
                              bname=input("Enter the Book Name:  ")
                              doen=input("Enter date of entry you want to show:  ")
                              dna=df[df['Book Name']==bname]
                              print(dna)
                              doein=int(input('Enter the index shown with the book:  '))
                              df.loc[doen,'date of entry']=doen
                              df.to_csv('libdata.csv',index=False)
                        elif elibdta==4:
                              df=pd.read_csv('libdata.csv')
                              bname=input("Enter the Book Name:  ")
                              cdno=int(input("Enter the Code No. you want to show:  "))
                              reach=df[df['Book Name']==bname].index
                              print(reach)
                              coden=int(input("Enter the index name shown with the book:  "))
                              df.loc[reach,'Code No']=cdno
                              df.to_csv('libdata.csv',index=False)  
                        elif elibdta==5:
                              df=pd.read_csv('libdata.csv')
                              bname=input("Enter the Book Name: ")
                              subch=input("Enter the Subject you want to show:  ")
                              SUBS=df[df['Book Name']==bname]
                              print(SUBS)
                              subin=int(input("Enter the index shown along with the book:  "))
                              df.loc[SUBS,'Subject']=subch
                              df.to_csv('libdata.csv',index=False)
                        elif elibdta==6:
                              df=pd.read_csv('libdata.csv')
                              bname=input("Enter the Book Name:  ")
                              prch=int(input("Enter the Price you want to show:  "))
                              bb=df[df['Book Name']==bname]
                              print(bb)
                              prb=int(input("Enter the index shown along with the book:  "))
                              df.loc[prb,'Price']=prch
                              df.to_csv('libdata.csv',index=False)
                        elif elibdta==7:
                              df=pd.read_csv('libdata.csv')
                              bname=input("Enter the Book Name:  ")
                              qch=int(input("Enter the Quantity you want to show:  "))
                              libb=df[df['Book Name']==bname]
                              print(libb)
                              quanindex=int(input("Enter the index shown along with the Book Name:  "))
                              df.at[quanindex,'Quantity']=qch
                              df.to_csv('libdata.csv',index=False)
                  elif ax=='No':
                        print('')
                  else:
                        print("1.Edit Book Name")
                        print("2.Edit Author Name")
                        print("3.Edit Date of Entry")
                        print("4.Edit Code No.")
                        print("5.Edit Subject")
                        print("6.Edit Price")
                        print("7.Edit Quantity")
                        elibdta=int(input("Enter your choice:  "))
                        if elibdta==1:
                              df=pd.read_csv('libdata.csv')
                              pbname=input("Enter the book name:  ")
                              Ename=input("Enter the name you want to show:  ")
                              Elib=df[df["Book Name"]==pbname].index
                              print(Elib)
                              Elibin=int(input("Enter the index showing with the book name:  "))
                              df.loc[Elib,["Book Name"]]=pbname
                              df.to_csv('libdata.csv',index=False)
                        if elibdta==2:
                              df=pd.read_csv('libdata.csv')
                              bname=input("Enter the Book Name:  ")
                              aname=input("Enter the Author Name you want to show:  ")
                              arn=df[df["Book Name"]==bname].index
                              print(arn)
                              arnin=int(input("Enter the index with the book name:  "))
                              df.loc[arn,['Author Name']]=aname
                              df.to_csv('libdata.csv',index=False)
                        elif elibdta==3:
                              df=pd.read_csv('libdata.csv')
                              bname=input("Enter the Book Name:  ")
                              doen=input("Enter date of entry you want to show:  ")
                              dna=df[df['Book Name']==bname]
                              print(dna)
                              doein=int(input('Enter the index shown with the book:  '))
                              df.at[doein,'date of entry']=doen
                              df.to_csv('libdata.csv',index=False)
                        elif elibdta==4:
                              df=pd.read_csv('libdata.csv')
                              bname=input("Enter the Book Name:  ")
                              cdno=int(input("Enter the Code No. you want to show:  "))
                              reach=df[df['Book Name']==bname]
                              print(reach)
                              coden=int(input("Enter the index name shown with the book:  "))
                              df.at[coden,'Code No']=cdno
                              df.to_csv('libdata.csv',index=False)  
                        elif elibdta==5:
                              df=pd.read_csv('libdata.csv')
                              bname=input("Enter the Book Name: ")
                              subch=input("Enter the Subject you want to show:  ")
                              SUBS=df[df['Book Name']==bname]
                              print(SUBS)
                              subin=int(input("Enter the index shown along with the book:  "))
                              df.at[subin,'Subject']=subch
                              df.to_csv('libdata.csv',index=False)
                        elif elibdta==6:
                              df=pd.read_csv('libdata.csv')
                              bname=input("Enter the Book Name:  ")
                              prch=int(input("Enter the Price you want to show:  "))
                              bb=df[df['Book Name']==bname]
                              print(bb)
                              prb=int(input("Enter the index shown along with the book:  "))
                              df.at[prb,'Price']=prch
                              df.to_csv('libdata.csv',index=False)
                        elif elibdta==7:
                              df=pd.read_csv('libdata.csv')
                              bname=input("Enter the Book Name:  ")
                              qch=int(input("Enter the Quantity you want to show:  "))
                              libb=df[df['Book Name']==bname]
                              print(libb)
                              quanindex=int(input("Enter the index shown along with the Book Name:  "))
                              df.at[quanindex,'Quantity']=qch
                              df.to_csv('libdata.csv',index=False)
            
      elif ch==3:
            print("1. Search by Book Name:  ")
            print("2. Search by Author Name:  ")
            print("3. Search by Subject:  ")
            print("4.Search by Quantity: ")
            ans=int(input("enter your choice:  "))
            if ans==1:
                  df=pd.read_csv("libdata.csv")
                  a=input("Enter the name of book which  you want to search: ")
                  i=df[df['Book Name']==a]
                  print(i)
            elif ans==2:
                  n=input("Enter the name of author of book which  you want to search:   ")
                  df=pd.read_csv("libdata.csv")
                  src=df[df["Author Name"]==n]
                  print(src)
            elif ans==3:
                  d=input("Enter the subject of book which  you want to search:   ")
                  df=pd.read_csv("libdata.csv")
                  src=df[df["Subject"]==d]
                  print(src)
            elif ans==4:
                  df=pd.read_csv('libdata.csv')
                  qu=int(input("Enter the quantity of books you want to search"))
                  src=df[df["Quantity"]==qu]
                  print(src)     
      elif ch==4:
            print("1. Add a member")
            print("2. Show members list")
            print("3. Delete Member record")
            print("4.Search a member")
            print("5.Edit a Member Record")
            ans=int(input("Enter your choice:   "))
            if ans==1:
                  mname=input("Enter the new member's name:   ")
                  phone=input("Enter the member's phone no.:  ")
                  irec=input("Enter the numbers of book issued:  ")
                  Membership_lan=input("Enter the span of membership plan: ")
                  h=int(input('Enter member id:  '))
                  Memrec=pd.DataFrame({'Member Id':[h],"Member Name":[mname],'Phone No.':[phone],
                  'Membership Plan validity':[Membership_lan],'No. of Books Issued':[irec]})
                  Memrec.to_csv("lib.csv",mode='a',index=False,header=None)
                  print("Member's detals are added ")
                  print('We welcome the new member to our library')

            if ans==2:
                  Memrec=pd.read_csv('lib.csv')
                  print(Memrec)

            if ans==3:
                  Memrec=pd.read_csv("lib.csv")
                  e=input("Enter the member name which record you want to delete:   ")
                  Memrec=Memrec.drop(Memrec[Memrec["Member Name"]==e].index)
                  Memrec.to_csv("lib.csv",index=False)
                  print("Thw member's details have been deleted")

            if ans==4:
                  print("1.Search by Member Name")
                  print("2.Search by Member Id")
                  print("3.Search by Phone No.")
                  f1=int(input("Select your option:  "))
                  if f1==1:
                        mn=input("Enter the name of member which  you want to search:   ")
                        Memrec=pd.read_csv("lib.csv")
                        srcc=Memrec[Memrec["Member Name"]==mn]
                        print(srcc) 
                  elif f1==2:
                        mi=int(input("Enter the Id of member which  you want to search:   "))
                        Memrec=pd.read_csv("lib.csv")
                        sr=Memrec[Memrec["Member Id"]==mi]
                        print(sr) 
                  elif f1==3:
                        pn=int(input("Enter the phone No. of member which  you want to search:   "))
                        Memrec=pd.read_csv("lib.csv")
                        srd=Memrec[Memrec["Phone No."]==pn]
                        print(srd)

            if ans==5:
                  print("1.Edit Member Name")
                  print("2.Edit Phone No.")
                  print("3.Edit Membership_Plan_valdity")
                  mrn=int(input("Select Your Choice:  "))
                  if mrn==1:
                        Memrec=pd.read_csv('lib.csv')
                        mn=input("Enter your Name:  ")
                        me=input("Enter your Name whic you want to use: ")
                        MNM=Memrec[Memrec["Member Name"]==mn].index
                        print(MNM)
                        mi=int(input("Enter the Index Code showing with your name: "))
                        Memrec.loc[MNM,'Member Name']=me
                        Memrec.to_csv('lib.csv',index=False)
                  if mrn==2:
                        Memrec=pd.read_csv('lib.csv')
                        mpn=input("Enter your Phone No.:  ")
                        mpne=input("Enter your Phone No. whic you want to use: ")
                        MNM=Memrec[Memrec["Phone No."]==mpn].index
                        print(MNM)
                        mi=int(input("Enter the index showing with your name: "))
                        Memrec.loc[MNM,'Phone No.']=mpne
                        Memrec.to_csv('lib.csv',index=False)
                  if mrn==3:
                        Memrec=pd.read_csv('lib.csv')
                        mpln=input("Enter your Membership Plan showing:  ")
                        mplne=input("Enter your Plan you are currently using: ")
                        MNM=Memrec[Memrec["Membership_Plan_validity"]==mpln].index
                        print(MNM)
                        mi=int(input("Enter the index code showing with your name: "))
                        Memrec.loc[MNM,'Membership_Plan_validity']=mplne
                        Memrec.to_csv('lib.csv',index=False)

      elif ch==5:
            k=input("Enter Book name:  ")
            l=input("Enter Author's name: ")
            d=input("enter date of issue(DD-MM-YYYY): ")
            t=input("Enter Book code no.: ")
            s=input("Enter Subject:  ")
            p=int(input("Enter Price:   "))
            membname=input("Enter the issuing person's name: ")
            quant=int(input('Enter the quantity of books: '))
            ef=pd.DataFrame({'Book Name':[k],"Author's Name":[l],'Date of Issue':[d],
            'Book Code':[t],'Subject':[s],'Price':[p],'Quantity':[quant],"Book Taker's name":[membname]})
            print("Book has been issued successfully")
            ef.to_csv('issue.csv',mode='a',index=False,header=None)

      elif ch==6:
            ef=pd.read_csv('issue.csv')
            print(ef)

      elif ch==7:
            D=input("Enter the  name of book which  you want to delete:  ")
            ef=pd.read_csv("issue.csv")
            delt=ef[ef["Book Name"]==D].index
            ef.drop(delt,inplace=True)
            ef.to_csv("issue.csv",index=False)
            print("Data deleted sucessfully")   

      elif ch==8:
            book_name=input('Enter the book name: ')
            membname=input("Enter the member's name:  ")
            aname=input("Enter Author's name: ")
            dor=input("enter date of return(DD-MM-YYYY): ")
            bcode=input("Enter Book code no.: ")
            sub=input("Enter Subject:  ")
            pr=int(input("Enter Price:   "))
            gf=pd.DataFrame({'Book Name':[book_name],'Member Name':[membname],
            'Author Name':[aname],'Date of Return':[dor],
            'Book Code':[bcode],'Subject':[sub],'Price':[pr]})
            gf.to_csv('Returned Books.csv',mode='a',index=False,header=None)
            print('Book has been returned successfully')

      elif ch==9:
            gf=pd.read_csv('Returned Books.csv')
            print("1.Search your required book")
            print("2.Show all ")
            sb=int(input("Enter your choice:   "))
            if sb==1:
                  print("1.Search by Book Name")
                  print("2.Search by Date of Return")
                  print("3.Search by Book Code")
                  print("4.Search by Subject")
                  print("5.Search by Member Name")
                  print("6.Search by Price")
                  sc=int(input("Select your choice:  "))
                  if sc==1:
                        gf=pd.read_csv('Returned Books.csv')
                        bn=input("Enter the name of book you want to search:  ")
                        bnn=gf[gf["Book Name"]==bn].index
                        print(gf.loc[bnn])
                  if sc==2:
                        gf=pd.read_csv('Returned Books.csv')
                        dr=input("Enter the date of return of the book:  ")
                        dorn=gf[gf["Date of Return"]==dr].index
                        print(gf.loc[dorn])
                  if sc==3:
                        gf=pd.read_csv('Returned Books.csv')
                        bcde=int(input("Enter the book code of book which you want to search:  "))
                        bkcde=gf[gf["Book Code"]==bcde].index
                        print(gf.loc[bkcde])
                  if sc==4:
                        gf=pd.read_csv('Returned Books.csv')
                        sbj=input("Enter the subject of book you want to search:  ")
                        sub=gf[gf["Subject"]==sbj].index
                        print(gf.loc[sub])
                  if sc==5:
                        gf=pd.read_csv('Returned Books.csv')
                        Mnme=input("Enter the name of meber you want to search:  ")
                        Mname=gf[gf["Member Name"]==Mnme].index
                        print(gf.loc[Mname])
                  if sc==6:
                        gf=pd.read_csv('Returned Books.csv')
                        Pr=int(input("Enter the price of book you want to search:  "))
                        Prc=gf[gf["Price"]==Pr].index
                        print(gf.loc[Prc])
            if sb==2:
                  print(gf)
            
      elif ch==10:
            A=input("Enter the  name of book which  you want to delete:  ")
            gf=pd.read_csv("Returned Books.csv")
            dlt=gf[gf["Book Name"]==A].index
            gf.drop(dlt,inplace=True)
            gf.to_csv("Returned Books.csv",index=False)
            print("Data deleted sucessfully")

      elif ch==11:
            Memrec=pd.read_csv('lib.csv')
            ef=pd.read_csv('issue.csv')
            nam=input('Enter the name of member: ')
            A=Memrec[Memrec["Member Name"]==nam].index
            B=ef[ef["Book Taker's name"]==nam]
            print(B)
            if B.empty:
                  print("No books has been issued")
            print('If you have any other issued book than this add that as well.')
            print('We will add this data in your book manually')
            sf=int(input('Enter no. of books you issued:  '))
            Memrec.loc[A,['No. of Books issued']]=sf
            fc=input('Wanna see the issue list(Yes or No):  ')
            if fc=='Yes':
                  print(ef)
            elif fc=='No':
                  print('Ok,Thanks for checking')
            Memrec.to_csv('lib.csv',index=False)
            print("Member's issue record has been updated successfully")

      elif ch==12:
            print('1.Show membership plans')
            print('2.Activate Membership')
            print('3.Features of a Membership')
            print('4.Have a coupon code ')
            n=int(input('Enter your choice:  '))
            if n==1:
                  print('A.Rs.300/Month')
                  print('B.Rs.600/2 Months')
                  print('C.1000/3 Months')
                  print('D.2100/6 Months')
                  print('E.4500/Year')
                  print('F.10000/2 Years')
                  print('G.14000/3 Year')
                  print('H.18000/4 Year')
                  print('I.23000/5 Year')
                  fr=input('Do you want a plan(Yes or No): ')
                  if fr=='Yes':
                        pl=input('Enter your plan:  ')
                        if pl=='A':
                              mr=int(input("Enter how many memberships you need:  "))
                              mn=int(input("For how many months you need: "))
                              amt=300*mr*mn
                              print('Your amount for',mr,'valid for',mn,'months','Your amount will be', amt)
                        if pl=='B':
                              mr=int(input("Enter how many memberships you need:  "))
                              amt=1000*mr
                              print('Your amount for',mr,'memberships will be', amt)
                        if pl=='C':
                              mr=int(input("Enter how many memberships you need:  "))
                              amt=300*mr
                              print('Your amount for',mr,'memberships will be', amt)
                        if pl=='D':
                              mr=int(input("Enter how many memberships you need:  "))
                              amt=2100*mr
                              print('Your amount for',mr,'memberships will be', amt)
                        if pl=='E':
                              mr=int(input("Enter how many memberships you need:  "))
                              amt=4500*mr
                              print('Your amount for',mr,'memberships will be', amt)
                        if pl=='F':
                              mr=int(input("Enter how many memberships you need:  "))
                              amt=300*mr
                              print('Your amount for',mr,'memberships will be', amt)
                        if pl=='G':
                              mr=int(input("Enter how many memberships you need:  "))
                              amt=300*mr
                              print('Your amount for',mr,'memberships will be', amt)
                        if pl=='H':
                              mr=int(input("Enter how many memberships you need:  "))
                              amt=300*mr
                              print('Your amount for',mr,'memberships will be', amt)
                        if pl=='I':
                              mr=int(input("Enter how many memberships you need:  "))
                              amt=300*mr
                              print('Your amount for',mr,'memberships will be', amt)
                  if fr=='No':
                        print('No problem,Thank You for checking')
            elif n==2:
                  Memrec=pd.read_csv('lib.csv')
                  mname=input("Enter the new member's name:   ")
                  phone=input("Enter the member's phone no.:  ")
                  irec=input("Enter the numbers of book issued(Enter 0 for now):  ")
                  Membership_lan=input("Enter the span of membership plan: ")
                  h=int(input('Enter member id:  '))
                  Memrec=pd.DataFrame({'Member Id':[h],"Member Name":[mname],'Phone No.':[phone],
                  'Membership Plan validity':[Membership_lan],'No. of Books Issued':[irec]})
                  Memrec.to_csv("lib.csv",mode='a',index=False,header=None)
                  print("Member's detals are added ")
                  print('Your membership has been approved succesfully')
                  print('Now,you are officially a member')
            elif n==3:
                  print('The Library Membership brings a set of facillities which is provided only to the members')
                  print('1.The Authority of Issuing Books without any limit.')
                  print('2.Free Books Galore.')
                  print('3.Access to Databases and Courses.')
                  print('4.Access to Prenium Books and Material.')
                  print('5.Authority to use Library Laptops for personal use')
            elif n==4:
                  cm=input('Enter your coupon code here: ')
                  print("Your code is valid ")
                  ans=int(input("Do you want to redeem your coupon code(Yes or No):  "))
                  if ans=='Yes':
                        Memrec=pd.read_csv('lib.csv')
                        mname=input("Enter the new member's name:   ")
                        phone=input("Enter the member's phone no.:  ")
                        irec=input("Enter the numbers of book issued(Enter 0 for now):  ")
                        Membership_lan=input("Enter the span of membership plan: ")
                        h=int(input('Enter member id:  '))
                        Memrec=pd.DataFrame({'Member Id':[h],"Member Name":[mname],'Phone No.':[phone],
                        'Membership Plan validity':[Membership_lan],'No. of Books Issued':[irec]})
                        Memrec.to_csv("lib.csv",mode='a',index=False,header=None)
                        print("Member's detals are added ")
                        print('Your membership has been approved succesfully')
                        print('Now,you are officially a member')
                  elif ans=='No':
                        pass
      elif ch==13:
            Memrec=pd.read_csv('lib.csv')
            fd=input("Enter the member's name: ")
            sd=input('For how many months you need the membership: ')
            K=Memrec[Memrec["Member Name"]==fd]
            print(K)
            fc=input('Are you able to see your record(Yes or No):  ')
            if fc=="Yes":
                  pass
            elif fc=='No':
                  print(Memrec)
                  print('See your record from here and write the index.')
            else:
                  pass
            sf=int(input("Enter the index displayed for accurate transfer of data:  "))
            Memrec.loc[sf,'Membership_Plan_validity']=sd
            Memrec.to_csv('lib.csv',index=False)
            print('You membership plan has been updated.')

      elif ch==14:
            print('1.Book and their cost')
            print('2.Number of books issued by a member')
            print('3.Feedback by different Users')
            print("4.User satisfaction")
            print("5.Books and their quantities")
            choice=int(input('Enter your choice:  '))
            if choice==1:
                  print("1.Bar Graph")
                  print("2.Line Graph")
                  print("3.Scatter Chart")
                  ch=int(input("Enter your choice: "))
                  if ch==1:
                        print("A.For books in library")
                        print("B.For books issued")
                        print("C.For books returned")
                        op=input("Select an option: ")
                        if op=='A':
                              df=pd.read_csv('libdata.csv')
                              X=df["Book Name"]
                              Y=df['Price']
                              plt.barh(X,Y)
                              plt.title('Prices of Books stored in the library ')
                              plt.ylabel('Book Name------>')
                              plt.xlabel('Price---------->')
                              plt.show()
                        elif op=='B':
                              ef=pd.read_csv('issue.csv')
                              pn=ef['Price']
                              bn=ef['Book Name']
                              plt.barh(bn,pn)
                              plt.title("Books issued by a library")
                              plt.xlabel('Book Name---->')
                              plt.ylabel('Price--->')
                              plt.show()
                        elif op=='C':
                              gf=pd.read_csv('Returned Books.csv')
                              pn=gf['Price']
                              bn=gf['Book Name']
                              plt.bar(pn,bn)
                              plt.title("Books issued by a library")
                              plt.xlabel('Book Name---->')
                              plt.ylabel('Price--->')
                              plt.show()
                  elif ch==2:
                        print("A.For books in library")
                        print("B.For books issued")
                        print("C.For books returned")
                        op=input("Select an option: ")
                        if op=='A':
                              df=pd.read_csv('libdata.csv')
                              df.sort_values("Price")
                              X=df["Price"]
                              Y=df['Book Name']
                              plt.plot(X,Y,'o-')
                              plt.title('No. of Books issued by a member')
                              plt.ylabel('Book Name------>')
                              plt.xlabel('Price---------->')
                              plt.show()
                        elif op=='B':
                              ef=pd.read_csv('issue.csv')
                              ef.sort_values("Price")
                              X=ef["Price"]
                              Y=ef['Book Name']
                              plt.plot(X,Y,'o-')
                              plt.title('No. of Books issued by a member')
                              plt.ylabel('Book Name------>')
                              plt.xlabel('Price---------->')
                              plt.show()
                        elif op=='C':
                              gf=pd.read_csv('Returned Books.csv')
                              gf.sort_values("Price")
                              X=gf["Price"]
                              Y=gf['Book Name']
                              plt.plot(X,Y,'o-')
                              plt.title('No. of Books issued by a member')
                              plt.ylabel('Book Name------>')
                              plt.xlabel('Price---------->')
                              plt.show()
                  elif ch==3:
                        df=pd.read_csv('libdata.csv')
                        X=df['Price']
                        Y=df['Book Name']
                        plt.scatter(X,Y)
                        plt.show()
            elif choice==2:
                  print("1.Bar Graph")
                  print("2.Line Graph")
                  print("3.Scatter Chart")
                  ch=int(input("Enter your choice: "))
                  if ch==1:
                        Memrec=pd.read_csv('lib.csv')
                        F=Memrec['Member Name']
                        G=Memrec['No. of Books issued']
                        plt.barh(F,G,color='red')
                        plt.ylabel('Member Name')
                        plt.xlabel('No. of Books Issued')
                        plt.show()
                  elif ch==2:
                        Memrec=pd.read_csv('lib.csv')
                        F=Memrec['Member Name']
                        G=Memrec['No. of Books issued']
                        plt.plot(F,G,'o-')
                        plt.ylabel('Member Name')
                        plt.xlabel('No. of Books Issued')
                        plt.show()
                  elif ch==3:
                        Memrec=pd.read_csv('lib.csv')
                        F=Memrec['Member Name']
                        G=Memrec['No. of Books issued']
                        plt.scatter(F,G)
                        plt.show()
            elif choice==3:
                  print("1.Bar Chart")
                  print("2.Line Chart")
                  print("3.Pie Chart")
                  print("4.Scatter Chart")
                  ch=int(input("Enter the choice: "))
                  if ch==1:
                        Feedback=pd.read_csv('libd.csv')
                        X=Feedback['Ratings']
                        Y=Feedback['Name']
                        plt.title('Ratings given by various Users')
                        plt.xlabel('Name of Users')
                        plt.ylabel('Ratings')
                        plt.legend("Ratings")
                        plt.bar(Y,X)
                        plt.show()
                  elif ch==2:
                        Feedback=pd.read_csv('libd.csv')
                        X=Feedback['Ratings']
                        Y=Feedback['Name']
                        plt.title('Ratings given by various Users')
                        plt.xlabel('Name of Users')
                        plt.ylabel('Ratings')
                        ac=plt.plot(Y,X,'o-')
                        plt.legend(ac[:2], ['Ratings'])
                        plt.show()
                  elif ch==3:
                        Feedback=pd.read_csv('libd.csv')
                        Y=Feedback['Ratings']
                        X=Feedback['Name']
                        plt.pie(Y,labels=Y)
                        plt.legend(X)
                        plt.show()
                  elif ch==4:
                        Feedback=pd.read_csv('libd.csv')
                        Y=Feedback['Ratings']
                        X=Feedback['Name']
                        plt.scatter(X,Y)
                        plt.show()

            elif choice==4:
                  print("1.Bar Graph")
                  print("2.Pie Chart")
                  print("3.Line Chart")
                  print("4.Scatter Chart")
                  ch=int(input("Select your option:  "))
                  if ch==1:
                        Feedback=pd.read_csv('libd.csv')
                        X=Feedback['Ratings']
                        Y=Feedback['User Opinions']
                        plt.bar(Y,X)
                        plt.xlabel("User Opinions")
                        plt.ylabel("Ratings")
                        plt.show()
                  if ch==2:
                        Feedback=pd.read_csv('libd.csv')
                        X=Feedback['Ratings']
                        Y=Feedback['User Opinions']
                        plt.pie(X,labels=Y)
                        plt.show()
                  if ch==3:
                        Feedback=pd.read_csv('libd.csv')
                        F=Feedback['User Opinions']
                        Positive=1
                        Negative=0.5
                        Y=Feedback['Ratings']
                        plt.plot(F,Y,'o-')
                        plt.show()
                  elif ch==4:
                        Feedback=pd.read_csv('libd.csv')
                        Y=Feedback['Ratings']
                        X=Feedback['User Opinions']
                        plt.scatter(X,Y)
                        plt.show()
            elif choice==5:
                  print("1.Bar Graph")
                  print("2.Line Chart")
                  print("3.Scatter Chart")
                  ch=int(input("Choose your option"))
                  if ch==1:
                        gf=pd.read_csv('Returned Books.csv')
                        X=gf["Book Name"]
                        Y=gf['Price']
                        plt.barh(X,Y)
                        plt.title('Prices of Books stored in the library ')
                        plt.ylabel('Book Name------>')
                        plt.xlabel('Price---------->')
                        plt.show()
                  elif ch==2:
                        gf=pd.read_csv('Returned Books.csv')
                        X=gf["Book Name"]
                        Y=gf['Price']
                        plt.plot(X,Y)
                        plt.show()
                  elif ch==3:
                        gf=pd.read_csv('Returned Books.csv')
                        X=gf["Book Name"]
                        Y=gf['Price']
                        plt.scatter(X,Y)
                        plt.show()

      elif ch==15:
            E=input("Enter the  name of member whose name you want to delete:  ")
            Memrec=pd.read_csv("lib.csv")
            delet=Memrec[Memrec["Member Name"]==E].index
            Memrec.drop(delet,inplace=True)
            Memrec.to_csv("lib.csv",index=False)
            print("Your membership has been cancelled and your records are deleted successfully") 

      elif ch==16:
            print(''' We are a part of OnePlus's initiative 'Knowledge For All' and were recognized as an
           organization in 2019.We provide free books to the children.We have branches all over India.
           We provide all kinds of books in our library.We have a motive of royal library experience
           to middle class segment.We provide best services to each and every member of our library.
           We have almost 100+ branches all over India and almost 1000+ branches outside India.We are
           the first library to provide membership at Rs.300/Month which is still the least amount for
           a membership in a library.We are admist the first library to have all kinds of book at our
           each ans every branch.We are among the top 10 best libraries at present.We are the profound
           choice of a collage or a school student for peaceful studying and a place with all the study
           material of their need.We are still on our way to prove our tagline-"Provide Experience like No Other"
           A virtual library has been created to provide broader access to the manuscripts:Codices Electronici Sangallenses. 
           This project has been expanded to include codices from other libraries as well and is operating under the name 
           e-codices.
           "WE REQUEST ALL OUR MEMBERS AND USERS TO FOLLOW THESE GUILDELINES"
              -ABHIMANYU 
              (ONEPLUS LIBRAY MANAGER)
           OnePlus's One Library Ltd. Copyright@2019''')

      elif ch==17:
            print("1.Add Feedback")
            print("2.Edit Your Feedback")
            print("3.Edit Your Details")
            print("4.If You have any problem finding your name.Check your name here ")
            ff=int(input("Enter your choice:  "))
            if ff==1:
                  aname=input('Please enter your name: ')
                  fback=input('Please help us by providing your feedback:  ')
                  rate=int(input("How much will you rate our facillities(Out of 10): "))
                  aptrev=input("How will you categorize our library management(Positive/Negative/Average/Not Bad):  ")
                  Feedback=pd.DataFrame({'Name':[aname],'Feedback Received':[fback],
                  'Ratings':[rate],'User Opinions':[aptrev]})
                  Feedback.to_csv('libd.csv',mode='a',index=False,header=None)
                  print('''Thank you for your valuable feedback.We will look forward to give you a better experience/via your feedback ''')

            elif ff==2:
                  Feedback=pd.read_csv('libd.csv')
                  ed=input("Enter the name of member you want to search:  ")
                  print("Your Feedback is shown below:-")
                  fdc=Feedback[Feedback["Name"]==ed]
                  print(fdc)
                  yon=input("Do you want to edit your feedback(Yes or No):  ")
                  if yon=='Yes':
                        print("1.Edit Your Feedback")
                        print("2.Edit Your Ratings")
                        print("3.Edit Your User Opinions")
                        fro=int(input("Select Your Choice:   "))

                        if fro==1:
                              Feedbck=pd.read_csv('libd.csv')
                              mn=input("Enter your name:")
                              fk=input("Enter your edited Feedback:  ")
                              edf=Feedback[Feedback["Name"]==mn].index
                              Feedback.loc[edf,'Feedback Received']=fk
                              Feedback.to_csv('libd.csv',index=False)
                              print("Your Feedback has been edited")

                        if fro==2:
                              Feedbck=pd.read_csv('libd.csv')
                              mn=input("Enter your name:")
                              fr=int(input("Enter your Ratings:  "))
                              edf=Feedback[Feedback["Name"]==mn].index
                              Feedback.loc[edf,['Ratings']]=fr
                              Feedback.to_csv('libd.csv',index=False)
                              print("Your Feedback has been edited")

                        if fro==3:
                              Feedbck=pd.read_csv('libd.csv')
                              fop=input("Enter your User Opinion(Positive/Negative/Average/Not Bad):  ")
                              edf=Feedback[Feedback["Name"]==mn].index
                              Feedback.loc[edf,['User Opinions']]=fop
                              Feedback.to_csv('libd.csv',index=False)
                              print("Your Feedback has been edited")

                  if yon=='No':
                        print("Your Feedback is not changed as your progress was stopped by you.")

            elif ff==3:
                  Feedback=pd.read_csv('libd.csv')
                  nf=input("Enter Your Name:  ")
                  nfr=input("Enter The Name which you want to show: ")
                  nfk=Feedback[Feedback["Name"]==nf]
                  print(nfk)
                  nfki=Feedback[Feedback["Name"]==nf].index
                  Feedback.loc[nfki,'Name']=nfr
                  Feedback.to_csv('libd.csv',index=False)
            elif ff==4:
                  print(Feedback)

      elif ch==18:
            uname=input('Enter your name:  ')
            query=input('Enter your query:  ')
            ans='TBD'
            Query_record=pd.DataFrame({'Name':[uname],'Question':[query],'Answer':[ans]})
            Query_record.to_csv('libq.csv',mode='a',index=False,header=None)

      elif ch==19:
            print("1.Show Feedbacks")
            print("2.Show queries")
            Select=int(input('Enter your choice: '))
            if Select==1:
                  Feedback=pd.read_csv('libd.csv')
                  print('You can filter to see your selected feedbacks')
                  print("1 For positive Feedbacks")
                  print("2 For negative Feedbacks")
                  print("3 For Unfiltered Feedbacks")
                  print("4 For Selecting range yourself")
                  print("5 For All")
                  sd=int(input("Select your option:  "))
                  if sd==1:
                        pos='Positive'
                        prev=Feedback[Feedback["User Opinions"]==pos]
                        print(prev)
                  if sd==2:
                        neg='Negative'
                        nrev=Feedback[Feedback["User Opinions"]==neg]
                        print(nrev)
                  if sd==3:
                        print(Feedback)
                  if sd==4:
                        S=int(input("Enter your selected ratings:  "))
                        if S==1:
                              zer=1
                              oneratings=Feedback[Feedback["Ratings"]==zer]
                              print(oneratings)
                        if S==2:
                              tw=2
                              tworatings=Feedback[Feedback["Ratings"]==tw]
                              print(tworatings)
                        if S==3:
                              th=3
                              ratingthree=Feedback[Feedback["Ratings"]==th]
                              print(ratingthree)
                        if S==4:
                              fr=4
                              ratingfour=Feedback[Feedback["Ratings"]==fr]
                              print(ratingfour)
                        if S==5:
                              fv=5
                              ratingfive=Feedback[Feedback["Ratings"]==fv]
                              print(ratingfive)
                        if S==6:
                              sx=6
                              ratingsix=Feedback[Feedback["Ratings"]==sx]
                              print(ratingsix)
                        if S==7:
                              sv=7
                              ratingseven=Feedback[Feedback["Ratings"]==sv]
                              print(ratingseven)
                        if S==8:
                              et=8
                              ratingseight=Feedback[Feedback["Ratings"]==et]
                              print(ratingseight) 
                        if S==9:
                              nn=9
                              ratingsnine=Feedback[Feedback["Ratings"]==nn]
                              print(ratingsnine)
                        if S==10:
                              O=10
                              bestrating=Feedback[Feedback["Ratings"]==O]
                              print(bestrating)
                  if sd==5:
                        print(Feedback)                             
            if Select==2:
                  Query_record=pd.read_csv('libq.csv')
                  print(Query_record)

      elif ch==20:
            print("1.Delete Feedback")
            print("2.Delete Query")
            sc=int(input("Select Your Choice:  "))
            if sc==1:
                  A=input("Enter the  name with which  you wrote the Feedback:  ")
                  Feedback=pd.read_csv("libd.csv")
                  delt=Feedback[Feedback["Name"]==A].index
                  Feedback.drop(delt,inplace=True)
                  Feedback.to_csv("libd.csv",index=False)
                  print("Feedback deleted sucessfully")
            if sc==2:
                  A=input("Enter the  name with which  you wrote the Query:  ")
                  Query_record=pd.read_csv("libq.csv")
                  delt=Query_record[Query_record["Name"]==A].index
                  Query_record.drop(delt,inplace=True)
                  Query_record.to_csv("libq.csv",index=False)
                  print("Query deleted sucessfully")

      elif ch==21:
            print("Help other users by providing them right solution for their problem.")
            Query_record=pd.read_csv('libq.csv')
            print(Query_record)
            qq=input("Enter the name of person whose query you want to answer: ")
            pq=Query_record[Query_record['Name']==qq].index
            answ=input("Please write your answer here:  ")
            Query_record.loc[pq,'Answer']=answ
            Query_record.to_csv('libq.csv',index=False)
            print("Your answer has reached the questioner.")
            print("Thanks for your valuable answer.")

      elif ch==22:
            print("Our team organises a contest every year for the readers.Stand a chance to win prices like:")
            print("1.MacBook")
            print("2.Tablet")
            print("3.IPhone")
            print("4.Cycles")
            print("5.Coupons upto price worth 10000")
            print("Rules:")
            print("A reader has to read upto 1000 books and 250+ articles.The first 5 winners will be awarded.")
            print("Reach any of our center to avail the price")
            print("Here's your chance to avail free 3 Months Membership")
            prize=['Better Luck Next time','Congrats you have grabbed a price']
            value=rand.choice(prize)
            print(value)
            if value=='Congrats you have grabbed a price':
                  coden=['QU','UQ','QK','PU','KS','BP','RU']
                  cr=rand.choice(coden)
                  ar=rand.randint(11,99)
                  code=cr+str(ar)
                  print('Your code is',code)
                  print("Use this code to avail your membership")
            elif value=='Better Luck Next Time':
                  print('Better Luck Next Time')
            
      elif ch==23:
            print("You can contact us through:")
            print("Instagram:OneLibrary")
            print("Facebook:OneLibrary24X7")
            print("Twitter:OneLib18")
            print("Website:www.OneLibrary.com")
            print("Email:OneLibrary@gmail.com")
            print("Phone:883345625,011-223456825")
            print("Helpline No:534")
            

      elif ch==24:
            Date=date.today()
            Memrec=pd.read_csv('lib.csv')
            mem=int(input("Enter the member id: "))
            acx=Memrec[Memrec['Member Id']==mem]
            print(acx)
            F=input("Are you able to see your name(Yes or No): ")
            if F=='No':
                  print(Memrec)
            print("Write your given informations accordingly")
            memb=int(input("Enter the index code given with id: "))
            member_id=Memrec.at[memb,'Member Id']
            member_name=Memrec.at[memb,'Member Name']
            member_phoneno=Memrec.at[memb,'Phone No.']
            features=qrcode.QRCode(version=1,box_size=3.75,border=10)
            features.add_data([member_id,member_name,member_phoneno])
            features.make(fit=True)
            img=features.make_image(fill_color='black',back_color='white')
            font=ImageFont.truetype("Roboto-Light.ttf",size=22)
            template=Image.open('template.jpg')
            Draw=ImageDraw.Draw(template)
            template.paste(img,(392,110))
            Draw.text((135,136),str(member_id),font=font,fill='black')
            Draw.text((85,161),str(member_name),font=font,fill='black')
            Draw.text((120,186),str(member_phoneno),font=font,fill='black')
            Draw.text((120,211),str(Date),font=font,fill='black')
            template.show()
            template.save("Photos/1.jpg")
            img.save("Photos/3.jpg")
            print("Your card is generated and saved successfully")

      elif ch==25:
            print('Thanks.........................visit again')
            break


