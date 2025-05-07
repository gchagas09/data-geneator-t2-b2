import ArtistGenerator as ag
import json
artistas_gerados = ag.generate_artists()
artistas = artistas_gerados[0]

print(json.dumps(artistas, indent=2, ensure_ascii=False))

