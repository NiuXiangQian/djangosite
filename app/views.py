from django.core import serializers
from django.shortcuts import render, redirect
from .model.User import User
from django.core.paginator import Paginator, EmptyPage
import json


def index(request):
    return render(request, "index.html")


def to_add(request):
    """
    跳转至添加用户页面
    :param request:
    :return:
    """
    return render(request, "add.html")


def show_all(request):
    """
    显示数据
    :param request:
    :return:
    """
    page_num = int(request.GET.get("pageNum", default=1))
    page_size = int(request.GET.get("pageSize", default=10))
    page_num = page_num if page_num > 1 else 1
    page_size = page_size if page_size > 1 else 10
    res = {}
    rs = User.objects.all()

    ptr = Paginator(rs, page_size)

    res['total'] = ptr.count

    try:
        masters = ptr.page(page_num)
        res['list'] = json.loads(serializers.serialize("json", masters))
    except EmptyPage:
        res['list'] = {}

    res['up'] = page_num - 1
    res['next'] = page_num + 1
    res['total_page'] = int(ptr.count / page_size if ptr.count % page_size == 0 else ptr.count / page_size + 1)
    res['page_size'] = page_size
    res['curr_page'] = page_num
    # 返回json   (rest api)
    # return JsonResponse(res)
    return render(request, "showAll.html", {"res_data": res})


def add_user(request):
    """
    添加一个新用户
    :param request:
    :return:
    """
    gender = request.GET.get("gender", default="F")
    age = int(request.GET.get("age", default=18))
    occupation = int(request.GET.get("occupation", default=1))
    zip_code = request.GET.get("zip_code", default="10000")

    new_user = User(gender=gender, age=age, occupation=occupation, zip_code=zip_code)
    new_user.save()
    print("添加成功")
    return redirect('/app/showAll/')


def to_modify(request):
    """
    跳转至修改页面
    :param request:
    :return:
    """
    id = int(request.GET.get("id"))
    user = User.objects.get(id=id)
    return render(request, "modify.html", {"res_data": user})


def modify_user(request):
    """
    修改用户
    :param request:
    :return:
    """
    id = int(request.POST.get("id"))
    gender = request.POST.get("gender")
    age = int(request.POST.get("age"))
    occupation = int(request.POST.get("occupation"))
    zip_code = request.POST.get("zip_code")

    old_user = User.objects.get(id=id)
    print("找到旧数据%s" % old_user)
    old_user.gender = gender
    old_user.age = age
    old_user.occupation = occupation
    old_user.zip_code = zip_code
    old_user.save()

    return redirect('/app/showAll/')


def del_user(request):
    """
    删除用户
    :param request:
    :return:
    """
    id = int(request.GET.get("id"))
    User.objects.get(id=id).delete()
    return redirect('/app/showAll/')
