#string are not mutable types so had to change all to lists to get to work...would like to know if it works without changing
tech_birthdays = {
    'Douglas Adams': ['03/11/1952'],
    'Paul Allen': ['01/21/1953'],
    'Marc Andreessen': ['07/09/1971'],
    'Steve Ballmer': ['06/14/1946'],
    'Sergey Brin': ['08/21/1973'],
    'Steve Case': ['08/21/1958'],
    'Martin Cooper': ['12/26/1928'],
    'Mark Cuban': ['07/31/1958'],
    'Michael Dell': ['02/23/1965'],
    'Larry Ellison': ['08/17/1944'],
    'Bill Gates': ['10/28/1955'],
    'Alexander Graham Bell': ['03/03/1847'],
    'Reed Hastings': ['08/08/1960'],
    'Bill Hewlett': ['05/20/1913'],
    'Edwin Hubble': ['11/20/1889'],
    'Chad Hurley': ['01/01/1977'],
    'Thomas Watson': ['02/17/1874'],
    'Steve Jobs': ['02/24/1955'],
    'Bill Joy': ['11/08/1954'],
    'Guy Kawasaki': ['08/30/1954'],
    'Sarah Lane': ['10/12/1976'],
    'Paul Maritz': ['01/01/1955'],
    'Leo Mechelin': ['11/24/1839'],
    'Robert Noyce': ['12/12/1927'],
    'David Packard': ['09/07/1912'],
    'Larry Page': ['03/26/1973'],
    'Robert Pittman': ['12/28/1953'],
    'Dennis Ritchie': ['09/09/1941'],
    'Jerry Sanders': ['09/12/1936'],
    'Alan Shugart': ['09/27/1930'],
    'Richard Stallman': ['03/16/1953'],
    'Nikola Tesla': ['07/10/1890'],
    'Guido van Rossum': ['01/31/1956'],
    'Masayuki Uemura': ['06/20/1943'],
    'Jimmy Wales': ['08/07/1966'],
    'Mark Zuckerberg': ['05/14/1984'],
    'Steve Wozniak': ['08/11/1950'],
    'Jerry Yang': ['11/06/1968'],
    'Tim Berners-Lee': ['06/08/1955']
}

# 1 show birthday of person name entered
print('Welcome to fun with tech guys please follow directions.')
print('type the names of famous tech individuals to see there birthdays (wow how cool)')
print('type done when you do not want to do that any more')
while True:
    askForName = input('tech persons name (case sensitive) : ')
    if askForName in tech_birthdays:
        print(askForName, 'birthday is ', tech_birthdays[askForName])
    elif askForName == 'done':
        print('Thanks for searching my tech guys dictionary, bye.')
        break
    else:
        print('that person is not part of the list')


# 2 add values to dict
def add_values_in_dict(sample_dict, key, list_of_values):
    """append multiple values to a key in the given dictionary"""
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


add_values_in_dict(tech_birthdays, 'Jeff Bezos', ['01/12/1964', 'Amazon Founder', 'Amazon Kindle'])
add_values_in_dict(tech_birthdays, 'Tim Cook', ['11/1/1960', 'Apple', 'current CEO'])
add_values_in_dict(tech_birthdays, 'Jack Dorsey', ['11/19/1976', 'Twitter', 'Co Founder and CEO of Twitter'])
add_values_in_dict(tech_birthdays, 'Henry Blodget',
                   ['1966', 'Business Insider', 'banned from involement in securities industry'])
add_values_in_dict(tech_birthdays, 'Jawed Karim', ['10/28/1979', 'Youtube', 'first video posted to youtube'])

print(tech_birthdays)

# 3 use add values function to add company worked for and one invention or innovation they are know for
add_values_in_dict(tech_birthdays, 'Douglas Adams', ['writer', 'hitchhikers guid to the galaxy']) #1
add_values_in_dict(tech_birthdays, 'Paul Allen', ['Microsoft', 'in international space hall of fame'])
add_values_in_dict(tech_birthdays, 'Marc Andreessen', ['Opsware', 'Mosian - web browser'])
add_values_in_dict(tech_birthdays, 'Steve Ballmer', ['Microsoft', 'owns clippers'])
add_values_in_dict(tech_birthdays, 'Sergey Brin', ['Google', 'page rank']) #5
add_values_in_dict(tech_birthdays, 'Steve Case', ['AOL', 'social media/quantum link'])
add_values_in_dict(tech_birthdays, 'Martin Cooper', ['Dyna LLC', 'wireless communication/father of handheld cell phone'])
add_values_in_dict(tech_birthdays, 'Mark Cuban', ['2929 Entertainment', 'broadcast.com'])
add_values_in_dict(tech_birthdays, 'Michael Dell', ['Dell', 'build personal computers'])
add_values_in_dict(tech_birthdays, 'Larry Ellison', ['Oracle', 'oracle']) #10
add_values_in_dict(tech_birthdays, 'Bill Gates', ['Microsoft', 'operating system/programmable computer'])
add_values_in_dict(tech_birthdays, 'Alexander Graham Bell', ['inventor', 'telephone'])
add_values_in_dict(tech_birthdays, 'Reed Hastings', ['Netflix', 'video streaming/chaos monkey'])
add_values_in_dict(tech_birthdays, 'Bill Hewlett', ['Hewlett Packard Company', 'computer parts'])
add_values_in_dict(tech_birthdays, 'Edwin Hubble', ['scientist', 'hubbles law']) #15
add_values_in_dict(tech_birthdays, 'Chad Hurley', ['Youtube', 'tagging and video sharing'])
add_values_in_dict(tech_birthdays, 'Thomas Watson', ['IBM', ' punched card tabulating machines'])
add_values_in_dict(tech_birthdays, 'Steve Jobs', ['Apple', 'iPhone'])
add_values_in_dict(tech_birthdays, 'Bill Joy', ['Sun Microsystems', 'BSD UNIX'])
add_values_in_dict(tech_birthdays, 'Guy Kawasaki', ['Apple', 'database software 4th Dimension']) #20
add_values_in_dict(tech_birthdays, 'Sarah Lane', ['Daily Tech News Show', 'media creator'])
add_values_in_dict(tech_birthdays, 'Paul Maritz', ['Pivotal Software', 'desktop and server software for microsoft'])
add_values_in_dict(tech_birthdays, 'Leo Mechelin', ['Nokia', 'mobil phones'])
add_values_in_dict(tech_birthdays, 'Robert Noyce', ['Fairchild Semiconductor/Intel', ' monolithic integrated circuit or microchip'])
add_values_in_dict(tech_birthdays, 'David Packard', ['Hewlett Packard Company', 'computer parts']) #25
add_values_in_dict(tech_birthdays, 'Larry Page', ['Google', 'page rank'])
add_values_in_dict(tech_birthdays, 'Robert Pittman', ['MTV Networks', 'radio and tv programmer'])
add_values_in_dict(tech_birthdays, 'Dennis Ritchie', ['programmer', 'C programming language creator'])
add_values_in_dict(tech_birthdays, 'Jerry Sanders', ['AMD', 'computer parts'])
add_values_in_dict(tech_birthdays, 'Alan Shugart', ['XEROX', ' IEEE Reynold B. Johnson Information Storage Systems Award']) #30
add_values_in_dict(tech_birthdays, 'Richard Stallman', ['Free Software Foundation', 'GNU project'])
add_values_in_dict(tech_birthdays, 'Nikola Tesla', ['inventor', 'AC current'])
add_values_in_dict(tech_birthdays, 'Guido van Rossum', ['programmer', 'python'])
add_values_in_dict(tech_birthdays, 'Masayuki Uemura', ['nintendo', 'RandD of nintendo hardware'])
add_values_in_dict(tech_birthdays, 'Jimmy Wales', ['Wikipedia', 'wikipedia']) #35
add_values_in_dict(tech_birthdays, 'Mark Zuckerberg', ['Facebook', 'wrote facebook code'])
add_values_in_dict(tech_birthdays, 'Steve Wozniak', ['Apple', 'apple 1 computer'])
add_values_in_dict(tech_birthdays, 'Jerry Yang', ['Yahoo', 'Search'])
add_values_in_dict(tech_birthdays, 'Tim Berners-Lee', ['programmer', 'world wide web'])

print(tech_birthdays)