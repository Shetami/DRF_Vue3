from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from fiches import upload


class Tag(models.Model):
    title = models.CharField("Название", max_length=50)
    slug = models.SlugField("URL", max_length=50)

    def __str__(self):
        return self.title


class MangaSeries(models.Model):
    title = models.CharField("Название серии", max_length=100)
    slug = models.SlugField("Url", max_length=100)

    def __str__(self):
        return self.title


class MangaTitle(models.Model):
    series = models.ForeignKey(MangaSeries, on_delete=models.CASCADE, related_name="series")
    title = models.CharField("Названия тайтла", max_length=100)
    slug = models.SlugField("Url", max_length=100, unique=True)
    image = models.ImageField("Постер", upload_to="posters/", blank=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    rating = models.FloatField(max_length=10)


class Author(models.Model):
    name = models.CharField("Автор", max_length=50, unique=True)
    slug = models.SlugField("URL", max_length=50, unique=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    language = models.CharField("Язык", max_length=20)

    def __str__(self):
        return self.language


class Character(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")

    def __str__(self):
        return self.name


class Post(models.Model):
    manga_title = models.ForeignKey(MangaTitle, on_delete=models.CASCADE, related_name="post", verbose_name="Название тайтла")
    title = models.CharField("Название", max_length=50)
    slug = models.SlugField("URL", max_length=50, unique=True)
    image = models.ImageField("Постер", upload_to="posters/post", blank=True)
    tags = models.ManyToManyField(Tag, max_length=50)
    author = models.OneToOneField(Author, on_delete=models.SET_NULL, related_name="author", verbose_name="Автор", null=True)
    language = models.OneToOneField(Language, on_delete=models.SET_NULL, verbose_name="Язык", related_name="languages", null=True)
    characters = models.ManyToManyField(Character, verbose_name="Герой")
    description = models.TextField("Описание", max_length=500)
    rating = models.OneToOneField(Rating, on_delete=models.CASCADE)
    reviews = models.TextField(max_length=250, verbose_name="Отзывы")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('manga_detail', kwargs={'slug': self.slug})

    def get_absolute_url_1(self):
        return reverse('manga_slider', kwargs={'manga_slug': self.slug})


class Page(models.Model):
    page = models.ImageField(upload_to=upload)
    manga = models.ForeignKey(Post, related_name="manga", on_delete=models.SET_NULL, null=True)

    def page_url(self):
        return mark_safe(
            f'<img src="{self.page.url}" width="100px" height="200px"')  # Тут делаю вывод картинки для админки


class Favorites(models.Model):
    manga = models.ForeignKey(Post, on_delete=models.SET_NULL, related_name="Манга", null=True)
    slug = models.SlugField("URL", max_length=50)



