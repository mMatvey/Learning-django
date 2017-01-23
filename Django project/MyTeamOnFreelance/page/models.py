from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name

class Good(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название")
    description = models.TextField(verbose_name="Краткое описание")
    category = models.ForeignKey(Category, verbose_name="Категории")
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name="Есть в наличии")
    price = models.FloatField(db_index=True, verbose_name="Цена руб.")

    def __str__(self):
        s = self.name
        if not self.in_stock:
            s += " (нет в наличии)"
            return s

    def save(self, *args, **kwargs):
        # Выполняем дополнительные действия перед сохранением записи

        # Обязательно вызываем метод save родителя,
        # который, собственно, выполняем сохранение записи
        # Если мы этого не сделаем, запись не будет сохранена
        super(Good, self).save(*args, **kwargs)

        # Выполняем какие-либо действия после сохранения записи
    def delete(self, *args, **kwargs):
        # Выполняем дополнительные действия перед удалением записи

        # Обязательно вызываем метод delete родителя
        # иначе запись не будет удалена
        super(Good, self).delete(*args, **kwargs)

        # Выполняем какие-либо действия после удаления записи
    class Meta:
        ordering = ["-price", "name"]
        unique_together = ("category", "name", "price")
        verbose_name = "товар"
        verbose_name_plural = "товары"
