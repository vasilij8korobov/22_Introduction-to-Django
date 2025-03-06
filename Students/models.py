from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='Students')

    def __str__(self):
        return self.name

    # first_name = models.CharField(max_length=150, verbose_name="Имя")
    # last_name = models.CharField(max_length=150, verbose_name="Фамилия", unique=True)
    #
    # age = models.IntegerField(help_text='Введите возраст студента')
    # is_active = models.BooleanField(default=True)
    # description = models.TextField(null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='photos/', verbose_name='Фотография')
    """
    Для работы с полем ImageField необходимо установить библиотеку Pillow
    """
    # group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='Students')
    # profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tag)
    #
    # STATUS_CHOICES = [
    #     ('draft', 'Draft'),
    #     ('published', 'Published'),
    # ]
    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    #
    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
    #
    # class Meta:
    #     verbose_name = "студент"
    #     verbose_name_plural = "студенты"
    #     ordering = ["last_name"]
    #     db_table = "custom_table_name"
