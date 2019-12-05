from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
def home(request):
    products=Product.objects
    return render(request,'products/index.html',{'products':products})
@login_required(login_url="/accounts/signup")
def create(request):
    if request.method=="POST":
            product=Product()
            product.title=request.POST['title']
            product.body=request.POST['summary']
            product.url=request.POST['url']
            product.icon=request.FILES['icon']
            product.image=request.FILES['image']
            product.publicationDate=timezone.datetime.now()
            product.hunter=request.user
            product.save()
            return redirect('/products/' + str(product.id))
    else:
        return render(request,'products/CreateProduct.html')
def detail(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request,'products/ProductDetail.html',{'product':product})
@login_required(login_url="/accounts/signup")
def upvote(request,product_id):
    if request.method=="POST":
        product=get_object_or_404(Product,pk=product_id)
        product.votes_total+=1
        product.save()
        return redirect('/products/' + str(product.id))
@login_required(login_url="/accounts/signup")
def downvote(request,product_id):
    if request.method=="POST":
        product=get_object_or_404(Product,pk=product_id)
        product.votes_total-=1
        product.save()
        return redirect('/products/' + str(product.id))
