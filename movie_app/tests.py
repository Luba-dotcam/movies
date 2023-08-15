import pytest
from django.test import Client
# Create your tests here.
from django.urls import reverse

from movie_app.forms import AddMovieModelForm, AddReviewForm
from movie_app.models import Genre, Person, Movie, Review
from movie_app.views import AddReviewToMovieView


def test_index():
    url = reverse('index')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200
    assert 'Witaj' in str(response.content)


@pytest.mark.django_db
def test_person_list_view(persons):
    url = reverse('person_list')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['persons'].count() == len(persons)
    for person in persons:
        assert person in response.context['persons']


@pytest.mark.django_db
def test_person_detail_view(person):
    url = reverse('person_detail', kwargs={'id': person.id})
    clinet = Client()
    response = clinet.get(url)
    assert response.status_code == 200
    assert response.context['person'] == person


@pytest.mark.django_db
def test_add_genre_view(user):
    url = reverse('add_genre')
    client = Client()
    client.force_login(user)
    dane = {'name':'komedia'}
    response = client.post(url, dane)
    assert response.status_code == 302
    Genre.objects.get(name='komedia')


@pytest.mark.django_db
def test_add_person():
    url = reverse('add_person')
    client = Client()
    dane = {
        'first_name': 'x',
        'last_name': 'x'
    }
    response = client.post(url, dane)
    assert response.status_code == 302
    Person.objects.get(**dane)


@pytest.mark.django_db
def test_Add_movie_get_not_login():
    url = reverse('add_movie_model_form_view')
    client = Client()
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))



@pytest.mark.django_db
def test_Add_movie_get(user):
    url = reverse('add_movie_model_form_view')
    client = Client()
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], AddMovieModelForm)


@pytest.mark.django_db
def test_add_movie(user, persons, genres):
    url = reverse('add_movie_model_form_view')
    client = Client()
    client.force_login(user)
    dane = {
        'title': 'gumise',
        'year': 1999,
        'director': persons[0].id,
        'screenplay': persons[0].id,
        'genres':[x.id for x in genres]
    }
    response = client.post(url, dane)
    assert response.status_code == 302
    del dane['genres']
    m = Movie.objects.get(**dane)
    assert m.genres.count() == len(genres)
    for genre in genres:
        assert genre in m.genres.all()


@pytest.mark.django_db
def test_add_review_get_login(user):
    url = reverse('add_review')
    client = Client()
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['add_review'], AddReviewToMovieView)


@pytest.mark.django_db
def test_add_review_to_movie_get(movie, user):
    url = reverse('add_review', kwargs={'id_movie': movie.id})
    client = Client()
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], AddReviewForm)


@pytest.mark.django_db
def test_add_review_to_movie(movie, user):
    url = reverse('add_review', kwargs={'id_movie':movie.id})
    client = Client()
    client.force_login(user)
    dane = {
        'text':'lorem ipsum'
    }
    response = client.post(url. dane)
    assert response.status_code == 302
    r = Review.objects.get(**dane)
    assert r.movie == movie
    assert r.user == user














