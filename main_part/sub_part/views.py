from django.db.models.aggregates import Count
from django.shortcuts import redirect, render
from . models import contacts, reg,adminreg,equipment,package,category, reservation, users,invoice
import easygui
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def Admin(request):
    return render(request,'AdminLogin.html')

def contact(request):
    return render(request,'contact.html')

def ee(request):
    return render(request,'ee.html')

def faq(request):
    return render(request,'faq.html')

def ff(request):
    return render(request,'ff.html')

def gg(request):
    return render(request,'gg.html')

def hh(request):
    return render(request,'hh.html')


def ind(request):
    return render(request,'ind.html')

def indexx(request):
    return render(request,'indexx.html')

def ll(request):
    return render(request,'ll.html')

def new1(request):
    return render(request,'new1.html')

def new2(request):
    return render(request,'new2.html')

def one(request):
    return render(request,'one.html')

def oo(request):
    return render(request,'oo.html')

def p1(request):
    return render(request,'p1.html')

def p2(request):
    return render(request,'p2.html')

def p3(request):
    return render(request,'p3.html')

def p4(request):
    return render(request,'p4.html')

def p5(request):
    return render(request,'p5.html')

def p6(request):
    return render(request,'p6.html')

def p7(request):
    return render(request,'p7.html')

def p8(request):
    return render(request,'p8.html')

def p9(request):
    return render(request,'p9.html')

def p10(request):
    return render(request,'p10.html')

def p11(request):
    return render(request,'p11.html')

def p12(request):
    return render(request,'p12.html')

def p13(request):
    return render(request,'p13.html')

def p14(request):
    return render(request,'p14.html')

def p15(request):
    return render(request,'p15.html')

def p16(request):
    return render(request,'p16.html')

def p17(request):
    return render(request,'p17.html')

def p18(request):
    return render(request,'p18.html')

def portfolio(request):
    return render(request,'portfolio-1-col.html')

def register(request):
    return render(request,'register.html')

def services(request):
    return render(request,'services.html')

def tee(request):
    return render(request,'tee.html')

def two(request):
    return render(request,'two.html')

def UserLogin(request):
    return render(request,'UserLogin.html')

def adminregister(request):
    return render(request,'adminregister.html')

def reser(request):
    return render(request,'reser.html')

def invo(request):
    return render(request,'invo.html')

def reserv(request):
    return render(request,'reserv.html')

def invoi(request):
    return render(request,'invoi.html')

def logout(request):
    log(request)
    easygui.msgbox("logged out...",title='log out')
    return render(request,'AdminLogin.html')

def logoutuser(request):
    log(request)
    easygui.msgbox("logged out...",title='log out')
    return render(request,'UserLogin.html')

def register(request):
    if request.method=='POST':
        if reg.objects.filter(phone=request.POST['phone']).exists():
            context={'msg':'phone number is already exist'}
            return render(request,'register.html',context)
        elif reg.objects.filter(email=request.POST['email']).exists():
            context1={'msg1':'email is already exist'}
            return render(request,'register.html',context1)
        elif request.method=='POST':    
            ex1=reg(firstname=request.POST['firstname'],
                    lastname=request.POST['lastname'],
                    phone=request.POST['phone'],
                    email=request.POST['email'],
                    psw=request.POST['psw'],
                    )
            ex1.save()
            easygui.msgbox("your registration has been saved successfully.....",title="Registration Form")
            return redirect(UserLogin)

    return render(request,'register.html')

def contact(request):
    if request.method=='POST':
        ex2=contacts(full_name=request.POST['full_name'],
                    phone_number=request.POST['phone_number'],
                    email_id=request.POST['email_id'],
                    message=request.POST['message'])
        ex2.save()
        easygui.msgbox("your message has been send successfully...",title="user message")
        return redirect(contact)

    return render(request,"contact.html")

def adminregister(request):
    if request.method=='POST':
        if adminreg.objects.filter(phone=request.POST['phone']).exists():
            context={'msg':'phone number is already exist'}
            return render(request,'adminregister.html',context)
        elif adminreg.objects.filter(email=request.POST['email']).exists():
            context1={'msg1':'email is already exist'}
            return render(request,'adminregister.html',context1)
        elif request.method=='POST':    
            ex1=adminreg(firstname=request.POST['firstname'],
                lastname=request.POST['lastname'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                psw=request.POST['psw'],
                )
            ex1.save()
            easygui.msgbox("your registration has been saved successfully.....",title=" Admin Registration Form")
            return redirect(Admin)
    return render(request,'adminregister.html')

def UserLogin(request):
    if request.method=='POST':
        if reg.objects.filter(email=request.POST['email'],psw=request.POST['psw']).exists():
            ex1=reg.objects.get(email=request.POST['email'],psw=request.POST['psw'])
            easygui.msgbox("logged successfully....",title="userlogin")
            return render(request,'indexx.html')
        else:
            easygui.msgbox("Invalid Email_id and password")
            return render(request,'UserLogin.html')
    return render(request,'UserLogin.html')

def Admin(request):
    if request.method=='POST':
        if adminreg.objects.filter(email=request.POST['email'],psw=request.POST['psw']).exists():
            ex1=adminreg.objects.get(email=request.POST['email'],psw=request.POST['psw'])
            easygui.msgbox("logged successfully....",title="Adminlogin")
            return render(request,'ind.html',{'ex1':ex1})
        else:
            easygui.msgbox("Invalid Email_id and password")
            return render(request,'AdminLogin.html')
    return render(request,'AdminLogin.html')

def two(request):
    if request.method=='POST':
        ex2=equipment(name=request.POST['name'],
                      equipment=request.POST['equipment'],
                      description=request.POST['description'],
                      category=request.POST['category'],
                      count=request.POST['count'])
        ex2.save()
        easygui.msgbox("your data has been stored successfully")
        return redirect(one)
    return render(request,'two.html')

def one(request):
    ex2=equipment.objects.all()
    return render(request,'one.html',{'ex2':ex2})

def edit_equipment(request,id):
    ex2=equipment.objects.get(id=id)
    return render(request,'edit_equipment.html',{'ex2':ex2})

def update_equipment(request,id):
    ex2=equipment(id=id,name=request.POST['name'],
                      equipment=request.POST['equipment'],
                      description=request.POST['description'],
                      category=request.POST['category'],
                      count=request.POST['count'])
    ex2.save()
    easygui.msgbox("your data has been updated")
    return redirect(one)

def delete_equipment(request,id):
    ex2=equipment.objects.get(id=id)
    ex2.delete()
    easygui.msgbox("your data has been deleted")
    return redirect(one)

def ee(request):
    if request.method=='POST':
        ex3=package(name=request.POST['name'],
                    description=request.POST['description'],
                    items=request.POST['items'],
                    count=request.POST['count'],
                    product=request.POST['product'])
        ex3.save()
        ex3=package.objects.all()
        easygui.msgbox("your data has been stored successfully")
        return redirect(tee)
    return render(request,'ee.html')

def tee(request):
    ex3=package.objects.all()
    return render(request,'tee.html',{'ex3':ex3})

def edit_packages(request,id):
    ex3=package.objects.get(id=id)
    return render(request,'edit_packages.html',{'ex3':ex3})

def update_packages(request,id):
    ex3=package(id=id,name=request.POST['name'],
                    description=request.POST['description'],
                    items=request.POST['items'],
                    count=request.POST['count'],
                    product=request.POST['product'])
    ex3.save()
    easygui.msgbox("your data has been Updated")
    return redirect(tee)

def delete_packages(request,id):
    ex3=package.objects.get(id=id)
    ex3.delete()
    easygui.msgbox("your data has been Deleted")
    return redirect(tee)


def hh(request):
    if request.method=='POST':
        ex4=category(name=request.POST['name'],
                     categories=request.POST['categories'],
                     count=request.POST['count'])
        ex4.save()
        easygui.msgbox("your data has been stored successfully")
        return redirect(ff)
    return render(request,'hh.html')

def ff(request):
    ex4=category.objects.all()
    return render(request,'ff.html',{'ex4':ex4})

def edit_category(request,id):
    ex4=category.objects.get(id=id)
    return render(request,'edit_category.html',{'ex4':ex4})

def update_category(request,id):
    ex4=category(id=id,name=request.POST['name'],
                     categories=request.POST['categories'],
                     count=request.POST['count'])
    ex4.save()
    easygui.msgbox("your data has been Updated")
    return redirect(ff)

def delete_category(request,id):
    ex4=category.objects.get(id=id)
    ex4.delete()
    easygui.msgbox("your data has been Deleted")
    return redirect(ff)


def ll(request):
    if request.method=='POST':
        ex5=users(email=request.POST['email'],
                  password=request.POST['password'],
                  name=request.POST['name'],
                  activation=request.POST['activation'])
        ex5.save()
        easygui.msgbox("your data has been stored successfully")
        return redirect(gg)
    return render(request,'ll.html')

def gg(request):
    ex5=users.objects.all()
    return render(request,'gg.html',{'ex5':ex5})

def edit_user(request,id):
    ex5=users.objects.get(id=id)
    return render(request,'edit_user.html',{'ex5':ex5})

def update_user(request,id):
    ex5=users(id=id,email=request.POST['email'],
                  password=request.POST['password'],
                  name=request.POST['name'],
                  activation=request.POST['activation'])
    ex5.save()
    easygui.msgbox("your data has been Updated")
    return redirect(gg)

def delete_user(request,id):
    ex5=users.objects.get(id=id)
    ex5.delete()
    easygui.msgbox("your data has been Deleted")
    return redirect(gg)


def reserv(request):
    if request.method=='POST':
        ex6=reservation(name=request.POST['name'],
                        payment=request.POST['payment'],
                        price=request.POST['price'],
                        security=request.POST['security'],
                        category=request.POST['category'],
                        count=request.POST['count'])
        ex6.save()
        easygui.msgbox("your data has been stored successfully")
        return redirect(reser)
    return render(request,'reserv.html')

def reser(request):
    ex6=reservation.objects.all()
    return render(request,'reser.html',{'ex6':ex6})

def edit_reservation(request,id):
    ex6=reservation.objects.get(id=id)
    return render(request,'edit_reservation.html',{'ex6':ex6})

def update_reservation(request,id):
    ex6=reservation(id=id,name=request.POST['name'],
                          payment=request.POST['payment'],
                          price=request.POST['price'],
                          security=request.POST['security'],
                          category=request.POST['category'],
                          count=request.POST['count'])
    ex6.save()
    easygui.msgbox("your data has been Updated")
    return redirect(reser)

def delete_reservation(request,id):
    ex6=reservation.objects.get(id=id)
    ex6.delete()
    easygui.msgbox("your data has been Deleted")
    return redirect(reser)

def invoi(request):
    if request.method=='POST':
        ex7=invoice(name=request.POST['name'],
                    product=request.POST['product'],
                    payment=request.POST['payment'],
                    count=request.POST['count'],
                    status=request.POST['status'],
                    category=request.POST['category'],
                    price=request.POST['price'])
        ex7.save()
        easygui.msgbox("your data has been stored successfully",title='invoice data')
        return redirect(invo)
    return render(request,'invoi.html')

def invo(request):
    ex7=invoice.objects.all()
    return render(request,'invo.html',{'ex7':ex7})

def edit_invoices(request,id):
    ex7=invoice.objects.get(id=id)
    return render(request,'edit_invoices.html',{'ex7':ex7})

def update_invoices(request,id):
    ex7=invoice(id=id,name=request.POST['name'],
                    product=request.POST['product'],
                    payment=request.POST['payment'],
                    count=request.POST['count'],
                    status=request.POST['status'],
                    category=request.POST['category'],
                    price=request.POST['price'])
    ex7.save()
    easygui.msgbox("your data has been Updated")
    return redirect(invo)

def delete_invoices(request,id):
    ex7=invoice.objects.get(id=id)
    ex7.delete()
    easygui.msgbox("your data has been Deleted")
    return redirect(invo)