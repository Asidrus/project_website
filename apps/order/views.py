from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core.exceptions import BadRequest
from django.views.decorators.csrf import csrf_exempt

from .models import Order, OrderStatus

import requests
from config import TELEGRAMBOT_URL


def index(request):
    return render(request, "order.html", {
        "items": [
            {
                "name": "Pepperoni",
                "description": "Pizza Sauce, Mozzarella and Double Pepperoni",
                "img": "Pepperoni.jpeg"
            },
            {
                "name": "Hawaiian",
                "description": "Pizza sauce, Mozzarella, Ham and Pineapple 🏳️‍🌈",
                "img": "Hawaiian.jpeg"
            },
            {
                "name": "All The Meats",
                "description": "Pizza Sauce, Mozzarella, Bacon, Ham, Spicy Beef, Pepperoni and Pork Sausage",
                "img": "All_The_Meats.jpeg"
            },
            {
                "name": "Special 4 Cheese",
                "description": "Pizza sauce, Mozzarella, Matured, Gouda and Old Amsterdam",
                "img": "Special_4_Cheese.jpeg"
            },
            {
                "name": "Cheese & Tomato",
                "description": "Pizza sauce and Mozzarella",
                "img": "Cheese_&_Tomato.jpeg"
            },
        ],
        "banners": [
            {"img": "Cheese_&_Tomato.jpeg"},
            {"img": "Special_4_Cheese.jpeg"},
            {"img": "Hawaiian.jpeg"}
        ]
    })


@csrf_exempt
def buy(request):
    if request.method == "POST":
        data = request.POST
        order = Order(address=data["address"], phone=data["phone"], pizza=data["pizza"], status=OrderStatus.cooking)
        order.save()
        response = requests.post(TELEGRAMBOT_URL + "/order",
                                 json={"id": order.id, "address": order.address,
                                       "phone": order.phone, "status": order.status.value})

        return JsonResponse({"orderID": order.id, "status": order.status.value})
    else:
        return BadRequest("Support only POST request")


def get_status(request):
    data = request.GET
    objects = Order.objects.all().filter(id=data["orderID"])
    return JsonResponse({"status": OrderStatus[objects[0].status.split(".")[-1]].value})


@csrf_exempt
def update_status(request):
    data = request.POST
    objects = Order.objects.get(id=data["orderID"])
    objects.status = data["status"]
    objects.save()
    return HttpResponse()
