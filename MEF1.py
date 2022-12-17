class Restik(): #создание классв
    def __init__(self, restik_name, prometasin_type): #краткое описание касса с методом инит
        self.name = restik_name #атрибут
        self.type = prometasin_type #атрибут
    def describe_restik(self): #спец метод
        print("The restik name is:" + self.name) #вывод текста с атрибутом
        print("The restik type is:" + self.type.title()) #тоже самое что и пред
    def open_restik(self): #спец метод
        print("Open") #сообщение о том что рестик открыт
restik = Restik(" KFC", " chicken") #вызов метода инит
restik.describe_restik() #обращение к значению атрибута
restik.open_restik() #тоже самое что и пред