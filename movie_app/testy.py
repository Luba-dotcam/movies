import pytest
from datetime import datetime

def analyze_pesel(pesel):
	weights = [1, 3, 7, 9,
    1, 3, 7, 9, 1, 3]
	weight_index = 0
	digits_sum = 0
	for digit in pesel[:-1]:
		digits_sum += int(digit) * weights[weight_index]
		weight_index += 1
	pesel_modulo = digits_sum % 10
	validate = 10 - pesel_modulo
	if validate == 10:
		validate = 0
	gender = "male" if int(pesel[-2]) % 2 == 0 else "female"
	birth_date = datetime(int("19" + pesel[0:2]), int(pesel[2:4]), int(pesel[4:6]))
	result = {
    	"pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date
         }
	return result

men = """
53071645254
87042247136
87051495258
55041573972
03282457331""".split()

inmen = """
53071645255
87042247137
87051495259
55041573973
03282457331""".split()

women = """
58122389589
80081328486
79033114383
59112315788
78082981768""".split()


@pytest.mark.parametrize('pesel',
                         men)

def test_returned_pesel_correct_men(pesel):
	value = analyze_pesel(pesel)
	assert value['pesel'] == pesel


@pytest.mark.parametrize('pesel',
                         women)


def test_returned_pesel_correct_women(pesel):
    value = analyze_pesel(pesel)
    assert value['pesel'] == pesel


@pytest.mark.parametrize('pesel',
                         men)
def test_returned_pesel_valid_men(pesel):
    value = analyze_pesel(pesel)
    assert value['valid']


@pytest.mark.parametrize('pesel',
                         women)
def test_returned_pesel_valid_women(pesel):
    value = analyze_pesel(pesel)
    assert value['valid']


@pytest.mark.parametrize('pesel',
                         inmen)
def test_returned_pesel_invalid_men(pesel):
    value = analyze_pesel(pesel)
    assert not value['valid']


@pytest.mark.parametrize('pesel',
                         men)
def test_returned_pesel_men(pesel):
    value = analyze_pesel(pesel)
    assert value['gender'] == 'male'


@pytest.mark.parametrize('pesel, date', [
    ('53071645254', datetime(1953, 7, 16)),
    ('87042247136', datetime(1987, 4, 22)),
    ('87051495258', datetime(1987, 5, 14)),
    ('55041573972', datetime(1955, 4, 15)),
    ('03282457331', datetime(2003, 8, 24)),
    ])
def test_returned_pesel_urodzenie(pesel, date):
    value = analyze_pesel(pesel)
    assert value['birth_date'] == date



def add(a, b):
	return a + b

@pytest.mark.parametrize('a,b,result' , [
	(0,0,0),
	(1,1,2),
	(2,1,3),
	(1,2,3),
	(3,4,7),
	(4,4,8),
	(4,-4,0)

])


def test_add(a,b,result):
	assert add(a, b) == result


def test_add_2_2():
	assert add(2, 2) == 4


def test_add_4_4():
	assert add(4, 4) == 8


def test_add_2_3():
	assert add(2, 3) == 5


def test_add_5_5():
	assert add(5, 5) == 10













