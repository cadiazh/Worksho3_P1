import numpy as np
import random
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Muestra películas al azar y sus embeddings"

    def handle(self, *args, **kwargs):
        movies = list(Movie.objects.all())

        if not movies:
            self.stdout.write("❌ No hay películas en la base de datos.")
            return

        # Elegimos cuántas películas mostrar
        num_random = min(5, len(movies))  # muestra 5 o menos si hay pocas
        selected_movies = random.sample(movies, num_random)

        self.stdout.write(f"🎲 Mostrando {num_random} películas seleccionadas al azar:\n")

        for movie in selected_movies:
            emb = np.frombuffer(movie.emb, dtype=np.float32)
            self.stdout.write(self.style.SUCCESS(f"🎬 {movie.title}"))
            self.stdout.write(f"🧠 Embedding (primeros 10 valores): {emb[:10]}\n")
