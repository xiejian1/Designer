
import os
from flaskdemo import app
from flaskdemo.controller.admin import  PictureEdit, Foodedit
from flaskdemo.controller.contentedit import ContentEdit, ImageUpload, EditeUpload
from flaskdemo.controller.demo import ShowUsers, JsonTest, JsonData, UserView
from flaskdemo.controller.entity import createtable, add, delete, update
from flaskdemo.controller.food import Foodlist, Fooddetail, Vegetablelist, Snacklist, Snackdetail, Souplist, Soupdetail
from flaskdemo.controller.meat import Meatlist, Meatdetail, Meatslist, Meatsdetail, Dessertlist, Dessertdetail, \
    Noodleslist, Noodlesdetail
from flaskdemo.controller.pictrue import Pictruelist, Picturedetail, Palettelist, Palettedetail
from flaskdemo.controller.test import Upload,Yulan, Multiple, EditerUplaod


BASE_DIR = os.path.abspath(os.path.dirname(__name__))



def main():
    app.add_url_rule(rule='/upload/', view_func=Upload.as_view('upload'))
    app.add_url_rule(rule='/yulan/', view_func=Yulan.as_view('yulan'))
    app.add_url_rule(rule='/editerUplaod/', view_func=EditerUplaod.as_view('editer'))
    app.add_url_rule(rule='/multiple/', view_func=Multiple.as_view('multiple'))

    app.add_url_rule(rule='/', view_func=ShowUsers.as_view('index'))
    app.add_url_rule(rule='/food/home/', view_func=Foodlist.as_view('foodlist'))
    app.add_url_rule(rule='/food/meat/',view_func=Meatlist.as_view('meatlist'))
    app.add_url_rule(rule='/food/meats/', view_func=Meatslist.as_view('meatslist'))
    app.add_url_rule(rule='/food/vegetable/', view_func=Vegetablelist.as_view('vegetablelist'))
    app.add_url_rule(rule='/food/snack/', view_func=Snacklist.as_view('snacklist'))
    app.add_url_rule(rule='/food/soup/', view_func=Souplist.as_view('souplist'))
    app.add_url_rule(rule='/food/dessert/', view_func=Dessertlist.as_view('dessertlist'))
    app.add_url_rule(rule='/food/noodles/', view_func=Noodleslist.as_view('noodleslist'))
    app.add_url_rule(rule='/meatdetail/<string:id>',view_func=Meatdetail.as_view('meatdetail'))
    app.add_url_rule(rule='/meatsdetail/<string:id>', view_func=Meatsdetail.as_view('meatsdetail'))
    app.add_url_rule(rule='/fooddetail/<string:id>', view_func=Fooddetail.as_view('fooddetail'))
    app.add_url_rule(rule='/vegetabledetail/<string:id>', view_func=Meatdetail.as_view('vegetabledetail'))
    app.add_url_rule(rule='/snackdetail/<string:id>', view_func=Snackdetail.as_view('snackdetail'))
    app.add_url_rule(rule='/soupdetail/<string:id>', view_func=Soupdetail.as_view('soupdetail'))
    app.add_url_rule(rule='/dessertdetail/<string:id>', view_func=Dessertdetail.as_view('dessertdetail'))
    app.add_url_rule(rule='/noodlesdetail/<string:id>', view_func=Noodlesdetail.as_view('noodlesdetail'))

    app.add_url_rule(rule='/picture/cutout/', view_func=Pictruelist.as_view('pictruelist'))
    app.add_url_rule(rule='/picturedetail/<string:id>', view_func=Picturedetail.as_view('picturedetail'))
    app.add_url_rule(rule='/picture/palette/',view_func=Palettelist.as_view('palettelist'))
    app.add_url_rule(rule='/palettedetail/<string:id>',view_func=Palettedetail.as_view('palettedetail'))


    app.add_url_rule(rule='/admin/', view_func=Foodedit.as_view('admin'))
    app.add_url_rule(rule='/pictureedit/', view_func=PictureEdit.as_view('pictureedit'))
    app.add_url_rule(rule='/contentedit/<string:type>/<string:id>', view_func=ContentEdit.as_view('contentedit'))
    app.add_url_rule(rule='/editeupload/', view_func=EditeUpload.as_view('editupload'))
    app.add_url_rule(rule='/imageupload/', view_func=ImageUpload.as_view('imageupload'))

    app.add_url_rule(rule='/jsontest/', view_func=JsonTest.as_view('json_test'))
    app.add_url_rule(rule='/json/', view_func=JsonData.as_view('json_demo'))
    app.add_url_rule(rule='/list/', view_func=UserView.as_view('list_users'))
    app.add_url_rule(rule='/db/', view_func=createtable.as_view('createtable'))
    app.add_url_rule(rule='/add/', view_func=add.as_view('add'))
    app.add_url_rule(rule='/delete/', view_func=delete.as_view('delate'))
    app.add_url_rule(rule='/update/', view_func=update.as_view('update'))

    app.run(debug=True, host='localhost', port=8000)


if __name__ == "__main__":
   main()