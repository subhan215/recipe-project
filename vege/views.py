from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/login/")
def allRecipes(request) : 
    querySet = Recipe.objects.all()
    ifSearch = False ; 
    if request.GET.get('search'):
        querySet = querySet.filter(recipeName__icontains=request.GET.get('search'))
        ifSearch = True
    context = {'recipes' : querySet , 'ifSearch' : ifSearch}
    return render(request , 'allRecipes.html' , context)




@login_required(login_url="/login/")
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipeName = data.get('recipeName')
        recipeDescription = data.get('recipeDescription')
        recipeImage = request.FILES.get('recipeImage')
        print(recipeName)
        print(recipeDescription)
        print(recipeImage)
        Recipe.objects.create(
            recipeImage=recipeImage,
            recipeDescription=recipeDescription,
            recipeName=recipeName
        )
        return redirect('/recipes/')
    querySet = Recipe.objects.all()
    ifSearch = False ; 
    if request.GET.get('search'):
        querySet = querySet.filter(recipeName__icontains=request.GET.get('search'))
        ifSearch = True
        con = {'recipes' : querySet , 'ifSearch' : ifSearch}
        return render(request , 'allRecipes.html' , con)
    context = {'recipes': querySet}
    return render(request, 'recipes.html', context)




@login_required(login_url="/login/")
def delRecipe(request , id):
    querySet = Recipe.objects.get(id = id)
    querySet.delete()
    return redirect('/allRecipes/')

@login_required(login_url="/login/")
def updRecipe(request, id):
    querySet = Recipe.objects.get(id=id)
    
    if request.method == "POST":
        data = request.POST
        recipeImage = request.FILES.get('recipeImage')
        recipeName = data.get('recipeName')
        recipeDescription = data.get('recipeDescription')
        
        querySet.recipeName = recipeName
        querySet.recipeDescription = recipeDescription
        
        if recipeImage:
            querySet.recipeImage = recipeImage

        querySet.save()
        return redirect('/allRecipes/')

    context = {'recipe': querySet}
    return render(request, 'updateRecipes.html', context)

def logInPage(request) : 
     if request.method == "POST" : 
        userName = request.POST.get('userName')
        password = request.POST.get('password')

        if not User.objects.filter(username = userName).exists() : 
            messages.error(request , 'Invalid Username!')
            return redirect('/login/')
        
        user = authenticate(username = userName , password = password)

        if user is None: 
            messages.error(request , 'Invalid Password!')
            return redirect('/login/')
        
        else: 
            login(request ,user)
            return redirect('/recipes/')
     
     
     
     return render(request , 'login.html') 


@login_required(login_url="/login/")
def logOutPage(request) : 
     logout(request)
     return redirect('/login/')    


def register(request) : 
    if request.method == "POST" : 
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        userName = request.POST.get('userName')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = userName)
        if user.exists() : 
            messages.error(request , 'username already exists')
            return redirect('/register/')
        user = User.objects.create(
            first_name = firstName , 
            last_name = lastName , 
            username = userName
        )
        user.set_password(password)
        user.save()
        
        messages.info(request , 'Account Created Successfully!')
        return redirect('/register/')
    
    return render(request , 'register.html')     


