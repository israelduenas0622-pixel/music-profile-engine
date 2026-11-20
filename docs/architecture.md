# Architecture

## Data

- `biblioteca`: list of songs.
- `historial`: list of user reactions to songs.
- `puntaje_reaccion`: dictionary that assigns a numerical score to each reaction type.

## Functions

### Persistence

#### `guardar_historial(historial)`
- Receives: reaction history.
- Does: saves the history to `historial.json`.
- Returns: nothing.

#### `cargar_historial()`
- Receives: nothing.
- Does: loads the saved history from `historial.json`.
- Returns: reaction history.

### Display

#### `mostrar_ficha(cancion)`
- Receives: one song.
- Does: displays the song title, artists, genres, album, and year.
- Returns: nothing.

### Analysis

#### `perfil_generos(historial, biblioteca)`
- Receives: reaction history and song library.
- Does: converts each reaction into a score and accumulates those scores by genre.
- Returns: a dictionary with the weighted score for each genre.

### Search

#### `buscar_artista(biblioteca, artista_buscado)`
- Receives: song library and an artist name.
- Does: searches the library for songs by that artist.
- Returns: a list of matching songs.

#### `buscar_cancion(biblioteca, titulo_buscado)`
- Receives: song library and a song title.
- Does: searches the library for a song with that title.
- Returns: a list containing the matching song, or an empty list.

#### `buscar_genero(biblioteca, genero_buscado)`
- Receives: song library and a genre.
- Does: searches the library for songs belonging to that genre.
- Returns: a list of matching songs.

### User Interaction

#### `reaccion(historial, cancion)`
- Receives: reaction history and one song.
- Does: asks the user for a reaction to the song and adds that reaction to the history.
- Modifies: `historial`.
- Returns: nothing.

## Flow

1. The program asks the user what they want to search for:
   - Artist
   - Song
   - Genre

2. Based on the selected option, the program asks for:
   - an artist name,
   - a song title,
   - or a genre.

3. The corresponding search function is called:
   - `buscar_artista()`
   - `buscar_cancion()`
   - `buscar_genero()`

4. If matching songs are found, the program:
   - displays each song using `mostrar_ficha()`,
   - asks the user for a reaction using `reaccion()`.

5. The reaction is added to `historial`.

6. The history is saved to `historial.json` using `guardar_historial()`.

7. `perfil_generos()` uses the reaction history and song library to calculate weighted genre scores.

8. The resulting genre scores represent the user's current music preference profile.