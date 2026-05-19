# file: quotes/views.py

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import random

quotes = [
    "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.",
    "We delight in the beauty of the butterfly, but rarely admit the changes it has gone through to achieve that beauty.",
    "Courage is the most important of all the virtues because without courage, you can't practice any other virtue consistently.",
    "I can be changed by what happens to me. But I refuse to be reduced by it.",
    "Success is liking yourself, liking what you do, and liking how you do it.",
]

images = [
    "https://www.victoryforwomen.org/sites/default/files/share_bundle/Maya%20Angelou.jpg",
    "https://gcp-na-images.contentstack.com/v3/assets/bltea6093859af6183b/blt4c04c6767ac8aa24/6986910f13c79f0db6192412/ap060912044082.jpg?branch=production&width=3840&quality=75&auto=webp&crop=3:2",
    "https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2014/5/30/1401465497478/Maya-Angelou---1972-011.jpg?width=465&dpr=1&s=none&crop=none",
    "https://www.thenation.com/wp-content/uploads/2015/04/maya_angelou_ap_img.jpg",
    "https://ivyprosper.files.wordpress.com/2014/06/maya-angelou-young.jpg?w=1000&h=1033",
]

# Create your views here.
def quote(request):
    '''Fund to respond to the "quote" request.'''

    template_name = 'quotes/quote.html'
     # a dict of context variables (key-value pairs)
    context = {
        "quote": random.choice(quotes),
        "image": random.choice(images),
    }
    return render(request, template_name, context)

def show_all(request):
    '''Respond to the URL 'show_all', delegate work to a template.'''

    template_name = 'quotes/show_all.html'
    # a dict of context variables (key-value pairs)
    context = {
        "quotes": quotes,
        "images": images,
    }
    return render(request, template_name, context)



def about(request):
    '''Respond to the URL 'about', delegate work to a template.'''

    template_name = 'quotes/about.html'
    # a dict of context variables (key-value pairs)
    context = {
    
    }
    return render(request, template_name, context)