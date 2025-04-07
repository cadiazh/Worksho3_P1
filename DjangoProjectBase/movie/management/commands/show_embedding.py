import numpy as np
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Mostrar los primeros valores del embedding de cada película"

    def handle(self, *args, **kwargs):
        for movie in Movie.objects.all():
            try:
                emb = np.frombuffer(movie.emb, dtype=np.float32)
                self.stdout.write(f"{movie.title}: {emb[:5]}")
            except Exception as e:
                self.stderr.write(f"❌ Error al leer el embedding de {movie.title}: {e}")
