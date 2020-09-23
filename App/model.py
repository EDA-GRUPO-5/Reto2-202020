"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

Se define la estructura de un catálogo de libros.
El catálogo tendrá  una lista para los libros.

Los autores, los tags y los años se guardaran en
tablas de simbolos.
"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------


def newCatalogDetails():

    catalog = { 'id': None,
                'budget': None,
                'genres': None,
                'imdb_id': None,
                'original_language': None,
                'original_title': None,
                'overview': None,
                'popularity': None,
                'production_companies': None,
                'production_countries': None,
                'release_date': None,
                'revenue': None,
                'runtime': None,
                'spoken_languages': None,
                'status': None,
                'tagline': None,
                'title': None,
                'vote_average': None,
                'vote_count': None,
                'production_companies_number': None,
                'production_countries_number': None,
                'spoken_languages_number': None} 
                
    catalog['id'] = lt.newList('SINGLE_LINKED', compareBookIds)
    catalog['budget'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['genres'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['imbd_id'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['original_languaje'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['original_title'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['overview'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['popularity'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['production_companies'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['production_countries'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['release_date'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['revenue'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['spoken_languages'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['status'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['tagline'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['title'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['vote_average'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['vote_count'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['production_companies_number'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['production_countries_number'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['spoken_languages_number'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)

    return catalog

def newCatalogCasting():

    catalog = { 'id': None,
                'actor1_name': None,
                'actor1_gender': None,
                'actor2_name': None,
                'actor2_gender': None,
                'actor3_name': None,
                'actor3_gender': None,
                'actor4_name': None,
                'actor4_gender': None,
                'actor5_name': None,
                'actor5_gender': None,
                'actor_number': None,
                'director_name': None,
                'director_gender': None,
                'producer_name': None,
                'director_number': None,
                'producer_number': None,
                'screeplay_name': None,
                'editor_name': None}

    catalog['id'] = lt.newList('SINGLE_LINKED', compareBookIds)
    catalog['actor1_name'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['actor1_gender'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['actor2_name'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['actor2_gender'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['actor3_name'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['actor3_gender'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['actor4_name'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['actor4_gender'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['actor5_name'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['actor5_gender'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['actor_number'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['director_name'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['director_gender'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['producer_name'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['director_number'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['producer_number'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['screeplay_name'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['editor_name'] = mp.newMap(4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    
    return catalog


def newAuthor(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    author = {'name': "", "books": None,  "average_rating": 0}
    author['name'] = name
    author['books'] = lt.newList('SINGLE_LINKED', compareAuthorsByName)
    return author


def newTagBook(name, id):
    """
    Esta estructura crea una relación entre un tag y los libros que han sido
    marcados con dicho tag.  Se guarga el total de libros y una lista con
    dichos libros.
    """
    tag = {'name': '',
           'tag_id': '',
           'total_books': 0,
           'books': None,
           'count': 0.0}
    tag['name'] = name
    tag['tag_id'] = id
    tag['books'] = lt.newList()
    return tag


# Funciones para agregar informacion al catalogo

def addMovie(catalogCast, catalogoDet, movie):
    """
    Esta funcion adiciona una pelicula a la lista de peliculas,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Crea una entrada en el Map de Años, para indicar que esta pelicula
    fue publicada en ese año
    """
    lt.addLast(catalogCast['id'], movie)
    lt.addLast(catalogoDet['id'], movie)

    mp.put(catalogoDet['title'], movie['imdb_id'], movie)
    #mp.put(catalogoDet['title'], movie['id'], movie)
    #mp.put(catalogoCast['title'], movie['id'], movie)
    
    
def addBook(catalog, movie):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['id'], movie)
    mp.put(catalog['id'], movie['goodreads_book_id'], movie)
    addBookYear(catalog, movie)


def addBookYear(catalog, book):
    """
    Esta funcion adiciona un libro a la lista de libros que
    fueron publicados en un año especifico.
    Los años se guardan en un Map, donde la llave es el año
    y el valor la lista de libros de ese año.
    """
    years = catalog['years']
    pubyear = book['original_publication_year']
    pubyear = int(float(pubyear))
    existyear = mp.contains(years, pubyear)
    if existyear:
        entry = mp.get(years, pubyear)
        year = me.getValue(entry)
    else:
        year = newYear(pubyear)
        mp.put(years, pubyear, year)
    lt.addLast(year['books'], book)


def newYear(pubyear):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'year': "", "books": None}
    entry['year'] = pubyear
    entry['books'] = lt.newList('SINGLE_LINKED', compareYears)
    return entry


def addBookAuthor(catalog, authorname, book):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    authors = catalog['authors']
    existauthor = mp.contains(authors, authorname)
    if existauthor:
        entry = mp.get(authors, authorname)
        author = me.getValue(entry)
    else:
        author = newAuthor(authorname)
        mp.put(authors, authorname, author)
    lt.addLast(author['books'], book)

    authavg = author['average_rating']
    bookavg = book['average_rating']
    if (authavg == 0.0):
        author['average_rating'] = float(bookavg)
    else:
        author['average_rating'] = (authavg + float(bookavg)) / 2


def addTag(catalog, tag):
    """
    Adiciona un tag a la tabla de tags dentro del catalogo
    """
    newtag = newTagBook(tag['tag_name'], tag['tag_id'])
    mp.put(catalog['tags'], tag['tag_name'], newtag)
    mp.put(catalog['tagIds'], tag['tag_id'], newtag)


def addBookTag(catalog, tag):
    """
    Agrega una relación entre un libro y un tag.
    Para ello se adiciona el libro a la lista de libros
    del tag.
    """
    bookid = tag['goodreads_book_id']
    tagid = tag['tag_id']
    entry = mp.get(catalog['tagIds'], tagid)

    if entry:
        tagbook = mp.get(catalog['tags'], me.getValue(entry)['name'])
        tagbook['value']['total_books'] += 1
        tagbook['value']['count'] += int(tag['count'])
        book = mp.get(catalog['bookIds'], bookid)
        if book:
            lt.addLast(tagbook['value']['books'], book['value'])


# ==============================
# Funciones de consulta
# ==============================


def getBooksByAuthor(catalog, authorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    author = mp.get(catalog['authors'], authorname)
    if author:
        return me.getValue(author)
    return None


def getBooksByTag(catalog, tagname):
    """
    Retornar la lista de libros asociados a un tag
    """
    tag = mp.get(catalog['tags'], tagname)
    books = None
    if tag:
        books = me.getValue(tag)['books']
    return books


def booksSize(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog['books'])


def authorsSize(catalog):
    """
    Numero de autores en el catalogo
    """
    return mp.size(catalog['authors'])


def tagsSize(catalog):
    """
    Numero de tags en el catalogo
    """
    return mp.size(catalog['tags'])


def getBooksByYear(catalog, year):
    """
    Retorna los libros publicados en un año
    """
    year = mp.get(catalog['years'], year)
    if year:
        return me.getValue(year)['books']
    return None


# ==============================
# Funciones de Comparacion
# ==============================

def compareProductionCompanies(id, tag):
    """
    Compara dos ids de compañias productoras
    """
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return -1


def compareBookIds(id1, id2):
    """
    Compara dos ids de libros
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareMapBookIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1


def compareAuthorsByName(keyname, author):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(author)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1


def compareTagNames(name, tag):
    tagentry = me.getKey(tag)
    if (name == tagentry):
        return 0
    elif (name > tagentry):
        return 1
    else:
        return -1


def compareTagIds(id, tag):
    tagentry = me.getKey(tag)
    if (int(id) == int(tagentry)):
        return 0
    elif (int(id) > int(tagentry)):
        return 1
    else:
        return 0


def compareMapYear(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0


def compareYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return 0
