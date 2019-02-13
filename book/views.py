from django.shortcuts import render, redirect
from .forms import Registration, SignInForm ,SellForm
from django.contrib.auth import login, authenticate, logout
from .models import Book , Cart
from django.http import JsonResponse
from django.contrib.auth.models import User



def SignUp(request):
	form=Registration()
	if request.method=='POST':
		form=Registration(request.POST)
		if form.is_valid():
			user=form.save(commit=False)
			user.set_password(user.password)
			user.save()
			login(request,user)
			return redirect('list')

	context={
		'form':form,
	}

	return render(request,'signup.html',context)

def SignIn(request):
	form = SignInForm()
	if request.method=='POST':
		form=SignInForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']

			authuser=authenticate(username=username,password=password)

			if authuser is not None:
				login(request,authuser)
				return redirect('list')

	context={
		'form':form,
	}

	return render(request,'signin.html',context)

def SignOut(request):
	logout(request)
	return redirect('signin')	


def BookList(request):

	books=Book.objects.all()
	bought_by = Cart.objects.filter(user = request.user)
	books_bought = []
	for boughtBook in bought_by:
		book = boughtBook.book
		books_bought.append(book)

	context={
		'books':books,
		'books_bought': books_bought
	}

	return render(request,'list.html',context)

def BookDetail(request,book_id):

	book=Book.objects.get(id=book_id)

	context={
		'book':book,
	}	

	return render(request,'detail.html',context)

def addToCart(request,book_id):
	book = Book.objects.get(id = book_id)
	boughtBook , created = Cart.objects.get_or_create(user = request.user , book = book)
	if created:
		action = 'add'
	else:
		action = 'remove'
		boughtBook.delete()
	response = {
	'action': action
	}
	return JsonResponse(response)

def create(request):
	form = SellForm()
	if request.method == 'POST':
		form = SellForm(request.POST, request.FILES)
		if form.is_valid():
			book = form.save(commit=False)
			book.seller = request.user
			book.save()
			return redirect('list')
	context = {
	'form':form,
	}
	return render(request,'create.html',context)

def update(request, book_id):
	book = Book.objects.get(id = book_id)
	form = SellForm(instance = book)
	if request.method == 'POST':
		form = SellForm(request.POST, instance = book )
		if form.is_valid():

			form.save()
			return redirect('list')
	context = {
	'form':form,
	'book':book,
	}
	return render(request,'update.html',context)

def delete(request,book_id):
	form = Book.objects.get(id = book_id )
	form.delete()
	return redirect('list')

def purchasedBooks(request):
	favs = Cart.objects.filter(user = request.user)
	context = {
	'favs':favs
	}
	return render(request,'purchased.html',context)

def sellerBooks(request):

	mine = Book.objects.filter(seller = request.user)
	context = {
	'mines':mine
	}
	return render(request,'sellerBooks.html',context)



def sellerSoldBooks(request):

	sold_books = Cart.objects.filter( seller= request.user)
	context = {
	'soldBooks':sold_books
	}
	return render(request,'soldBooks.html',context)			










