from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def home(request): 
    peoples = [ 
        {'name' : 'Subhan' , 'age' : 19} , 
        {'name' : 'Sufyan' , 'age' : 16} ,
        {'name' : 'Zain' , 'age' : 22} ,
        {'name' : 'Asif' , 'age' : 14} ,
        {'name' : 'Ahmed' , 'age' : 30} 

    ]
    text = """
    loremjiu7327u32yqhsabnsbdsjduwywuqy78268i3y2uu2y3u26382jhwsjsxslkapqiwoquiwiq
    """
    vegetables = ['pumpkin' , 'tomato' , 'potato']
    return render(request , "index.html" , context = {'peoples' : peoples , 'text' : text , 
    'vegetables': vegetables})

def success_page(request) : 
    print("subhan")
    return HttpResponse("<h1> Hey! This is a success page") 
def about(request) : 
    context = {'page': 'About'}
    print("subhan")
    return render(request , "about.html" , context )
def contact(request) : 
    context = {'page': 'Contact'}
    print("subhan")
    return render(request , "contact.html" , context )

