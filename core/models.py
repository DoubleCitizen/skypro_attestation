from django.db import models


class Contact(models.Model):
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    email = models.EmailField()
    country = models.CharField(max_length=30, verbose_name="Страна")
    city = models.CharField(max_length=30, verbose_name="Город")
    street = models.CharField(max_length=30, verbose_name="Улица")
    house_number = models.IntegerField(verbose_name="Номер дома")

    def __str__(self):
        return f"{self.email}"


class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField(max_length=80, verbose_name="Имя продукта")
    model = models.CharField(max_length=100, verbose_name="Модель продукта")
    release_date = models.DateField(verbose_name="Дата выпуска")

    def __str__(self):
        return f"{self.name} {self.model}"


class Factory(models.Model):
    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"

    name = models.CharField(verbose_name="Название завода", max_length=50)
    contacts = models.ManyToManyField(Contact, verbose_name="Данные контактов")
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    country = models.CharField(max_length=30, verbose_name="Страна")
    city = models.CharField(max_length=30, verbose_name="Город")
    street = models.CharField(max_length=30, verbose_name="Улица")
    house_number = models.IntegerField(verbose_name="Номер дома")

    def __str__(self):
        return f"{self.name}"


class RetailChain(models.Model):
    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"

    name = models.CharField(verbose_name="Имя крупной розничной сети", max_length=50)
    contacts = models.ManyToManyField(Contact, verbose_name="Данные контактов")
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    supplier = models.ForeignKey(Factory, verbose_name="Поставщик", on_delete=models.CASCADE)
    debt = models.FloatField(verbose_name="Задолженность перед поставщиком")
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    country = models.CharField(max_length=30, verbose_name="Страна")
    city = models.CharField(max_length=30, verbose_name="Город")
    street = models.CharField(max_length=30, verbose_name="Улица")
    house_number = models.IntegerField(verbose_name="Номер дома")

    def __str__(self):
        return f"Розничная сеть {self.name}"


class IndividualEntrepreneur(models.Model):
    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"

    name = models.CharField(verbose_name="Имя индивидуально предпринимателя", max_length=50)
    contacts = models.ManyToManyField(Contact, verbose_name="Данные контактов")
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    supplier = models.ForeignKey(RetailChain, verbose_name="Поставщик", on_delete=models.CASCADE)
    debt = models.FloatField(verbose_name="Задолженность перед поставщиком")
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    country = models.CharField(max_length=30, verbose_name="Страна")
    city = models.CharField(max_length=30, verbose_name="Город")
    street = models.CharField(max_length=30, verbose_name="Улица")
    house_number = models.IntegerField(verbose_name="Номер дома")

    def __str__(self):
        return f"ИП {self.name}"
