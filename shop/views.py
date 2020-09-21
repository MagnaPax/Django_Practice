from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from shop.models import Product


def product_list(request):
    count = Product.objects.count()
    productList = Product.objects.order_by("-product_id")

    return render(request, 'shop/product_list.html', {'productList': productList, 'count': count})



def product_write(request):
    return render(request, "shop/product_write.html")


UPLOAD_DIR ="/home/kosmo1/PycharmProjects/myweb/shop/static/images/"

@csrf_exempt
def product_insert(request):
    # 첨부 파일이 존재 한다면 ...
    if "file1" in request.FILES:
        # 파일 이름
        file = request.FILES["file1"]
        file_name = file.name
        fp = open("%s%s"%(UPLOAD_DIR, file_name), "wb")
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
    else:
        file_name="-"
    dto = Product(product_name=request.POST["product_name"],
                  description=request.POST["description"],
                  price=request.POST["price"],
                  picture_url=file_name)
    dto.save()
    return redirect("/shop/shoplist")


def product_detail(request):
    idx = request.GET["product_id"]

    product_detail = Product.objects.get(product_id=idx)
    print(product_detail.product_id)
    print(product_detail.product_name)
    return render(request, "shop/product_detail.html",{"dto":product_detail})
