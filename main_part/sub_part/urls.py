from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('Admin',views.Admin,name='Admin'),
    path('contact',views.contact,name='contact'),
    path('ee',views.ee,name='ee'),
    path('faq',views.faq,name='faq'),
    path('ff',views.ff,name='ff'),
    path('gg',views.gg,name='gg'),
    path('hh',views.hh,name='hh'),
    path('ind',views.ind,name='ind'),
    path('indexx',views.indexx,name='indexx'),
    path('invo',views.invo,name='invo'),
    path('ll',views.ll,name='ll'),
    path('new1',views.new1,name='new1'),
    path('new2',views.new2,name='new2'),
    path('one',views.one,name='one'),
    path('oo',views.oo,name='oo'),
    path('p1',views.p1,name='p1'),
    path('p2',views.p2,name='p2'),
    path('p3',views.p3,name='p3'),
    path('p4',views.p4,name='p4'),
    path('p5',views.p5,name='p5'),
    path('p6',views.p6,name='p6'),
    path('p7',views.p7,name='p7'),
    path('p8',views.p8,name='p8'),
    path('p9',views.p9,name='p9'),
    path('p10',views.p10,name='p10'),
    path('p11',views.p11,name='p11'),
    path('p12',views.p12,name='p12'),
    path('p13',views.p13,name='p13'),
    path('p14',views.p14,name='p14'),
    path('p15',views.p15,name='p15'),
    path('p16',views.p16,name='p16'),
    path('p17',views.p17,name='p17'),
    path('p18',views.p18,name='p18'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('register',views.register,name='register'),
    path('services',views.services,name='services'),
    path('tee',views.tee,name='tee'),
    path('two',views.two,name='two'),
    path('UserLogin',views.UserLogin,name='UserLogin'),
    path('adminregister',views.adminregister,name='adminregister'),
    path('register',views.register,name='register'),
    path('reser',views.reser,name='reser'),
    path('contact',views.contact,name='contact'),
    path('UserLogin',views.UserLogin,name='UserLogin'),
    path('Admin',views.Admin,name='Admin'),
    path('two',views.two,name='two'),
    path('ee',views.ee,name='ee'),
    path('hh',views.hh,name='hh'),
    path('ll',views.ll,name='ll'),
    path('reserv',views.reserv,name='reserv'), 
    path('invoi',views.invoi,name='invoi'),
    path('logout',views.logout,name='logout'),
    path('logoutuser',views.logoutuser,name='logoutuser'),
    path('edit_reservation/<int:id>',views.edit_reservation,name='edit_reservation'),
    path('update_reservation/<int:id>',views.update_reservation,name='update_reservation'),
    path('delete_reservation/<int:id>',views.delete_reservation,name='delete_reservation'),
    path('edit_invoices/<int:id>',views.edit_invoices,name='edit_invoices'),
    path('update_invoices/<int:id>',views.update_invoices,name='update_invoices'),
    path('delete_invoices/<int:id>',views.delete_invoices,name='delete_invoices'),
    path('edit_packages/<int:id>',views.edit_packages,name='edit_packages'),
    path('update_packages/<int:id>',views.update_packages,name='update_packages'),
    path('delete_packages/<int:id>',views.delete_packages,name='delete_packages'),
    path('edit_category/<int:id>',views.edit_category,name='edit_category'),
    path('update_category/<int:id>',views.update_category,name='update_category'),
    path('delete_category/<int:id>',views.delete_category,name='delete_category'),
    path('edit_user/<int:id>',views.edit_user,name='edit_user'),
    path('update_user/<int:id>',views.update_user,name='update_user'),
    path('delete_user/<int:id>',views.delete_user,name='delete_user'),
    path('edit_equipment/<int:id>',views.edit_equipment,name='edit_equipment'),
    path('update_equipment/<int:id>',views.update_equipment,name='update_equipment'),
    path('delete_equipment/<int:id>',views.delete_equipment,name='delete_equipment')
    
    


]