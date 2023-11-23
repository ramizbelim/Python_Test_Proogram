demo_dict = {
    'South Africa': {
        'Western Cape': {
            'Waterkloof': [1],
            'Cape Town': [1, 2],
            'Swellendam': [1, 2, 3],
            'Limpopo': {
                'Polokwane': [1],
                'Louis Trichardt': [1, 2],
                'Modimolle': [1, 2, 3]
            },
            'Mpumalanga': {
                'eNtokozweni': [1],
                'Mbombela': [1, 2],
                'Lydenburg': [1, 2, 3]
            },
            'Eastern Cape': {
                'Bisho': [1],
                'Kareedouw': [1, 2],
                'Gqeberha': [1, 2, 3]
            },
            'Northern Cape': {
                'Kuruman': [1],
                'Kimberley': [1, 2],
                'Jan Kempdorp': [1, 2, 3]
            }
        }
    },
    'France': {
        'Normandie': {
            'Rouen': [1],
            'Caen': [1, 2],
            'Saint-Lô': [1, 2, 3]
        },
        'Brittany': {
            'Saint-Malo': [1],
            'Quimper': [1, 2],
            'Brest': [1, 2, 3]
        },
        'Corsica': {
            'Porto-Vecchio': [1],
            'Bonifacio': [1, 2],
            'Sartène': [1, 2, 3]
        },
        'Alsace': {
            'Riquewihr': [1],
            'Colmar': [1, 2],
            'Bergheim': [1, 2, 3]
        }
    },
    'China': {
        'Xinjiang': {
            'Korla': [1],
            'Aksu City': [1, 2],
            'Hami': [1, 2, 3]
        },
        'Zhejiang': {
            'Hangzhou': [1],
            'Jinhua': [1, 2],
            'Taizhou': [1, 2, 3]
        },
        'Jiangsu': {
            'Xuzhou': [1],
            'Zhenjiang': [1, 2],
            'Nanjing': [1, 2, 3]
        },
        'Fujian': {
            'Quanzhou': [1],
            'Fuzhou': [1, 2],
            'Putian': [1, 2, 3]
        }
    }
}
def sort_dictionary(dictionary):
    x = lambda key : key[0]
    sorted_dictionary = sorted(dictionary,key=x)
    return sorted_dictionary
print(sort_dictionary(demo_dict))


