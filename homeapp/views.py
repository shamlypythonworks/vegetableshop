from django.shortcuts import render,get_object_or_404,redirect
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.views.generic.list import ListView
# Create your views here.
def homepage(request,c_slug=None):
    catgs = categtable.objects.all()
    if c_slug!=None:
        cat=get_object_or_404(categtable,slug=c_slug)
        prdts=prdttable.objects.all().filter(category=cat,available=True)
    else:
        prdts=prdttable.objects.all().filter(available=True)

    paginator=Paginator(prdts,2)
    try:
      page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(InvalidPage,EmptyPage):
        pro=paginator.page(page.num_pages)

    return render(request, 'index.html', {'catgs':catgs,'prdts': prdts,'pg':pro})

def detailpage(request,c_slug,p_slug):
        try:
            prdts = prdttable.objects.get(category__slug=c_slug,slug=p_slug)
            review = request.POST.get('rev')
            date = request.POST.get('dte')

        except Exception as e:
            raise e
        return render(request,'detail.html',{'pr':prdts,'review':review,'date':date})
def searching(request):
    prod=None
    searchele=None
    if 'q' in request.GET:
        searchele=request.GET.get('q')
        prod= prdttable.objects.all().filter(Q(name__contains=searchele)|Q(desc__contains=searchele))
    return render(request,'search.html',{'qr':searchele,'pr':prod})
def reviewpage(request,p_slug):
    pr = prdttable.objects.get(slug=p_slug)
    return render(request,'review.html',{'pr':pr})
def createsessionid(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id
def wishlist(request,p_slug):
        pdtwsh = prdttable.objects.get(slug=p_slug)
        try:
            wsh_listid = wish_list.objects.get(wshlist_id=createsessionid(request))
        except wish_list.DoesNotExist:
            wsh_listid = wish_list.objects.create(wshlist_id=createsessionid(request))
        wsh_listid.save()
        try:
            wsh_itms = wishlisttable.objects.get(wshlist_kee=wsh_listid, prowishkee=pdtwsh)
        except wishlisttable.DoesNotExist:
            wsh_itms = wishlisttable.objects.create(wshlist_kee=wsh_listid, prowishkee=pdtwsh)
        wsh_itms.save()
        wishitems = wishlisttable.objects.filter(wshlist_kee=wsh_listid)
        return render(request, 'wishlist.html', {'prodts': wishitems})
def remvwshlist(request,p_slug):
    pdtwsh = prdttable.objects.get(slug=p_slug)
    wsh_listid = wish_list.objects.get(wshlist_id=createsessionid(request))
    wsh_itms = get_object_or_404(wishlisttable,wshlist_kee=wsh_listid, prowishkee=pdtwsh)
    wsh_itms.delete()
    return render(request,'wishlist.html')




    # pr = prdttable.objects.get(slug=p_slug)
    # try:
    #     wishitm = wishlisttable.objects.get(wishkee=pr)
    # except:
    #     wishitm = wishlisttable.objects.create(wishkee=pr)
    # wishitm.save()
    # return render(request,'wishlist.html',{'pro':wishitm})

