from django.shortcuts import render

# Create your views here.
def recipes(request):
    if request.method == 'POST':
        pass
        # form = LoginForm(request, request.POST)
        # if form.is_valid():
        #     user = form.get_user()
        #     login(request, user)
        #     greetings = "You're Welcome "+user.username
        #     messages.success(request, greetings)
        #     # redirect to home
        #     return redirect('home')
        # else:
        #     messages.error(request, "Invalid Credentials")
    else:
        # form = LoginForm()
        pass

    return render(request, 'recipes/recipes.html')
