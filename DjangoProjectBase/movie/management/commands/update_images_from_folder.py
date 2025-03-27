import os
from django.core.management.base import BaseCommand
from movie.models import Movie
from django.conf import settings

class Command(BaseCommand):
    help = "Update movie images from a folder"

    def handle(self, *args, **kwargs):
        # 📁 Ruta de la carpeta donde están las imágenes
        image_folder = os.path.join(settings.MEDIA_ROOT, 'movie/images')

        # ✅ Verifica si la carpeta existe
        if not os.path.exists(image_folder):
            self.stderr.write(self.style.ERROR(f"Folder '{image_folder}' not found."))
            return

        updated_count = 0

        # 🔍 Recorre todas las películas en la base de datos
        for movie in Movie.objects.all():
            image_filename = f"m_{movie.title}.png"  # 📌 Formato del nombre de archivo
            image_path = os.path.join(image_folder, image_filename)

            # 📷 Verifica si la imagen existe
            if os.path.exists(image_path):
                # Actualiza la ruta de la imagen en la BD
                movie.image = f"movie/images/{image_filename}"
                movie.save()
                updated_count += 1
                self.stdout.write(self.style.SUCCESS(f"Updated image for: {movie.title}"))
            else:
                self.stderr.write(self.style.WARNING(f"Image not found for: {movie.title}"))

        # 🏁 Muestra el resumen final
        self.stdout.write(self.style.SUCCESS(f"Finished updating {updated_count} movie images."))
