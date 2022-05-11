import wikipedia
import utils
import wikipediaapi
from tqdm import tqdm
import pickle
from nltk.corpus import wordnet as wn

wiki_wiki = wikipediaapi.Wikipedia('en')

parent_priority = ['table lamp', 'boxer', 'junco', 'Maltese', 'Papillon', 'Dalmatian', 'Pomeranian', 'ladybug', 'birdhouse', 'brass memorial plaque', 'breakwater', 'one-piece bathing suit', 'moving van', 'Windsor tie']
non_first_indices = {'goblet': 1, 'baby bib': 1, 'langur': 1, 'storage chest': 1, 'music speaker': 1, 'milk can': 1, 'product packet / packaging': 2, 'snorkel': 2, 'sweatshirt': 1, 'tea cup': 2, }
string_priority_definitions = {'tool kit': 'A set of tools kept together, especially comprising all the tools suitable for some particular type of work.'}
string_priority_search_pages = {'plate rack': 'Dish drying cabinet', 'soda bottle': 'Two-liter bottle', 'soup bowl': 'bowl', 'lakeshore': 'Shore', 'airplane wing': 'Wing', 'pole': 'Utility pole', 'drink pitcher': 'Pitcher (container)'}

wikipedia_contexts_by_class = {}

for class_name in tqdm(utils.imagenet_classes()):
    classname_synset = utils.imagenet_class_to_synset(class_name)
    classname_synset = wn.synset_from_pos_and_offset('n', int(classname_synset[1:]))
    parent_synset_name = str(classname_synset.hypernyms()[0].name())
    parent = parent_synset_name[ : parent_synset_name.find('.')].replace('_', ' ')

    search_space_parent = wikipedia.search(class_name+' '+parent)
    search_space = wikipedia.search(class_name)

    name = search_space[0].encode('utf-8') 
    if(class_name in non_first_indices):
        name = search_space[non_first_indices[class_name]].encode('utf-8')

    if(class_name in string_priority_search_pages):
        name = string_priority_search_pages[class_name]
    
    if(class_name in string_priority_definitions):
        res = string_priority_definitions[class_name]
   
    try:
        res = wikipedia.summary(title=name).encode('utf-8')
    except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError) as e:
        page_py = wiki_wiki.page(name)    
        res = page_py.summary.encode('utf-8')

    wikipedia_contexts_by_class[class_name] = res
pickle.dump(wikipedia_contexts_by_class, open('./wikipedia_contexts_by_imagenet_class.pickle', 'wb'))