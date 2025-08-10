from django.db import models

class Book(models.Model):
    title = models.CharField("Название", max_length=70)
    author = models.CharField("Автор", max_length=70)
    description = models.TextField("Описание")
    ageLimit = models.IntegerField("Возрастное ограничение")
    kolPages = models.IntegerField("Количество страниц")
    publishing = models.CharField("Издательство", max_length=70)
    yearPublication = models.DateField("Дата издания")
    image=models.ImageField("Изображение", upload_to="images/")
    bookFile=models.FileField("Файл", upload_to="books/")

    class Meta:
        verbose_name='Книга'
        verbose_name_plural='Книги'

    def __str__(self):
        return self.title

class Genre(models.Model):
    title = models.CharField("Название", max_length=70)
    description = models.TextField("Описание")

    class Meta:
        verbose_name='Жанр'
        verbose_name_plural='Жанры'

    def __str__(self):
        return self.title

class NDS(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    percentNDS = models.IntegerField("Процент НДС")
    type = models.CharField("Вид ставки", max_length=70)
    priceWithNDS = models.DecimalField("Цена с учетом НДС", decimal_places=2, max_digits=9)
    priceNoNDS = models.DecimalField("Цена без учета НДС", decimal_places=2, max_digits=9)

    class Meta:
        verbose_name='НДС книги'
        verbose_name_plural='НДС книг'

    def __str__(self):
        return self.book.title

class BookGenre(models.Model):
    Book = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.CASCADE)
    Genre = models.ForeignKey(Genre, verbose_name='Жанр', on_delete=models.CASCADE)

    class Meta:
        verbose_name='Жанры книги'
        verbose_name_plural='Жанры книг'

    def __str__(self):
        return self.Book.title