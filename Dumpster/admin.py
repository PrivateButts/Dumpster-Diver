from django.contrib import admin

from . import models


@admin.register(models.Asset)
class AssetAdmin(admin.ModelAdmin):
    model = models.Asset


@admin.register(models.ImageAsset)
class ImageAssetAdmin(admin.ModelAdmin):
    model = models.ImageAsset


@admin.register(models.VideoAsset)
class VideoAssetAdmin(admin.ModelAdmin):
    model = models.VideoAsset


@admin.register(models.AudioAsset)
class AudioAssetAdmin(admin.ModelAdmin):
    model = models.AudioAsset


@admin.register(models.TextAsset)
class TextAssetAdmin(admin.ModelAdmin):
    model = models.TextAsset


@admin.register(models.TextureAsset)
class TextureAssetAdmin(admin.ModelAdmin):
    model = models.TextureAsset


@admin.register(models.ModelAsset)
class ModelAssetAdmin(admin.ModelAdmin):
    model = models.ModelAsset
