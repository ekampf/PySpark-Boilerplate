import re
from functools import partial
from shared.context import JobContext

__author__ = 'ekampf'

class WordCountJobContext(JobContext):
    def _init_accumulators(self, sc):
        self.initalize_counter(sc, 'words')


strip_regexp = re.compile(r"[^\w]*")

def to_pairs(context, word):
    context.inc_counter('words')
    return word, 1


def analyze(sc):
    print "Running wordcount"
    context = WordCountJobContext(sc)

    text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum at condimentum augue. Sed a massa convallis, rhoncus felis sed, fringilla lacus. Sed tristique nulla sem, ut egestas erat consequat sed. Duis ultrices nulla eu elit consectetur elementum. Vivamus pharetra erat sit amet quam tincidunt efficitur. Aenean fringilla convallis ipsum, eu dapibus lorem congue sit amet. Nam vehicula, nibh vitae semper tincidunt, nisl augue lobortis nisl, ut efficitur velit ligula vitae leo. Duis vel augue auctor, rhoncus mi et, rhoncus nisi. Vivamus aliquam sagittis laoreet. Mauris non elementum metus. Donec sagittis, diam eget feugiat suscipit, dolor tortor dignissim tellus, sed luctus augue odio vel sapien. Sed eleifend lectus a sem maximus viverra. Proin eu nulla nulla. Quisque suscipit lacinia arcu, ac suscipit diam malesuada sed. Curabitur vel iaculis erat, non ultricies mi.
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Fusce et iaculis tortor. Pellentesque tempus pellentesque hendrerit. Etiam non lacinia justo, nec placerat lacus. Sed tellus tellus, hendrerit vitae massa non, facilisis eleifend sem. Etiam id metus dolor. Aliquam rutrum eros eu ante sodales pharetra. Phasellus faucibus sapien vitae justo interdum, in eleifend felis malesuada. In commodo est nec sapien tincidunt facilisis. Curabitur tempor tincidunt nibh, ut pharetra libero ornare quis. Ut egestas felis sed lacus vestibulum porttitor. Fusce lacinia eros nec odio vulputate egestas. Fusce pharetra nisl sed dui fermentum dignissim. Nullam id scelerisque mi. Nunc libero nisi, suscipit vel tortor in, pulvinar rutrum sapien.
Nam id mattis erat. Nam condimentum mollis ex, in eleifend orci. Donec accumsan mollis luctus. In id purus semper metus vestibulum cursus. Nullam leo sem, rutrum tempor pharetra in, lobortis nec dolor. Fusce dignissim, arcu ac finibus rutrum, sapien massa rhoncus eros, sit amet ornare justo arcu vel risus. Phasellus vel lorem vitae arcu dictum aliquam non ac metus. Curabitur interdum mattis velit eu venenatis. Nunc lobortis lorem quis ante pretium tempus. Sed auctor dui magna, a tincidunt turpis vehicula a. Integer porttitor eleifend sapien ut commodo.
Curabitur molestie lorem nec risus vestibulum, commodo finibus mauris eleifend. Nullam eleifend vel risus in malesuada. Fusce vitae leo mattis, dictum augue vitae, mollis massa. Quisque mollis, augue eu ullamcorper semper, ligula neque porta nunc, in blandit dolor mauris nec nulla. Aliquam ut sodales purus. Nullam sed ex a orci fringilla tempus ut ut sem. Nam imperdiet neque ex, non iaculis lacus commodo et. Curabitur mauris mauris, interdum eget purus et, facilisis ornare lectus. Etiam luctus sollicitudin aliquet. Nulla mauris leo, aliquam et hendrerit eget, gravida eu lorem.
Integer nibh ante, facilisis ut dignissim id, tristique eget sem. Nulla at nulla ut elit porta luctus quis ut augue. Sed vel sem eu felis lobortis feugiat sed consectetur justo. Sed semper velit id risus gravida consectetur et ac elit. Suspendisse euismod cursus elit ac semper. Vivamus nec urna quis eros semper maximus. Ut ipsum metus, condimentum dictum aliquet vel, tincidunt et nisi.
Cras dignissim mollis nunc, quis aliquam leo scelerisque quis. Aenean egestas nulla vitae justo ultrices, quis tincidunt nisi finibus. Nunc vel dolor scelerisque, sodales diam sed, tempus urna. Donec porta justo eget molestie sodales. Duis in dapibus lacus. Ut tempor laoreet ultricies. In hac habitasse platea dictumst. Curabitur mauris lorem, molestie eget arcu nec, congue faucibus purus. Duis quis tincidunt arcu. Nullam feugiat ultricies libero, dapibus dictum purus aliquet dictum. Ut elementum enim eu enim commodo ornare. Fusce nibh odio, ornare ut imperdiet ut, viverra at odio. Nulla tortor risus, mattis nec sagittis vel, gravida eu nisl. Nunc luctus egestas sem et tincidunt. Donec vitae malesuada felis, ut aliquet ante. Nulla interdum iaculis lacus a finibus.
Nullam vitae posuere lorem. Vivamus gravida malesuada convallis. Curabitur dui nibh, condimentum at cursus in, elementum ut mauris. Nam ac lectus a lectus pharetra ultricies nec quis nisl. Integer sit amet tellus in nisi mattis aliquet non eu sapien. Morbi eget porttitor eros. Quisque non mauris tortor. Fusce lobortis lacus libero, a vestibulum massa fermentum vitae.
Aliquam eu nisl in metus sollicitudin cursus vel non ligula. Aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean lectus nibh, lobortis vitae lacinia posuere, eleifend nec nisi. Nulla faucibus tempus pharetra. Aliquam ipsum quam, pharetra ac molestie nec, faucibus eu turpis. Quisque congue urna ut nisi posuere aliquet. Cras consectetur efficitur enim. Nam quis urna sit amet tortor cursus vehicula quis nec nisi. Ut consequat sapien in erat sollicitudin sollicitudin. Proin eu consectetur velit, vel vulputate nunc. Aenean ut lacus eros. Donec pretium dolor a ex pulvinar, at condimentum mauris venenatis. Pellentesque ipsum tellus, ornare ut lacus id, congue auctor erat. Donec mattis purus sed feugiat condimentum.
Suspendisse potenti. Curabitur nibh nunc, vulputate eget massa id, dictum gravida dolor. Praesent dapibus vulputate sodales. Nulla in ex nisl. Cras dictum malesuada facilisis. Maecenas efficitur cursus turpis, vitae pharetra lacus fringilla eget. Nullam eleifend nulla sodales imperdiet consectetur. Vivamus non metus magna. Aenean tincidunt elementum enim, sed feugiat tortor. Quisque aliquet pulvinar diam, hendrerit blandit mauris. Sed viverra aliquet imperdiet.
Quisque a orci tempor, luctus arcu eget, rutrum augue. Donec lobortis ipsum vel eros tempor, a tempus justo aliquet. Duis congue turpis quis diam sodales, ac iaculis metus maximus. Donec nec neque quis orci tempus volutpat vel ac arcu. Cras posuere eget tellus ac tristique. Quisque vel lacinia arcu, posuere egestas lacus. Morbi feugiat ante vitae nulla venenatis, eget pulvinar tellus tristique. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nunc egestas feugiat quam accumsan laoreet. Ut a purus sagittis, vestibulum arcu vitae, gravida mi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed maximus metus eget est dictum consequat. Cras feugiat, lacus sit amet auctor feugiat, nulla mauris tincidunt augue, id pretium libero risus non sapien.
Quisque arcu nunc, feugiat ut mi quis, blandit varius elit. Quisque ullamcorper quam quis lectus varius auctor. Ut suscipit tellus justo, eget interdum dui placerat at. Nunc mattis augue eu justo condimentum fermentum eu nec magna. Pellentesque nec ante blandit, dapibus erat ut.
    """

    to_pairs_trasform = partial(to_pairs, context)

    words = sc.parallelize(text.split())
    pairs = words.map(to_pairs_trasform)
    counts = pairs.reduceByKey(lambda a, b: a+b)
    ordered = counts.sortBy(lambda pair: pair[1], ascending=False)

    result = ordered.collect()
    print result
    context.print_accumulators()

    return result
