from django.shortcuts import render
from shop_app.models import Product, Client, Maillot, Comment
from shop_app.forms import CommentForm
import datetime


def index(request):
	products = Product.objects.all()
	return render(request, 'index.html', context={'products': products })

def product(request, product_id):
	product = Product.objects.get(id=product_id)
	comments = Comment.objects.all().filter(product_id=product_id)
	return render(request, 'product.html', context={'product': product, 'comments': comments })



def clients(request):
	clients = Client.objects.all()
	return render(request, 'clients.html', context={'clients': clients })



def client(request, client_id):
	client = Client.objects.get(id=client_id)
	return render(request, 'client.html', context={'client': client })


def maillots(request):
	maillots = Maillot.objects.all()
	return render(request, 'maillots.html', context={'maillots': maillots })


def maillot(request, maillot_id):
	maillot = Maillot.objects.get(id=maillot_id)
	return render(request, 'maillot.html', context={'maillot': maillot })


def comments(request):
	comments = Comment.objects.all()
	return render(request, 'comments.html', context={'comments': comments })

def comment(request, comment_id):
	comment = Comment.objects.get(id=comment_id)
	return render(request, 'comment.html', context={'comment': comment })




def comment_form(request, product_id):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        text = request.POST.get('text')
        print(text)
        product = Product.objects.get(id=product_id)
        date = datetime.datetime.now()
        comment = Comment.objects.get_or_create(username=username, text=text, product=product, date=date)


    return render(request, 'comment_form.html', context={ 'comment_form': CommentForm() })




