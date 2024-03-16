from django.shortcuts import render,redirect
from .models import Person
# Create your views here.
def home_page(req):
    people=Person.objects.all()
    stx={
        "people":people
    }
    return render(req,"home.html",stx)
def fill_page(req):
    if req.method == "POST":
        name=req.POST.get("name")
        lastname=req.POST.get("last_name")
        age=req.POST.get("age")
        gender=req.POST.get("gender")
        email=req.POST.get("email")
        pr_lng=req.POST.get("prog_lang")
        st_da=req.POST.get("start_date")
        con=req.POST.get("confirm")
        if not con:
            con=False
        else:
            con=True
        Person.objects.create(
            email=email,
            name=name,
            last_name=lastname,
            age=age,
            gender=gender,
            prog_lang=pr_lng,
            start_date=st_da,
            confirm=con
        )
        return redirect("home")
    else:
        return render(req,"fill.html")
def edit_page(req,person_id):
    person=Person.objects.get(id=person_id)
    if req.method == "GET":
        stx={
            "person":person,
        }
        return render(req,"edit.html",stx)
    else:
        person.name = req.POST.get("name")
        person.last_name=req.POST.get("last_name")
        person.age=req.POST.get("age")
        person.gender=req.POST.get("gender")
        person.email=req.POST.get("email")
        person.prog_lang=req.POST.get("prog_lang")
        person.start_date=req.POST.get("start_date")
        person.confirm=req.POST.get("confirm")=="on"

        person.save()
        return redirect("home")
def delete_page(req,person_id):
    person=Person.objects.get(id=person_id)
    stx={
        "person":person,

    }
    return render(req,"delete.html",stx)
def confirm_delete(req,person_id):
    person=Person.objects.get(id=person_id)
    person.delete()
    return redirect('home')