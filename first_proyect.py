

DATA = [
    {
        'name': 'Facundo',
        'age': 32,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def position_selection(Datas):
    works=['Language Maker', 'Human Resources Manager', 'Student', 'Support', 'Backend Developer','Associate', 'QA Manager','UX Designer','Technical Coach']

    selection=int(input('Seleccione el trabajo que busca:\n1)Language Maker\n2)Human Resources Manager\n3)Student\n4)Support\n5)Backend Developer\n6)Associate\n7)QA Manager\n8)UX Designer\n9)Technical Coach\n: '))

    selection_ = works[selection-1]

    all_workers=[worker['name'] for worker in Datas if worker['position']==selection_]
    print(all_workers)


def fix_words(word): 
    word=word.capitalize()
    word=word.replace(' ','')
    return word


def all_python(Datas):   
    all=[workers['name'] for workers in Datas if workers['language']=='python']
    print(all)


def all_work(Datas):
        empresa=fix_words(input('Ingrese la empresa que desee ver: '))
        all= [worker['name'] for worker in Datas if worker['organization'] == empresa]
        print(all)


def all_positions(datas):
    position=input('Ingrese la posicion que desea ver: ')
    all=[worker['name'] for worker in datas if worker['position'] == position ]
    print(position)
    print(all)


def run():
    position_selection(DATA)
    # all_work(DATA)
    # all_python(DATA)

if __name__=='__main__':
    run()