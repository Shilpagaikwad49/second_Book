from django.shortcuts import render,redirect
from BookApp.models import Book

# Create your views here.

def homePage(request):
    #fetching the data
    data = Book.objects.all()
    context = {}
    context["books"] = data
    return render(request,'home.html',context)


def addbook(request):
    if request.method=='GET':
        return render(request,'addbook.html')
    else:
        t= request.POST['title']
        a= request.POST['author']
        p= request.POST['price']
        
        b=Book.objects.create(title = t, author = a , price = p)
        b.save()
        
        # print(t,a,p)
        # return render(request,'home.html')
         
        # print("Added book: ",name,price,author)
        # return render(request,'home.html') #returns empty page no data
        # redirects to home with data
           
        
        # feating data
        # data = Book.objects.all()
        # context ={}
        # context['books']=data
        # return render(request,'home.html',context) 
        return redirect('/home')
    
def deleteBook(request,bookid):
    # print("Deleted book id: ",bookid)
    b=Book.objects.filter(id=bookid)
    b.delete()
    # return render(request,'home.html')
    return redirect('/home')

def updateBook(request,bookid):
    if request.method=="GET":
        print("Update Book id: ",bookid)
        b=Book.objects.filter(id=bookid)
        '''
        b is  queryset and it can have
        all boook objects returned by database, based on condition
        we are filtering book data based on PK:'id',so there will be only 1 book object.
        that book object is present at index 0, so we need to send b[0] to template
        '''
        # print(b[0].title)
        context={}
        context['book']=b[0]
        return render(request,'updatebook.html',context)
    else:
        #Fetch the data
        t=request.POST['title']
        p=request.POST['price']
        a=request.POST['author']
        b=Book.objects.filter(id=bookid)
        b.update(title=t,author=a,price=p)
        return redirect('/home')


        
        

      
        
    
