from django.db import models
from django.urls import reverse
from django.templatetags.static import static
from colorfield.fields import ColorField


class ModelWithTimestamps(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(ModelWithTimestamps):
    name = models.CharField(max_length=200)
    text_color = ColorField(blank=True)
    background_color = ColorField(blank=True)

    def __str__(self):
        return self.name


class Asset(ModelWithTimestamps):
    name = models.CharField(max_length=200)
    source = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)

    attribution_required = models.BooleanField(default=False)
    attribution_text = models.TextField(blank=True)

    type = models.CharField(max_length=10, choices=(
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('text', 'Snippet'),
        ('texture', 'Texture'),
        ('model', 'Model'),
    ))

    tags = models.ManyToManyField(Tag, blank=True)

    @property
    def versions(self):
        if self.type == 'image':
            return self.imageasset_set
        elif self.type == 'audio':
            return self.audioasset_set
        elif self.type == 'video':
            return self.videoasset_set
        elif self.type == 'text':
            return self.textasset_set
        elif self.type == 'texture':
            return self.textureasset_set
        elif self.type == 'model':
            return self.modelasset_set

    @property
    def current_version(self):
        return self.versions.latest('number')

    def get_absolute_url(self):
        return reverse("asset-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.name}"


def get_asset_upload_directory(instance, name):
    return f"assets/{instance.upload_folder}/{name}"

def get_thumb_upload_directory(instance, name):
    return f"thumbs/{instance.upload_folder}/{name}"

class Version(ModelWithTimestamps):
    class Meta:
        abstract = True

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

    number = models.PositiveIntegerField()
    file = models.FileField(upload_to=get_asset_upload_directory)
    notes = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to=get_thumb_upload_directory, blank=True)
    
    preview_image = "/default_images/generic.png"
    def get_preview_image(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return static(self.preview_image)

    def __str__(self) -> str:
        return f"{self.asset.name} version #{self.number}"


class ImageAsset(Version):
    file = models.ImageField(upload_to="assets/images/")
    thumbnail = None
    def get_preview_image(self):
        return self.file.url


class VideoAsset(Version):
    upload_folder = "videos"
    preview_image = "/default_images/video.png"



class AudioAsset(Version):
    upload_folder = "audios"
    preview_image = "/default_images/audio.png"


class TextAsset(Version):
    file = None
    text = models.TextField()
    syntax_highlighting_language = models.CharField(
        max_length=100, blank=True,
        help_text="Uses Prism.js to render. Refer to https://prismjs.com/#supported-languages for the value for this box"
    )
    upload_folder = "text"
    preview_image = "/default_images/text.png"
    def __str__(self) -> str:
        return f"{self.asset.name} version #{self.number}"


class TextureAsset(Version):
    upload_folder = "textures"
    preview_image = "/default_images/texture.png"


class ModelAsset(Version):
    upload_folder = "models"
    preview_image = "/default_images/model.png"
    preview_model = models.FileField(upload_to="assets/preview_model/", blank=True)