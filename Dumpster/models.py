from django.db import models
from django.urls import reverse


class ModelWithTimestamps(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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

class Version(ModelWithTimestamps):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

    number = models.PositiveIntegerField()
    file = models.FileField(upload_to=get_asset_upload_directory)
    notes = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.asset.name} version #{self.number}"


class ImageAsset(Version):
    upload_folder = "images"


class VideoAsset(Version):
    upload_folder = "videos"


class AudioAsset(Version):
    upload_folder = "audios"


class TextAsset(ModelWithTimestamps):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

    number = models.PositiveIntegerField()
    text = models.TextField()
    notes = models.TextField(blank=True)
    syntax_highlighting_language = models.CharField(
        max_length=100, blank=True,
        help_text="Uses Prism.js to render. Refer to https://prismjs.com/#supported-languages for the value for this box"
    )
    def __str__(self) -> str:
        return f"{self.asset.name} version #{self.number}"


class TextureAsset(Version):
    upload_folder = "textures"


class ModelAsset(Version):
    upload_folder = "models"
